/**
 * Input Validation & Sanitization Module
 * Provides defense against injection attacks, XSS, and malicious input
 */

import { z } from "zod";
import { SECURITY_CONFIG } from "./config";

/**
 * Check string against dangerous patterns
 */
function containsDangerousPatterns(input: string): { safe: boolean; reason?: string } {
  // Check SQL injection patterns
  for (const pattern of SECURITY_CONFIG.input.sqlInjectionPatterns) {
    if (pattern.test(input)) {
      return { safe: false, reason: "Potential SQL injection detected" };
    }
  }
  
  // Check XSS patterns
  for (const pattern of SECURITY_CONFIG.input.xssPatterns) {
    if (pattern.test(input)) {
      return { safe: false, reason: "Potential XSS attack detected" };
    }
  }
  
  // Check path traversal patterns
  for (const pattern of SECURITY_CONFIG.input.pathTraversalPatterns) {
    if (pattern.test(input)) {
      return { safe: false, reason: "Potential path traversal detected" };
    }
  }
  
  return { safe: true };
}

/**
 * Sanitize string input - remove dangerous characters and normalize
 */
export function sanitizeString(input: string): string {
  if (typeof input !== "string") return "";
  
  // Trim and limit length
  let sanitized = input.trim().slice(0, SECURITY_CONFIG.input.maxQueryLength);
  
  // Remove null bytes
  sanitized = sanitized.replace(/\0/g, "");
  
  // Normalize unicode to prevent homograph attacks
  sanitized = sanitized.normalize("NFKC");
  
  // Remove control characters except common whitespace
  sanitized = sanitized.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "");
  
  // Escape HTML entities
  sanitized = sanitized
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;");
  
  return sanitized;
}

/**
 * Sanitize for SQL-safe search (decode HTML entities for DB search)
 */
export function sanitizeForSearch(input: string): string {
  if (typeof input !== "string") return "";
  
  let sanitized = input.trim().slice(0, SECURITY_CONFIG.input.maxQueryLength);
  
  // Remove null bytes
  sanitized = sanitized.replace(/\0/g, "");
  
  // Normalize unicode
  sanitized = sanitized.normalize("NFKC");
  
  // Remove control characters
  sanitized = sanitized.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, "");
  
  // Remove SQL dangerous characters but keep search-friendly ones
  sanitized = sanitized.replace(/[;'"\\`]/g, "");
  
  // Collapse multiple spaces
  sanitized = sanitized.replace(/\s+/g, " ");
  
  return sanitized;
}

/**
 * Validate and sanitize slug (category, etc.)
 */
export function sanitizeSlug(input: string): string {
  if (typeof input !== "string") return "";
  
  return input
    .toLowerCase()
    .trim()
    .slice(0, SECURITY_CONFIG.input.maxCategorySlugLength)
    .replace(/[^a-z0-9-]/g, "")
    .replace(/-+/g, "-")
    .replace(/^-|-$/g, "");
}

/**
 * Zod Schemas for API Input Validation
 */

// Custom refinement for dangerous patterns
const safeString = z.string().refine(
  (val) => containsDangerousPatterns(val).safe,
  { message: "Invalid input detected" }
);

// Export for use in other modules
export { safeString };

// Search query schema
export const searchQuerySchema = z.object({
  q: z.string()
    .max(SECURITY_CONFIG.input.maxQueryLength, "Query too long")
    .optional()
    .default("")
    .transform(sanitizeForSearch),
  category: z.string()
    .max(SECURITY_CONFIG.input.maxCategorySlugLength)
    .optional()
    .default("")
    .transform(sanitizeSlug),
  page: z.string()
    .optional()
    .default("1")
    .transform((val) => {
      const num = parseInt(val, 10);
      if (isNaN(num) || num < 1) return 1;
      return Math.min(num, SECURITY_CONFIG.input.maxPageNumber);
    }),
  limit: z.string()
    .optional()
    .default(String(SECURITY_CONFIG.input.defaultLimit))
    .transform((val) => {
      const num = parseInt(val, 10);
      if (isNaN(num) || num < SECURITY_CONFIG.input.minLimitPerPage) {
        return SECURITY_CONFIG.input.defaultLimit;
      }
      return Math.min(num, SECURITY_CONFIG.input.maxLimitPerPage);
    }),
});

// Methods query schema
export const methodsQuerySchema = z.object({
  category: z.string()
    .max(SECURITY_CONFIG.input.maxCategorySlugLength)
    .optional()
    .transform((val) => val ? sanitizeSlug(val) : undefined),
  id: z.string()
    .optional()
    .transform((val) => {
      if (!val) return undefined;
      const num = parseInt(val, 10);
      if (isNaN(num) || num < 1 || num > 1000) return undefined;
      return num;
    }),
});

// Generic ID schema
export const idSchema = z.object({
  id: z.string()
    .transform((val) => {
      const num = parseInt(val, 10);
      if (isNaN(num) || num < 1) throw new Error("Invalid ID");
      return num;
    }),
});

/**
 * Validate request body size
 */
export function validateBodySize(body: string | null): boolean {
  if (!body) return true;
  return body.length <= SECURITY_CONFIG.request.maxBodySize;
}

/**
 * Validate URL length
 */
export function validateUrlLength(url: string): boolean {
  return url.length <= SECURITY_CONFIG.request.maxUrlLength;
}

/**
 * Validate and parse search params safely
 */
export function parseSearchParams(url: URL): Record<string, string> {
  const params: Record<string, string> = {};
  
  // Limit number of parameters
  let count = 0;
  const maxParams = 20;
  
  for (const [key, value] of url.searchParams) {
    if (count >= maxParams) break;
    
    // Sanitize key and value
    const safeKey = key.slice(0, 50).replace(/[^a-zA-Z0-9_-]/g, "");
    const safeValue = value.slice(0, SECURITY_CONFIG.input.maxQueryLength);
    
    if (safeKey) {
      params[safeKey] = safeValue;
      count++;
    }
  }
  
  return params;
}

/**
 * Validate that input only contains expected characters
 */
export function isAlphanumericWithSpaces(input: string): boolean {
  return /^[\w\s-]*$/.test(input);
}

/**
 * Validate integer within range
 */
export function validateInt(
  value: unknown,
  min: number,
  max: number,
  defaultValue: number
): number {
  if (typeof value === "number") {
    if (isNaN(value) || value < min) return defaultValue;
    return Math.min(value, max);
  }
  
  if (typeof value === "string") {
    const num = parseInt(value, 10);
    if (isNaN(num) || num < min) return defaultValue;
    return Math.min(num, max);
  }
  
  return defaultValue;
}

export type SearchQueryInput = z.infer<typeof searchQuerySchema>;
export type MethodsQueryInput = z.infer<typeof methodsQuerySchema>;
