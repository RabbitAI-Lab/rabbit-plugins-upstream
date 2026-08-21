# CyberScope Security Hardening Documentation

## Overview

CyberScope has been hardened with comprehensive, defense-in-depth security measures across all layers of the application. This document details all security controls implemented.

---

## 1. Edge-Level Protection (Middleware)

### 1.1 Path-Based Blocking
Automatically blocks requests to dangerous or sensitive paths:
- `.env`, `.git/`, `.svn/`, `.htaccess`, `.htpasswd`
- PHP/ASP/JSP files (attack surface reduction)
- WordPress paths (`wp-admin`, `wp-login`, `wp-config`)
- PHPMyAdmin, Adminer paths
- Backup files (`.bak`, `.backup`, `.old`, `.sql`)
- Archive files (`.tar`, `.zip`, `.rar`)

### 1.2 User-Agent Filtering
Blocks known attack tools:
- SQLMap, Nikto, Nmap, Masscan
- Directory busters (Gobuster, Dirbuster, DirB, FFUF)
- Vulnerability scanners (Nuclei, Acunetix, Netsparker)
- Penetration testing tools (BurpSuite, OWASP ZAP)

### 1.3 Header Injection Protection
Blocks suspicious headers used in attacks:
- `X-Original-URL` (IIS path override)
- `X-Rewrite-URL` (IIS path override)

### 1.4 URL Validation
- Maximum URL length: 2048 characters (414 response)
- Maximum header size: 8192 bytes (431 response)
- Null byte injection protection
- Double-encoding detection

---

## 2. Security Headers

All responses include comprehensive security headers:

| Header | Value | Purpose |
|--------|-------|---------|
| `Content-Security-Policy` | Strict policy | Prevents XSS, injection attacks |
| `X-Frame-Options` | DENY | Prevents clickjacking |
| `X-Content-Type-Options` | nosniff | Prevents MIME sniffing |
| `X-XSS-Protection` | 1; mode=block | Legacy XSS filter |
| `Strict-Transport-Security` | max-age=31536000; includeSubDomains; preload | Forces HTTPS |
| `Referrer-Policy` | strict-origin-when-cross-origin | Controls referrer info |
| `Permissions-Policy` | Restrictive | Disables dangerous features |
| `Cross-Origin-Opener-Policy` | same-origin | Isolates browsing context |
| `Cross-Origin-Resource-Policy` | same-origin | Prevents cross-origin reads |
| `Cross-Origin-Embedder-Policy` | require-corp | Enables COEP |
| `Cache-Control` | no-store | Prevents caching sensitive data |

---

## 3. Rate Limiting

### Per-Endpoint Limits (per minute)
| Endpoint | Limit | Block Duration |
|----------|-------|----------------|
| `/api/search` | 30 requests | 5 minutes |
| `/api/seed` | 3 requests | 5 minutes |
| `/api/categories` | 60 requests | 5 minutes |
| `/api/methods` | 60 requests | 5 minutes |
| `/api/stats` | 30 requests | 5 minutes |
| Default | 100 requests | 5 minutes |

### Implementation Details
- Sliding window algorithm for accuracy
- Client identification via IP + User-Agent fingerprint
- Cloudflare, X-Real-IP header support
- Rate limit headers in responses (`X-RateLimit-Remaining`, `X-RateLimit-Reset`)

---

## 4. Input Validation & Sanitization

### 4.1 Zod Schema Validation
All API inputs are validated with strict Zod schemas:
- Type checking
- Length limits
- Pattern validation
- Default value handling

### 4.2 SQL Injection Protection
**Patterns detected and blocked:**
- SQL keywords (SELECT, INSERT, UPDATE, DELETE, DROP, UNION, etc.)
- SQL comments (`--`, `/*`, `*/`)
- SQL special characters (`;`, `'`, `"`)
- Stored procedure calls (EXEC, EXECUTE, SP_, XP_)

**Additionally:**
- Drizzle ORM uses parameterized queries (never string concatenation)
- Input sanitization removes dangerous characters

### 4.3 XSS Protection
**Patterns detected and blocked:**
- Script tags (`<script>`)
- Event handlers (`onclick=`, `onload=`, etc.)
- JavaScript protocol (`javascript:`)
- VBScript protocol (`vbscript:`)
- Data URIs (`data:`)
- Iframe, object, embed tags

**Additionally:**
- HTML entity encoding for all output
- React's built-in escaping

