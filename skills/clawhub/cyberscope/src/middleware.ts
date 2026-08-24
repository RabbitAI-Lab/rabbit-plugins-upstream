import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";

/**
 * Edge Middleware for CyberScope Security
 * Runs before any request reaches the application
 */

// Security configuration for middleware
const MAX_URL_LENGTH = 2048;
const MAX_HEADER_SIZE = 8192;

// Suspicious paths that should be blocked at edge
const BLOCKED_PATHS = [
  /\.php$/i,
  /\.asp$/i,
  /\.aspx$/i,
  /\.jsp$/i,
  /\.cgi$/i,
  /\.env/i,
  /wp-admin/i,
  /wp-login/i,
  /wp-content/i,
  /wp-includes/i,
  /wp-config/i,
  /phpmyadmin/i,
  /phpinfo/i,
  /adminer/i,
  /\.git\//i,
  /\.svn\//i,
  /\.hg\//i,
  /\.htaccess/i,
  /\.htpasswd/i,
  /web\.config/i,
  /\.DS_Store/i,
  /Thumbs\.db/i,
  /\.bak$/i,
  /\.backup$/i,
  /\.old$/i,
  /\.orig$/i,
  /\.sql$/i,
  /\.tar$/i,
  /\.tar\.gz$/i,
  /\.zip$/i,
  /\.rar$/i,
  /\.7z$/i,
  /\/\./,  // Hidden files
  /\.\./,  // Path traversal
];

// Blocked user agents (scanners, exploit tools)
// Note: curl and wget are allowed as they're commonly used by legitimate tools
const BLOCKED_USER_AGENTS = [
  /sqlmap/i,
  /nikto/i,
  /nmap/i,
  /masscan/i,
  /gobuster/i,
  /dirbuster/i,
  /dirb/i,
  /wfuzz/i,
  /ffuf/i,
  /feroxbuster/i,
  /nuclei/i,
  /jaeles/i,
  /acunetix/i,
  /netsparker/i,
  /burpsuite/i,
  /owasp-zap/i,
  /arachni/i,
  /vega\//i,
  /w3af/i,
  /wapiti/i,
  /skipfish/i,
  /havij/i,
];

// Suspicious request headers that could indicate attacks
// Note: x-forwarded-host is allowed as proxies legitimately use it
const SUSPICIOUS_HEADERS = [
  "x-original-url",    // Potential path override (IIS specific attack)
  "x-rewrite-url",     // Potential path override (IIS specific attack)
];

export function middleware(request: NextRequest) {
  const url = request.nextUrl;
  const pathname = url.pathname;
  
  // Allow health check endpoint without any restrictions
  if (pathname === "/api/health") {
    return NextResponse.next();
  }
  
  // 1. Block oversized URLs
  if (request.url.length > MAX_URL_LENGTH) {
    return new NextResponse("URI Too Long", { status: 414 });
  }
  
  // 2. Block suspicious paths
  for (const pattern of BLOCKED_PATHS) {
    if (pattern.test(pathname)) {
      console.warn(`[SECURITY:EDGE] Blocked path: ${pathname}`);
      return new NextResponse("Forbidden", { status: 403 });
    }
  }
  
  // 3. Block malicious user agents
  const userAgent = request.headers.get("user-agent") || "";
  for (const pattern of BLOCKED_USER_AGENTS) {
    if (pattern.test(userAgent)) {
      console.warn(`[SECURITY:EDGE] Blocked user agent: ${userAgent.slice(0, 50)}`);
      return new NextResponse("Forbidden", { status: 403 });
    }
  }
  
  // 4. Block requests with suspicious headers
  for (const header of SUSPICIOUS_HEADERS) {
    if (request.headers.has(header)) {
      console.warn(`[SECURITY:EDGE] Suspicious header: ${header}`);
      return new NextResponse("Bad Request", { status: 400 });
    }
  }
  
  // 5. Check for oversized headers (potential header injection/overflow)
  let totalHeaderSize = 0;
  request.headers.forEach((value, key) => {
    totalHeaderSize += key.length + value.length;
  });
  if (totalHeaderSize > MAX_HEADER_SIZE) {
    console.warn(`[SECURITY:EDGE] Oversized headers: ${totalHeaderSize} bytes`);
    return new NextResponse("Request Header Fields Too Large", { status: 431 });
  }
  
  // 6. Block requests with null bytes in URL (injection attempt)
  if (pathname.includes("%00") || pathname.includes("\0")) {
    console.warn(`[SECURITY:EDGE] Null byte in path`);
    return new NextResponse("Bad Request", { status: 400 });
  }
  
  // 7. Block double-encoded paths (evasion attempt)
  if (/%25[0-9a-fA-F]{2}/.test(pathname)) {
    console.warn(`[SECURITY:EDGE] Double-encoded path detected`);
    return new NextResponse("Bad Request", { status: 400 });
  }
  
  // 8. Add security headers to response
  const response = NextResponse.next();
  
  // Add request ID for tracing
  const requestId = `edge_${Date.now().toString(36)}_${Math.random().toString(36).slice(2, 7)}`;
  response.headers.set("X-Request-ID", requestId);
  
  // Add timing header (useful for debugging, remove in ultra-secure mode)
  response.headers.set("X-Response-Time", new Date().toISOString());
  
  return response;
}

// Configure which paths the middleware runs on
export const config = {
  matcher: [
    /*
     * Match all request paths except:
     * - _next/static (static files)
     * - _next/image (image optimization files)
     * - favicon.ico (favicon file)
     */
    "/((?!_next/static|_next/image|favicon.ico).*)",
  ],
};
