---
name: api-security-auditor
version: "1.0.0"
category: security
tags:
  - api-security
  - rest-api
  - graphql
  - owasp-api
  - authentication
  - authorization
  - rate-limiting
  - input-validation
  - injection
  - api-gateway
model: claude-sonnet-4-20250514
trigger_keywords:
  - API security
  - API audit
  - REST security
  - GraphQL security
  - API authentication
  - API authorization
  - rate limiting
  - API key management
  - OWASP API Top 10
  - API vulnerability
pricing: "$9.99 one-time"
---

# API Security Auditor

> **Comprehensive API security audit based on OWASP API Security Top 10 (2023).** Scans REST and GraphQL APIs for authentication flaws, authorization bypass, injection, excessive data exposure, rate limiting gaps, and misconfigured CORS — outputs a prioritized fix list with code examples.

## Why This Skill Exists

APIs are the #1 attack vector for web applications (Gartner, 2026). Traditional web security scanners miss API-specific vulnerabilities like BOLA (Broken Object Level Authorization), mass assignment, and excessive data exposure. This skill is purpose-built for API security.

## When to Activate

Activate when the user:
- Asks for API security audit or review
- Mentions OWASP API Top 10, BOLA, or API vulnerabilities
- Builds or reviews a REST or GraphQL API
- Says "is my API secure" or "check my endpoints"
- Needs to prepare for a penetration test or security audit

## Workflow

### Step 1: API Surface Mapping

Catalog all API endpoints:

| Method | Path | Auth Required | Description |
|--------|------|--------------|-------------|
| GET | /api/v1/users | ✅ | List users |
| GET | /api/v1/users/:id | ✅ | Get user by ID |
| POST | /api/v1/users | ❌ | Create user (signup) |
| PATCH | /api/v1/users/:id | ✅ | Update user |
| DELETE | /api/v1/users/:id | ✅ (admin) | Delete user |
| POST | /api/v1/auth/login | ❌ | Login |
| POST | /api/v1/auth/refresh | ✅ | Refresh token |
| GET | /api/v1/users/:id/orders | ✅ | Get user's orders |

Also check:
- GraphQL: schema, queries, mutations, subscriptions
- WebSocket endpoints
- File upload endpoints
- Webhook receivers

### Step 2: OWASP API Top 10 (2023) Audit

#### API1:2023 — Broken Object Level Authorization (BOLA)
The #1 API vulnerability. Test every endpoint that takes an object ID:

```javascript
// VULNERABLE: User can access other users' data
app.get('/api/users/:id', auth, (req, res) => {
  const user = db.getUser(req.params.id);  // No ownership check!
  res.json(user);
});

// SECURE: Verify ownership
app.get('/api/users/:id', auth, (req, res) => {
  if (req.user.id !== req.params.id && !req.user.isAdmin) {
    return res.status(403).json({ error: 'Forbidden' });
  }
  const user = db.getUser(req.params.id);
  res.json(user);
});
```

**Check every endpoint:**
- Can user A access user B's resource by changing the ID?
- Can user A modify user B's resource by changing the ID in the body?
- Can user A delete user B's resource?
- Are IDs sequential (enables enumeration)?

#### API2:2023 — Broken Authentication
| Check | Issue | Fix |
|-------|------|-----|
| Password reset token reusable | Token doesn't expire after use | One-time use + 15min expiry |
| JWT alg=none accepted | Server accepts unsigned tokens | Whitelist specific algorithms |
| No rate limit on login | Brute force possible | 5 attempts / 15 min / IP |
| Refresh token never expires | Token theft = permanent access | 7-day rotation + reuse detection |
| API key in URL | Logged in server logs/nginx | Move to `Authorization: Bearer` header |
| No email verification | Account takeover via signup | Verify before granting access |

#### API3:2023 — Broken Object Property Level Authorization
**Mass Assignment:**
```javascript
// VULNERABLE: User can set isAdmin
app.patch('/api/users/:id', auth, (req, res) => {
  db.updateUser(req.params.id, req.body);  // Accepts ALL fields!
});

// SECURE: Whitelist allowed fields
app.patch('/api/users/:id', auth, (req, res) => {
  const allowedFields = ['name', 'email', 'avatar'];
  const updates = pick(req.body, allowedFields);
  db.updateUser(req.params.id, updates);
});
```

**Excessive Data Exposure:**
```javascript
// VULNERABLE: Returns password hash, internal IDs, admin flags
app.get('/api/users/:id', auth, (req, res) => {
  const user = db.getUser(req.params.id);
  res.json(user);  // Everything!
});

// SECURE: Explicit field selection
app.get('/api/users/:id', auth, (req, res) => {
  const user = db.getUser(req.params.id, {
    select: ['id', 'name', 'email', 'avatar', 'createdAt']
  });
  res.json(user);
});
```

