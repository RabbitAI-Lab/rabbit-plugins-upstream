/**
 * Client-side Security Utilities
 * Sanitization and validation for browser-side code
 */

/**
 * Sanitize text for safe display in HTML
 * React already escapes by default, but this adds an extra layer
 */
export function sanitizeDisplayText(text: string | null | undefined): string {
  if (!text) return "";
  
  return text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#x27;")
    .replace(/\//g, "&#x2F;");
}

/**
 * Sanitize URL for safe use in href attributes
 */
export function sanitizeUrl(url: string | null | undefined): string {
  if (!url) return "#";
  
  // Trim and normalize
  const trimmed = url.trim();
  
  // Block dangerous protocols
  const dangerousProtocols = [
    "javascript:",
    "data:",
    "vbscript:",
    "file:",
    "about:",
  ];
  
  const lowerUrl = trimmed.toLowerCase();
  for (const protocol of dangerousProtocols) {
    if (lowerUrl.startsWith(protocol)) {
      console.warn("[SECURITY] Blocked dangerous URL protocol:", protocol);
      return "#";
    }
  }
  
  // Only allow http, https, and relative URLs
  if (
    trimmed.startsWith("http://") ||
    trimmed.startsWith("https://") ||
    trimmed.startsWith("/") ||
    trimmed.startsWith("#")
  ) {
    return trimmed;
  }
  
  // Assume https for protocol-relative URLs
  if (trimmed.startsWith("//")) {
    return `https:${trimmed}`;
  }
  
  // For other URLs, prepend https
  return `https://${trimmed}`;
}

/**
 * Validate and sanitize search input
 */
export function sanitizeSearchInput(input: string): string {
  if (!input) return "";
  
  // Limit length
  let sanitized = input.slice(0, 200);
  
  // Remove control characters
  sanitized = sanitized.replace(/[\x00-\x1F\x7F]/g, "");
  
  // Normalize whitespace
  sanitized = sanitized.replace(/\s+/g, " ").trim();
  
  return sanitized;
}

/**
 * Create a safe click handler for external links
 */
export function createSafeExternalLinkHandler(url: string) {
  return (e: React.MouseEvent) => {
    e.preventDefault();
    const safeUrl = sanitizeUrl(url);
    if (safeUrl !== "#") {
      window.open(safeUrl, "_blank", "noopener,noreferrer");
    }
  };
}

/**
 * Validate that a value is a safe integer
 */
export function validateSafeInteger(
  value: unknown,
  min: number,
  max: number,
  defaultValue: number
): number {
  if (typeof value === "number") {
    if (!Number.isInteger(value) || value < min || value > max) {
      return defaultValue;
    }
    return value;
  }
  
  if (typeof value === "string") {
    const num = parseInt(value, 10);
    if (!Number.isInteger(num) || num < min || num > max) {
      return defaultValue;
    }
    return num;
  }
  
  return defaultValue;
}

/**
 * Rate limiter for client-side operations
 */
class ClientRateLimiter {
  private timestamps: number[] = [];
  private readonly maxRequests: number;
  private readonly windowMs: number;

  constructor(maxRequests: number = 10, windowMs: number = 1000) {
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
  }

  canMakeRequest(): boolean {
    const now = Date.now();
    
    // Remove old timestamps
    this.timestamps = this.timestamps.filter(t => now - t < this.windowMs);
    
    if (this.timestamps.length >= this.maxRequests) {
      return false;
    }
    
    this.timestamps.push(now);
    return true;
  }

  reset(): void {
    this.timestamps = [];
  }
}

// Export singleton rate limiter for search
export const searchRateLimiter = new ClientRateLimiter(5, 1000); // 5 searches per second max

/**
 * Debounce function for search input
 */
export function debounce<T extends (...args: Parameters<T>) => ReturnType<T>>(
  func: T,
  wait: number
): (...args: Parameters<T>) => void {
  let timeout: NodeJS.Timeout | null = null;
  
  return function(...args: Parameters<T>) {
    if (timeout) {
      clearTimeout(timeout);
    }
    timeout = setTimeout(() => {
      func(...args);
    }, wait);
  };
}
