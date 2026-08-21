/**
 * Security Configuration - Central security settings
 * All security parameters are defined here for easy auditing
 */

export const SECURITY_CONFIG = {
  // Rate Limiting
  rateLimit: {
    windowMs: 60 * 1000, // 1 minute window
    maxRequests: {
      search: 30,      // 30 searches per minute
      seed: 3,         // 3 seed attempts per minute
      categories: 60,  // 60 category requests per minute
      methods: 60,     // 60 method requests per minute
      stats: 30,       // 30 stats requests per minute
      default: 100,    // 100 requests per minute for other endpoints
    },
    blockDurationMs: 5 * 60 * 1000, // 5 minute block for violators
  },

  // Input Validation Limits
  input: {
    maxQueryLength: 200,
    maxCategorySlugLength: 100,
    maxPageNumber: 1000,
    maxLimitPerPage: 100,
    minLimitPerPage: 1,
    defaultLimit: 20,
    allowedCharactersRegex: /^[\w\s\-.,!?@#$%^&*()+=[\]{}|\\:;"'<>/]*$/,
    // Block common SQL injection patterns
    sqlInjectionPatterns: [
      /(\b(SELECT|INSERT|UPDATE|DELETE|DROP|UNION|ALTER|CREATE|TRUNCATE)\b)/i,
      /(--|;|\/\*|\*\/|@@|@)/,
      /(\bOR\b|\bAND\b).*[=<>]/i,
      /\b(EXEC|EXECUTE|SP_|XP_)\b/i,
    ],
    // Block common XSS patterns
    xssPatterns: [
      /<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi,
      /javascript:/gi,
      /on\w+\s*=/gi,
      /<iframe/gi,
      /<object/gi,
      /<embed/gi,
      /data:/gi,
      /vbscript:/gi,
    ],
    // Block path traversal
    pathTraversalPatterns: [
      /\.\.\//g,
      /\.\.%2f/gi,
      /%2e%2e%2f/gi,
      /%252e%252e%252f/gi,
    ],
  },

  // Response Headers
  headers: {
    // Content Security Policy
    csp: [
      "default-src 'self'",
      "script-src 'self' 'unsafe-inline' 'unsafe-eval'", // Required for Next.js
      "style-src 'self' 'unsafe-inline'", // Required for Tailwind
      "img-src 'self' data: https:",
      "font-src 'self'",
      "connect-src 'self'",
      "frame-ancestors 'none'",
      "base-uri 'self'",
      "form-action 'self'",
      "upgrade-insecure-requests",
    ].join("; "),
    
    // Other security headers
    xContentTypeOptions: "nosniff",
    xFrameOptions: "DENY",
    xXssProtection: "1; mode=block",
    referrerPolicy: "strict-origin-when-cross-origin",
    strictTransportSecurity: "max-age=31536000; includeSubDomains; preload",
    permissionsPolicy: [
      "accelerometer=()",
      "camera=()",
      "geolocation=()",
      "gyroscope=()",
      "magnetometer=()",
      "microphone=()",
      "payment=()",
      "usb=()",
      "interest-cohort=()",
    ].join(", "),
    cacheControl: "no-store, no-cache, must-revalidate, proxy-revalidate",
    pragma: "no-cache",
    expires: "0",
  },

  // Session/Request security
  request: {
    maxBodySize: 10 * 1024, // 10KB max body size
    timeout: 30000, // 30 second timeout
    maxUrlLength: 2048,
  },

  // Logging
  logging: {
    logSuspiciousActivity: true,
    logRateLimitViolations: true,
    sanitizeLogsForPII: true,
  },

  // Error Messages (generic to prevent info leakage)
  errors: {
    generic: "An error occurred while processing your request",
    validation: "Invalid input provided",
    rateLimit: "Too many requests. Please try again later",
    notFound: "Resource not found",
    forbidden: "Access denied",
    badRequest: "Bad request",
  },
} as const;

export type SecurityConfig = typeof SECURITY_CONFIG;