#### API4:2023 — Unrestricted Resource Consumption
| Check | Limit | Recommendation |
|-------|-------|---------------|
| Rate limiting | None | 100 req/min/user, 1000 req/min/IP |
| File upload size | Unlimited | 10MB max, validate MIME type |
| Pagination | None | Max 100 items per page |
| Query complexity (GraphQL) | Unlimited | Depth limit 10, complexity scoring |
| Compression bomb | Not checked | Max decompressed size check |
| Memory usage | Not tracked | Per-request memory limit |

#### API5:2023 — Broken Function Level Authorization
```javascript
// VULNERABLE: Admin endpoint check only on frontend
app.delete('/api/users/:id', auth, (req, res) => {
  db.deleteUser(req.params.id);  // No role check!
});

// SECURE: Verify role on backend
app.delete('/api/users/:id', auth, requireRole('admin'), (req, res) => {
  db.deleteUser(req.params.id);
});
```

#### API6:2023 — Unrestricted Access to Sensitive Business Flows
- Check: Can user abuse business logic? (e.g., unlimited coupon use, bypass purchase limits)
- Check: Are there race conditions in payment/transfer flows?
- Check: Can user skip steps in multi-step workflow?

#### API7:2023 — SSRF
- Check: Any endpoint that takes a URL and fetches it server-side
- Check: Webhook URLs, image proxy, PDF generation from URL
- Fix: URL allowlist, block private IPs (169.254.169.254, 10.x, 172.x, 192.168.x)

#### API8:2023 — Security Misconfiguration
- CORS: `Access-Control-Allow-Origin: *` with credentials
- HTTP methods: TRACE, PUT, DELETE enabled unnecessarily
- Error responses: stack traces, internal paths, SQL errors exposed
- Headers: missing X-Content-Type-Options, X-Frame-Options, CSP
- TLS: allows TLS 1.0/1.1, weak ciphers

#### API9:2023 — Improper Inventory Management
- Old API versions still accessible (`/api/v1/` alongside `/api/v2/`)
- Staging API accessible from internet
- Undocumented endpoints (not in OpenAPI spec)
- Deprecated endpoints still functional

#### API10:2023 — Unsafe Consumption of APIs
- Third-party API calls without TLS verification
- No timeout on third-party API calls
- Trusting third-party API responses without validation
- No circuit breaker for third-party API failures

### Step 3: Rate Limiting & DDoS Protection Audit

```markdown
## Rate Limiting Audit

| Endpoint | Current Limit | Recommended | Method |
|----------|--------------|-------------|--------|
| POST /auth/login | None | 5/15min/IP | Fixed window |
| POST /auth/signup | None | 3/hour/IP | Fixed window |
| GET /api/* | None | 100/min/user | Sliding window |
| POST /api/upload | None | 10/min/user | Token bucket |
| GraphQL /api/graphql | None | 30/min/user + depth limit | Complexity-based |

## Missing Protections
- ❌ No global rate limit middleware
- ❌ No per-user rate limit (only IP-based)
- ❌ No GraphQL query depth/complexity limiting
- ❌ No DDoS protection (Cloudflare/AWS Shield)
- ❌ No CAPTCHA on auth endpoints after failed attempts
```

### Step 4: Generate Security Report

```markdown
# 🔐 API Security Audit Report

## Executive Summary

| Severity | Count | Categories |
|----------|-------|------------|
| 🔴 Critical | 3 | BOLA, Broken Auth, Mass Assignment |
| 🟠 High | 5 | Rate Limiting, Excessive Data, CORS |
| 🟡 Medium | 4 | Error Handling, Headers, API Versioning |
| 🔵 Low | 2 | Documentation, Monitoring |

**Overall Risk: CRITICAL — Immediate action required**

## Prioritized Fix List

### 🔴 Fix Immediately (Today)
1. **BOLA on GET /api/users/:id** — Any user can read any other user's data
2. **Mass Assignment on PATCH /api/users/:id** — Users can set `isAdmin: true`
3. **No rate limit on POST /auth/login** — Brute force attack possible

### 🟠 Fix This Week
4. Add rate limiting middleware (express-rate-limit / slowapi)
5. Implement field selection on all user endpoints
6. Fix CORS: remove wildcard origin, use allowlist
7. Add GraphQL depth/complexity limiting
8. Disable old API version (v1)

[... full report with code examples for each fix ...]
```

## Output Constraints

- Every finding must include: endpoint, HTTP method, vulnerability description, OWASP API category, exploit scenario, and code fix
- Critical findings must include a curl command demonstrating the exploit
- All code fixes must be copy-paste ready
- Rate limiting recommendations must include specific numbers (not "add rate limiting")
- CORS findings must include the specific header values to set

## What This Skill Does NOT Do

- Does not send actual requests to the API (static analysis only)
- Does not test for business logic vulnerabilities specific to your domain
- Does not scan for infrastructure vulnerabilities (use cloud security scanner)
- Does not replace professional penetration testing for regulated industries
