---
name: owasp-security-code-review
version: "1.0.0"
category: security
tags:
  - security
  - code-review
  - owasp
  - vulnerability
  - audit
  - static-analysis
model: claude-sonnet-4-20250514
trigger_keywords:
  - security review
  - code audit
  - vulnerability scan
  - OWASP
  - security check
  - penetration test
  - secure code
  - dependency scan
  - SQL injection
  - XSS
  - CSRF
  - authentication flaw
  - authorization bypass
  - insecure deserialization
  - security hardening
pricing: "$9.99 one-time"
---

# OWASP Security Code Review Auditor

> **Automated, severity-rated security review based on OWASP Top 10 (2025).** Scans your codebase for vulnerabilities, misconfigurations, and insecure patterns — outputs a structured report grouped by file with critical/warning/suggestion severity ratings.

## Why This Skill Exists

Most AI code reviews flag generic "best practices" without catching real vulnerabilities. This skill encodes the OWASP Top 10 (2025), CWE mappings, and industry-specific compliance frameworks (PCI-DSS, HIPAA, SOC2) into a structured audit that produces immediately actionable findings — not vague suggestions.

## When to Activate

Activate when the user:
- Asks for a security review, security audit, or vulnerability scan
- Says "check this code for vulnerabilities" or "is this secure?"
- Mentions OWASP, CWE, CVE, or compliance frameworks (PCI-DSS, HIPAA, SOC2)
- Commits authentication, authorization, crypto, or data-handling code
- Requests a penetration test or red team review

## Prerequisites

- Access to the codebase via file system or git
- Language detection (Python, JavaScript/TypeScript, Go, Java, Rust, PHP, Ruby)

## Workflow

### Step 1: Reconnaissance — Map the Attack Surface

Scan the codebase structure and identify:
- **Entry points**: API routes, web handlers, GraphQL resolvers, WebSocket endpoints
- **Auth boundaries**: middleware, decorators, interceptors, guards
- **Data flows**: user input → database, user input → shell, user input → template
- **External dependencies**: package.json, requirements.txt, go.mod, Cargo.toml, pom.xml
- **Secrets**: hardcoded API keys, tokens, passwords, private keys
- **Config files**: .env, docker-compose, nginx.conf, CORS policies

Output: Attack surface map (markdown table)

### Step 2: OWASP Top 10 (2025) Systematic Audit

For each category below, scan every relevant file and flag findings:

#### A01: Broken Access Control
- Check: IDOR (Insecure Direct Object Reference) patterns
- Check: missing authorization checks on sensitive routes
- Check: role escalation possibilities (user → admin bypass)
- Check: JWT/token validation completeness (alg=none, expired, forged)
- Check: CORS misconfiguration (wildcard origins with credentials)
- Pattern: `req.params.id` used without ownership verification

#### A02: Cryptographic Failures
- Check: hardcoded secrets/keys in source code
- Check: weak hashing (MD5, SHA1 for passwords)
- Check: insecure random number generators (Math.random for tokens)
- Check: SSL/TLS verification disabled (`rejectUnauthorized: false`)
- Check: sensitive data in URL parameters
- Check: plaintext storage of passwords, tokens, PII

#### A03: Injection
- Check: raw SQL queries with string concatenation
- Check: unparameterized ORM queries
- Check: shell command execution with user input (`exec`, `system`, `subprocess`)
- Check: template injection (Jinja2, ERB, Thymeleaf with user input)
- Check: LDAP/XPath/NoSQL injection vectors
- Pattern: `query("SELECT * FROM users WHERE id = " + req.params.id)`

#### A04: Insecure Design
- Check: missing rate limiting on auth endpoints
- Check: no account lockout after failed logins
- Check: password reset flow predictability
- Check: missing input validation on business logic
- Check: missing CSRF tokens on state-changing operations

#### A05: Security Misconfiguration
- Check: debug mode enabled in production config
- Check: default credentials still present
- Check: unnecessary HTTP methods enabled (PUT, DELETE, TRACE)
- Check: missing security headers (X-Frame-Options, CSP, HSTS, X-Content-Type-Options)
- Check: verbose error messages exposing stack traces

#### A06: Vulnerable & Outdated Components
- Scan: all dependencies against known CVE databases
- Flag: packages with known critical vulnerabilities
- Flag: packages not updated in 12+ months
- Check: lockfile consistency (package-lock.json vs package.json)

#### A07: Authentication Failures
- Check: weak password policies (no length/complexity requirements)
- Check: session management (session fixation, no rotation on login)
- Check: missing MFA on sensitive operations
- Check: predictable token generation
- Check: credential stuffing protection (no CAPTCHA, no rate limit)

