/**
 * In-Memory Rate Limiter with Sliding Window Algorithm
 * Provides protection against brute force and DDoS attacks
 */

import { SECURITY_CONFIG } from "./config";

interface RateLimitEntry {
  count: number;
  windowStart: number;
  blocked: boolean;
  blockedUntil: number;
}

// In-memory store (in production, use Redis)
const rateLimitStore = new Map<string, RateLimitEntry>();

// Cleanup old entries periodically
const CLEANUP_INTERVAL = 60 * 1000; // 1 minute
let lastCleanup = Date.now();

function cleanupExpiredEntries(): void {
  const now = Date.now();
  if (now - lastCleanup < CLEANUP_INTERVAL) return;
  
  lastCleanup = now;
  const windowMs = SECURITY_CONFIG.rateLimit.windowMs;
  
  for (const [key, entry] of rateLimitStore.entries()) {
    if (now - entry.windowStart > windowMs * 2 && !entry.blocked) {
      rateLimitStore.delete(key);
    }
    if (entry.blocked && now > entry.blockedUntil) {
      rateLimitStore.delete(key);
    }
  }
}

export type EndpointType = keyof typeof SECURITY_CONFIG.rateLimit.maxRequests;

export interface RateLimitResult {
  allowed: boolean;
  remaining: number;
  resetTime: number;
  blocked: boolean;
}

/**
 * Check if a request is rate limited
 * Uses sliding window algorithm for accurate rate limiting
 */
export function checkRateLimit(
  identifier: string,
  endpoint: EndpointType = "default"
): RateLimitResult {
  cleanupExpiredEntries();
  
  const now = Date.now();
  const windowMs = SECURITY_CONFIG.rateLimit.windowMs;
  const maxRequests = SECURITY_CONFIG.rateLimit.maxRequests[endpoint];
  const key = `${identifier}:${endpoint}`;
  
  let entry = rateLimitStore.get(key);
  
  // Check if currently blocked
  if (entry?.blocked && now < entry.blockedUntil) {
    return {
      allowed: false,
      remaining: 0,
      resetTime: entry.blockedUntil,
      blocked: true,
    };
  }
  
  // Reset if window expired or first request
  if (!entry || now - entry.windowStart > windowMs) {
    entry = {
      count: 0,
      windowStart: now,
      blocked: false,
      blockedUntil: 0,
    };
  }
  
  // Increment request count
  entry.count++;
  
  // Check if limit exceeded
  if (entry.count > maxRequests) {
    // Block the client
    entry.blocked = true;
    entry.blockedUntil = now + SECURITY_CONFIG.rateLimit.blockDurationMs;
    rateLimitStore.set(key, entry);
    
    if (SECURITY_CONFIG.logging.logRateLimitViolations) {
      console.warn(`[SECURITY] Rate limit exceeded: ${identifier} on ${endpoint}`);
    }
    
    return {
      allowed: false,
      remaining: 0,
      resetTime: entry.blockedUntil,
      blocked: true,
    };
  }
  
  rateLimitStore.set(key, entry);
  
  return {
    allowed: true,
    remaining: maxRequests - entry.count,
    resetTime: entry.windowStart + windowMs,
    blocked: false,
  };
}

/**
 * Get client identifier from request
 * Uses multiple factors for accurate identification
 */
export function getClientIdentifier(request: Request): string {
  const forwarded = request.headers.get("x-forwarded-for");
  const realIp = request.headers.get("x-real-ip");
  const cfIp = request.headers.get("cf-connecting-ip");
  
  // Prefer Cloudflare IP, then X-Real-IP, then X-Forwarded-For
  let ip = cfIp || realIp || (forwarded ? forwarded.split(",")[0].trim() : null) || "unknown";
  
  // Sanitize IP to prevent header injection
  ip = ip.replace(/[^a-fA-F0-9.:]/g, "").slice(0, 45);
  
  // Add user agent fingerprint for additional entropy
  const userAgent = request.headers.get("user-agent") || "";
  const uaHash = simpleHash(userAgent);
  
  return `${ip}:${uaHash}`;
}

/**
 * Simple hash function for fingerprinting
 */
function simpleHash(str: string): string {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    const char = str.charCodeAt(i);
    hash = ((hash << 5) - hash) + char;
    hash = hash & hash;
  }
  return Math.abs(hash).toString(16).slice(0, 8);
}

/**
 * Reset rate limit for an identifier (for testing)
 */
export function resetRateLimit(identifier: string): void {
  for (const key of rateLimitStore.keys()) {
    if (key.startsWith(identifier)) {
      rateLimitStore.delete(key);
    }
  }
}
