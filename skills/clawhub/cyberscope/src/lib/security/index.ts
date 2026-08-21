/**
 * Security Module - Main Export
 * Centralized security utilities for the CyberScope application
 */

export * from "./config";
export * from "./rate-limiter";
export * from "./validator";
export * from "./headers";
export * from "./middleware";

// Re-export commonly used functions for convenience
export {
  SECURITY_CONFIG,
} from "./config";

export {
  checkRateLimit,
  getClientIdentifier,
} from "./rate-limiter";

export {
  sanitizeString,
  sanitizeForSearch,
  sanitizeSlug,
  searchQuerySchema,
  methodsQuerySchema,
  parseSearchParams,
  validateInt,
} from "./validator";

export {
  secureJsonResponse,
  secureErrorResponse,
  rateLimitResponse,
  applySecurityHeaders,
} from "./headers";

export {
  enforceSecurityMiddleware,
  wrapSecureResponse,
  validateRequestBody,
} from "./middleware";