#### A08: Software & Data Integrity Failures
- Check: unsigned updates/downloads
- Check: insecure deserialization (pickle, YAML.load, eval)
- Check: missing integrity checks on CI/CD pipeline
- Check: untrusted CDNs for critical resources

#### A09: Security Logging & Monitoring Failures
- Check: missing audit logs for sensitive actions
- Check: logs containing sensitive data (passwords, tokens)
- Check: no alerting on suspicious activity (brute force, privilege escalation)

#### A10: Server-Side Request Forgery (SSRF)
- Check: server-side HTTP requests with user-controlled URLs
- Check: missing URL allowlist for outbound requests
- Check: metadata endpoint access (169.254.169.254 on AWS/GCP)
- Check: DNS rebinding possibilities

### Step 3: Dependency Vulnerability Scan

For each dependency file found:
- Parse all dependencies and versions
- Cross-reference against:
  - GitHub Advisory Database (GHSA)
  - npm audit / pip-audit / cargo audit / go vuln database
- Flag: critical (CVSS ≥ 9.0), high (7.0-8.9), moderate (4.0-6.9)
- Provide: specific version to upgrade to, or patch instructions

### Step 4: Secret Detection

Scan all files for:
- API keys: AWS (`AKIA*`), Google (`AIza*`), Stripe (`sk_live_*`), GitHub (`ghp_*`)
- Private keys: `-----BEGIN RSA PRIVATE KEY-----`, `-----BEGIN OPENSSH PRIVATE KEY-----`
- Database connection strings with credentials
- JWT secrets
- Generic high-entropy strings (entropy ≥ 4.5)
- `.env` files committed to git

### Step 5: Generate Report

Produce a structured report in this exact format:

```markdown
# 🔒 Security Audit Report

**Project**: [project name]
**Date**: [date]
**Auditor**: OWASP Security Code Review Auditor v1.0
**Files scanned**: [N]
**Languages**: [languages detected]

---

## Executive Summary

| Severity | Count |
|----------|-------|
| 🔴 Critical | N |
| 🟠 High | N |
| 🟡 Warning | N |
| 🔵 Suggestion | N |

**Overall Risk Level**: [Critical / High / Medium / Low]

---

## Findings

### 🔴 Critical

#### [C-01] SQL Injection in `src/api/users.js:42`
- **OWASP**: A03: Injection
- **CWE**: CWE-89
- **Description**: User-supplied `req.params.id` is concatenated directly into SQL query
- **Vulnerable code**:
  ```js
  const query = "SELECT * FROM users WHERE id = " + req.params.id;
  ```
- **Impact**: Full database compromise, data exfiltration, authentication bypass
- **Remediation**:
  ```js
  const query = "SELECT * FROM users WHERE id = ?";
  db.execute(query, [req.params.id]);
  ```
- **References**: [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

### 🟠 High
#### [H-01] ...

### 🟡 Warning
#### [W-01] ...

### 🔵 Suggestion
#### [S-01] ...

---

## Dependency Vulnerabilities

| Package | Version | Severity | CVE | Fix Version |
|---------|---------|----------|-----|-------------|
| lodash | 4.17.15 | Critical | CVE-2021-23337 | 4.17.21 |

---

## Secrets Detected

| File | Type | Status |
|------|------|--------|
| .env | AWS Access Key | 🔴 Must remove from git history |

---

## Compliance Mapping

| Framework | Status | Gaps |
|-----------|--------|------|
| PCI-DSS | ❌ Non-compliant | [list gaps] |
| HIPAA | ⚠️ Partial | [list gaps] |
| SOC2 | ⚠️ Partial | [list gaps] |

---

## Remediation Priority

1. **Immediate** (fix today): [list critical findings]
2. **This week** (fix within 7 days): [list high findings]
3. **This sprint** (fix within 14 days): [list warnings]
4. **Backlog** (plan for next quarter): [list suggestions]
```

## Output Constraints

- Every finding MUST include: severity, file:line, OWASP category, CWE ID, vulnerable code snippet, remediation code, and reference link
- Critical findings MUST include exploit scenario description
- No vague suggestions like "improve security" — every finding must be specific and actionable
- If no vulnerabilities found in a category, state "✅ No issues found in A0X: [category name]"
- Sort findings by severity (Critical → High → Warning → Suggestion)

## What This Skill Does NOT Do

- Does not run dynamic analysis or penetration testing
- Does not replace a professional security audit for regulated industries
- Does not scan compiled binaries or Docker images
- Does not check infrastructure/cloud configuration (use cloud security scanner)
