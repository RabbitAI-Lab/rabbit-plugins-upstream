---
name: cyberscope
description: "CyberScope — a searchable reference catalog of 62 documented cyber-operations, surveillance, and censorship methods across 10 categories, each linked to public sources (MITRE ATT&CK, CISA, NIST, EFF, OWASP, SANS). Packaged as a security-hardened Next.js + PostgreSQL search engine for threat intelligence, research, education, and defensive threat modeling. Descriptive documentation only — no operational or exploit instructions."
version: 1.0.0
categories: [research, security]
topics: [cyber-threat-intelligence, surveillance, censorship, threat-modeling, reference]
metadata:
  openclaw:
    emoji: "🔭"
    requires:
      bins: ["node", "npm"]
      apis: ["PostgreSQL database (DATABASE_URL) — local only, no external services"]
    network:
      outbound: []
---

# 🔭 CyberScope — Cyber Operations Search Engine (Reference Skill)

**A searchable, source-linked catalog of documented cyber-operations, surveillance, and
censorship methods — for threat intelligence, research, education, and defensive modeling.**

CyberScope is a self-contained Next.js + PostgreSQL application that catalogs **62 methods
across 10 categories**. Every method is a short, neutral *description* of a technique that is
already publicly documented, and each is linked to authoritative public sources (MITRE
ATT&CK, CISA, NIST, EFF, OWASP, SANS, and more). This skill packages the app, its data, and
its documentation so it can be run and studied.

> ⚠️ **What this skill is — and is not.** It is a **reference catalog**: descriptions and
> citations of known techniques, of the same kind as MITRE ATT&CK or academic
> surveillance/censorship research. It contains **no exploit code, no payloads, no
> step-by-step offensive instructions**, and it must not be used to conduct or facilitate
> unauthorized access, surveillance, or disruption of systems you do not own. Use it for
> research, education, journalism, threat modeling, and defense only, and within the law.

## The catalog at a glance (10 categories, 62 methods)

| # | Category | Examples of documented methods |
|---|---|---|
| I | Mass Data Collection & Interception | bulk metadata collection, fiber-optic cable tapping, full-take storage |
| II | Targeted Hacking & Network Penetration | credential phishing, supply-chain compromise, social engineering |
| III | Living-Off-the-Land & Stealth | LotL techniques, fileless malware, false-front operations |
| IV | Hack-and-Leak Operations | data exfiltration & release, timed strategic leaks |
| V | Denial-of-Service & Disruption | DDoS, wiper malware, website defacement |
| VI | Internet Censorship & Content Control | DPI, DNS poisoning, TLS reset injection, protocol whitelisting |
| VII | Internet Shutdowns & Access Manipulation | BGP manipulation, full shutdowns, national intranets |
| VIII | Domestic Surveillance & Legal Frameworks | data retention, lawful interception (SORM-type), camera networks |
| IX | Defensive Cyber Methods & Frameworks | MITRE ATT&CK-based testing, KEV catalog, segmentation |
| X | Intelligence Sharing & Coordination Methods | coordinated vulnerability disclosure, threat sharing |

Each method record carries: `title`, a one-line `description`, `keywords`, and one or more
curated `resources` (public URL + source + type) such as MITRE ATT&CK technique pages,
NIST publications, EFF analyses, and OWASP projects.

## How to run it

Prerequisites: Node.js ≥ 20, npm, and a local PostgreSQL instance.

```bash
npm install
# point drizzle at your database (drizzle.config.json) and set the env var:
export DATABASE_URL="postgresql://user:pass@127.0.0.1:5432/app_db"
npx drizzle-kit push                 # create the schema
npm run dev                          # start at http://localhost:3000
curl -X POST http://localhost:3000/api/seed   # load the 62 methods (idempotent)
```

API endpoints: `/api/search?q=…`, `/api/categories`, `/api/methods`, `/api/stats`,
`/api/health`, `/api/seed`.

## Built-in security hardening (documented in `SECURITY.md`)

- **Edge middleware**: path-based blocking (`.env`, `.git/`, `.sql`, …), user-agent
  filtering of attack tools, header-injection protection, URL/null-byte/double-encoding checks.
- **Security headers**: strict CSP, HSTS, `X-Frame-Options: DENY`, COOP/CORP/COEP, `nosniff`.
- **Rate limiting**: per-endpoint sliding-window limits with 5-minute blocks.
- **Input validation**: Zod schemas, SQL-injection/XSS/path-traversal pattern blocking,
  length limits; parameterized queries via Drizzle ORM (no raw SQL).
- **Output sanitization**: DOMPurify for any rendered HTML, `rel="noopener noreferrer"`,
  protocol allow-listing (`https://` only).

## Honest-use rules

1. **Reference only** — this catalog documents what exists; it is not a guide for doing it.
2. **Lawful use** — you may only use it for research, education, journalism, threat modeling,
   and defense, and only on systems/contexts you are authorized to study.
3. **No weaponization** — do not derive or add executable attack steps from these entries.
4. **Cite, don't amplify** — when writing from this catalog, link the public sources.

## Files

- `src/lib/seed-data.ts` — the 10 categories + 62 methods + curated resources
- `src/db/schema.ts` — PostgreSQL schema (categories, methods, resources)
- `src/app/api/*` — search/categories/methods/stats/seed/health endpoints
- `src/lib/security/*`, `src/middleware.ts` — security layers
- `SECURITY.md` — full defense-in-depth documentation
- `README.md` — permissions, security & privacy, verification hashes
