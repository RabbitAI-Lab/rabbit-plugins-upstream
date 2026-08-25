/**
 * Security Headers Module
 * Applies comprehensive security headers to all responses
 */

import { NextResponse } from "next/server";
import { SECURITY_CONFIG } from "./config";

/**
 * Apply all security headers to a NextResponse
 */
export function applySecurityHeaders(response: NextResponse): NextResponse {
  const headers = SECURITY_CONFIG.headers;
  
  // Content Security Policy
  response.headers.set("Content-Security-Policy", headers.csp);
  
  // Prevent MIME type sniffing
  response.headers.set("X-Content-Type-Options", headers.xContentTypeOptions);
  
  // Prevent clickjacking
  response.headers.set("X-Frame-Options", headers.xFrameOptions);
  
  // XSS Protection (legacy but still useful)
  response.headers.set("X-XSS-Protection", headers.xXssProtection);
  
  // Control referrer information
  response.headers.set("Referrer-Policy", headers.referrerPolicy);
  
  // HTTP Strict Transport Security
  response.headers.set("Strict-Transport-Security", headers.strictTransportSecurity);
  
  // Permissions Policy (formerly Feature-Policy)
  response.headers.set("Permissions-Policy", headers.permissionsPolicy);
  
  // Prevent caching of sensitive data
  response.headers.set("Cache-Control", headers.cacheControl);
  response.headers.set("Pragma", headers.pragma);
  response.headers.set("Expires", headers.expires);
  
  // Additional security headers
  response.headers.set("X-DNS-Prefetch-Control", "off");
  response.headers.set("X-Download-Options", "noopen");
  response.headers.set("X-Permitted-Cross-Domain-Policies", "none");
  response.headers.set("Cross-Origin-Opener-Policy", "same-origin");
  response.headers.set("Cross-Origin-Resource-Policy", "same-origin");
  response.headers.set("Cross-Origin-Embedder-Policy", "require-corp");
  
  return response;
}

/**
 * Create a secure JSON response with all security headers
 */
export function secureJsonResponse(
  data: unknown,
  status: number = 200
): NextResponse {
  const response = NextResponse.json(data, { status });
  return applySecurityHeaders(response);
}

/**
 * Create a secure error response
 */
export function secureErrorResponse(
  message: string,
  status: number = 500
): NextResponse {
  // Never expose internal error details
  const safeMessage = status >= 500 
    ? SECURITY_CONFIG.errors.generic 
    : message;
    
  const response = NextResponse.json(
    { error: safeMessage },
    { status }
  );
  return applySecurityHeaders(response);
}

/**
 * Create rate limit exceeded response
 */
export function rateLimitResponse(resetTime: number): NextResponse {
  const response = NextResponse.json(
    { error: SECURITY_CONFIG.errors.rateLimit },
    { status: 429 }
  );
  
  response.headers.set("Retry-After", String(Math.ceil((resetTime - Date.now()) / 1000)));
  response.headers.set("X-RateLimit-Remaining", "0");
  
  return applySecurityHeaders(response);
}

/**
 * Add rate limit headers to response
 */
export function addRateLimitHeaders(
  response: NextResponse,
  remaining: number,
  resetTime: number
): NextResponse {
  response.headers.set("X-RateLimit-Remaining", String(remaining));
  response.headers.set("X-RateLimit-Reset", String(Math.ceil(resetTime / 1000)));
  return response;
}