### 4.4 Path Traversal Protection
**Patterns detected and blocked:**
- `../` sequences
- URL-encoded variants (`%2e%2e%2f`)
- Double-encoded variants

### 4.5 Input Limits
| Parameter | Max Length |
|-----------|------------|
| Search query | 200 characters |
| Category slug | 100 characters |
| Page number | 1-1000 |
| Limit per page | 1-100 |

---

## 5. Client-Side Security

### 5.1 URL Sanitization
External links are sanitized:
- Block dangerous protocols (`javascript:`, `data:`, `vbscript:`)
- Enforce `https://` for external URLs
- `rel="noopener noreferrer"` on all external links

### 5.2 Client Rate Limiting
- Additional client-side rate limit (5 searches/second)
- Debounced search input

### 5.3 Input Sanitization
- Control character removal
- Whitespace normalization
- Length limits enforced

---

## 6. API Security

### 6.1 Error Handling
- Generic error messages (no stack traces)
- Separate internal logging
- Never expose database errors

### 6.2 Request Validation
- Body size limit: 10KB
- Timeout: 30 seconds
- Method validation (GET, POST, OPTIONS, HEAD only)

### 6.3 Response Security
- Request ID tracking (`X-Request-ID`)
- No sensitive data in responses
- Consistent error format

---

## 7. Database Security

### 7.1 Query Security
- Parameterized queries via Drizzle ORM
- No raw SQL string concatenation
- Input sanitization before database operations

### 7.2 Connection Security
- Connection pooling with limits
- Environment-based configuration
- No credentials in code

---

## 8. Configuration Security

### 8.1 Next.js Configuration
- `poweredByHeader: false` (hides Next.js version)
- `reactStrictMode: true`
- `productionBrowserSourceMaps: false` (no source maps in production)

### 8.2 Environment Variables
- Database URL from environment only
- No hardcoded secrets
- Environment validation on startup

---

## 9. Logging & Monitoring

### 9.1 Security Event Logging
Logged events:
- Rate limit violations
- Blocked requests (path, user-agent)
- Suspicious patterns detected
- Error occurrences

### 9.2 PII Protection
- IP addresses sanitized in logs
- Search queries limited in storage
- No sensitive data logged

---

## 10. Defense in Depth Summary

```
┌──────────────────────────────────────────────────────────┐
│                    EDGE MIDDLEWARE                        │
│  • Path blocking • UA filtering • Header validation       │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                   SECURITY HEADERS                        │
│  • CSP • HSTS • X-Frame-Options • CORS policies          │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                    RATE LIMITING                          │
│  • Per-endpoint limits • IP fingerprinting • Blocking     │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                  INPUT VALIDATION                         │
│  • Zod schemas • SQL/XSS patterns • Length limits         │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                   API HANDLERS                            │
│  • Parameterized queries • Error handling • Sanitization  │
└─────────────────────────┬────────────────────────────────┘
                          │
┌─────────────────────────▼────────────────────────────────┐
│                    DATABASE                               │
│  • Drizzle ORM • Connection pooling • No raw SQL          │
└──────────────────────────────────────────────────────────┘
```

---

## Security Testing Verification

### Blocked Attacks
```bash
# SQL Injection - Blocked/Sanitized
curl "http://localhost:3000/api/search?q=SELECT%20*%20FROM%20users"
# Result: Empty results (query sanitized)

# Path Traversal - 403 Forbidden
curl "http://localhost:3000/.env"
# Result: 403 Forbidden

# WordPress Attack Path - 403 Forbidden
curl "http://localhost:3000/wp-admin"
# Result: 403 Forbidden

# Rate Limiting - 429 after limit
for i in {1..35}; do curl "http://localhost:3000/api/search?q=test"; done
# Result: 429 Too Many Requests after 30 requests
```

### Security Headers Present
```
Content-Security-Policy: default-src 'self' ...
X-Frame-Options: DENY
X-Content-Type-Options: nosniff
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
```

---

## Recommendations for Production

1. **WAF Integration**: Add cloud WAF (Cloudflare, AWS WAF) for additional protection
2. **Redis Rate Limiting**: Replace in-memory rate limiter with Redis for multi-instance support
3. **SIEM Integration**: Forward security logs to SIEM for monitoring
4. **Regular Audits**: Conduct periodic penetration testing
5. **Dependency Scanning**: Enable automated vulnerability scanning (Snyk, npm audit)
6. **Certificate Pinning**: Implement for mobile/desktop clients
7. **API Keys**: Add API key authentication for production use
