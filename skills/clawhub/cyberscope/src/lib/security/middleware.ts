/**
 * Security Middleware Module
 * Central security enforcement for all API routes
 */

import { NextRequest, NextResponse } from "next/server";
import { SECURITY_CONFIG } from "./config";
import { checkRateLimit, getClientIdentifier, type EndpointType } from "./rate-limiter";
import { validateUrlLength, validateBodySize } from "./validator";
import { 
  secureErrorResponse, 
  rateLimitResponse, 
  applySecurityHeaders,
  addRateLimitHeaders 
} from "./headers";

export interface SecurityContext {
  clientId: string;
  timestamp: number;
  requestId: string;
}

/**
 * Generate a unique request ID
 */
function generateRequestId(): string {
  return `req_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 9)}`;
}

/**
 * Log security events
 */
function logSecurityEvent(
  event: string,
  context: SecurityContext,
  details?: Record<string, unknown>
): void {
  if (!SECURITY_CONFIG.logging.logSuspiciousActivity) return;
  
  // Sanitize client ID for logging
  const sanitizedClientId = SECURITY_CONFIG.logging.sanitizeLogsForPII
    ? context.clientId.replace(/(\d+\.){3}\d+/, "[IP_REDACTED]")
    : context.clientId;
    
  console.warn(`[SECURITY] ${event}`, {
    requestId: context.requestId,
    clientId: sanitizedClientId,
    timestamp: new Date(context.timestamp).toISOString(),
    ...details,
  });
}

/**
 * Detect potential bot/scanner signatures
 */
function detectSuspiciousUserAgent(userAgent: string | null): boolean {
  if (!userAgent) return true; // No user agent is suspicious
  
  const suspiciousPatterns = [
    /curl/i,
    /wget/i,
    /python-requests/i,
    /python-urllib/i,
    /libwww/i,
    /httpunit/i,
    /nutch/i,
    /scrapy/i,
    /mj12bot/i,
    /semrush/i,
    /ahrefsbot/i,
    /dotbot/i,
    /scanner/i,
    /nikto/i,
    /sqlmap/i,
    /nmap/i,
    /masscan/i,
    /gobuster/i,
    /dirbuster/i,
    /burp/i,
    /zap\//i,
  ];
  
  return suspiciousPatterns.some(pattern => pattern.test(userAgent));
}

/**
 * Detect suspicious request patterns
 */
function detectSuspiciousRequest(request: NextRequest): { suspicious: boolean; reason?: string } {
  const url = request.url;
  const method = request.method;
  
  // Check for common attack paths
  const suspiciousPaths = [
    /\.php$/i,
    /\.asp$/i,
    /\.env/i,
    /wp-admin/i,
    /wp-login/i,
    /wp-config/i,
    /phpmyadmin/i,
    /admin\.php/i,
    /shell/i,
    /\.git\//i,
    /\.svn\//i,
    /\.htaccess/i,
    /\.htpasswd/i,
    /web\.config/i,
    /crossdomain\.xml/i,
    /clientaccesspolicy\.xml/i,
  ];
  
  for (const pattern of suspiciousPaths) {
    if (pattern.test(url)) {
      return { suspicious: true, reason: `Suspicious path pattern: ${pattern}` };
    }
  }
  
  // Check for unusual HTTP methods
  const allowedMethods = ["GET", "POST", "OPTIONS", "HEAD"];
  if (!allowedMethods.includes(method)) {
    return { suspicious: true, reason: `Unusual HTTP method: ${method}` };
  }
  
  return { suspicious: false };
}

/**
 * Main security middleware function
 * Should be called at the start of every API route
 */
export async function enforceSecurityMiddleware(
  request: NextRequest,
  endpoint: EndpointType = "default"
): Promise<{ allowed: true; context: SecurityContext } | { allowed: false; response: NextResponse }> {
  const context: SecurityContext = {
    clientId: getClientIdentifier(request),
    timestamp: Date.now(),
    requestId: generateRequestId(),
  };
  
  // 1. Check URL length
  if (!validateUrlLength(request.url)) {
    logSecurityEvent("URL too long", context, { urlLength: request.url.length });
    return {
      allowed: false,
      response: secureErrorResponse(SECURITY_CONFIG.errors.badRequest, 414),
    };
  }
  
  // 2. Check for suspicious request patterns
  const suspiciousCheck = detectSuspiciousRequest(request);
  if (suspiciousCheck.suspicious) {
    logSecurityEvent("Suspicious request blocked", context, { reason: suspiciousCheck.reason });
    return {
      allowed: false,
      response: secureErrorResponse(SECURITY_CONFIG.errors.forbidden, 403),
    };
  }
  
  // 3. Check for suspicious user agent (log but allow)
  const userAgent = request.headers.get("user-agent");
  if (detectSuspiciousUserAgent(userAgent)) {
    logSecurityEvent("Suspicious user agent", context, { 
      userAgent: userAgent?.slice(0, 100) || "none" 
    });
    // Don't block, just log - could be legitimate automation
  }
  
  // 4. Rate limiting
  const rateLimitResult = checkRateLimit(context.clientId, endpoint);
  if (!rateLimitResult.allowed) {
    logSecurityEvent("Rate limit exceeded", context, { endpoint });
    return {
      allowed: false,
      response: rateLimitResponse(rateLimitResult.resetTime),
    };
  }
  
  // 5. All checks passed
  return { allowed: true, context };
}

/**
 * Wrap a response with security headers and rate limit info
 */
export function wrapSecureResponse(
  response: NextResponse,
  context: SecurityContext,
  endpoint: EndpointType = "default"
): NextResponse {
  // Apply security headers
  applySecurityHeaders(response);
  
  // Add request ID for tracing
  response.headers.set("X-Request-ID", context.requestId);
  
  // Add rate limit headers
  const rateLimitResult = checkRateLimit(context.clientId, endpoint);
  addRateLimitHeaders(response, rateLimitResult.remaining, rateLimitResult.resetTime);
  
  return response;
}

/**
 * Validate request body for POST requests
 */
export async function validateRequestBody(
  request: NextRequest
): Promise<{ valid: true; body: string } | { valid: false; response: NextResponse }> {
  try {
    const contentLength = request.headers.get("content-length");
    if (contentLength && parseInt(contentLength, 10) > SECURITY_CONFIG.request.maxBodySize) {
      return {
        valid: false,
        response: secureErrorResponse("Request body too large", 413),
      };
    }
    
    const body = await request.text();
    
    if (!validateBodySize(body)) {
      return {
        valid: false,
        response: secureErrorResponse("Request body too large", 413),
      };
    }
    
    return { valid: true, body };
  } catch {
    return {
      valid: false,
      response: secureErrorResponse(SECURITY_CONFIG.errors.badRequest, 400),
    };
  }
}
