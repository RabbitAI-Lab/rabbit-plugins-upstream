# 🔭 CyberScope

**Category:** research, security

## ✨ What This Skill Does

Packages **CyberScope**, a searchable reference catalog of 62 documented
cyber-operations, surveillance, and censorship methods across 10 categories, each linked to
authoritative public sources (MITRE ATT&CK, CISA, NIST, EFF, OWASP, SANS). The skill ships
the full, security-hardened Next.js + PostgreSQL search engine (schema, seed data, API
routes, security layers) so it can be run and studied for threat intelligence, research,
education, and defensive threat modeling. It is descriptive documentation only — no exploit
code, no payloads, no step-by-step offensive instructions.

## 🔐 Permissions & Requirements

- Runtime: Node.js ≥ 20, npm, and a local PostgreSQL database (connection string via
  `DATABASE_URL`).
- Network: the application makes **no outbound calls** — it serves a local web UI and reads
  a local database. The catalog's resource links are plain URLs opened by the user.
- Writes: the app creates its own PostgreSQL schema/tables and serves a local web server on
  localhost.
- No API keys, no secrets, no third-party services.

## 🔒 Security & Privacy

- What it reads/collects: only what you put in the local database (the bundled catalog) and
  the search queries you type.
- Does data leave the machine? No — everything runs locally; queries hit your own local
  API, and no telemetry is sent anywhere.
- No secrets are read, stored, or logged; `DATABASE_URL` is read from the environment only.
- Known risks: the catalog *describes* offensive and surveillance techniques. It is
  reference material and must not be used to conduct or facilitate attacks, surveillance,
  or disruption of systems you do not own.
- Mitigations: the app is defense-in-depth hardened (see `SECURITY.md`) — path/user-agent
  blocking, strict CSP, rate limiting, Zod validation, parameterized queries, DOMPurify
  output sanitization — and the skill's honest-use rules prohibit weaponization.
- Review before install: read `SKILL.md`, `SECURITY.md`, and `src/lib/seed-data.ts`.

## ✅ Verification Hash

Installers can verify this skill matches the published artifact by hashing the skill files
and comparing to the digests below:

- **SKILL.md SHA-256:** `ee440b84df93d05d5b9855d59ecedf194e94610af29a6595d899238a88eab27d`
- **src/lib/seed-data.ts SHA-256:** `8c4597e63d8d94c782fbf9cd46542096012cd721941239666b35ac967149dd3b`
- **SECURITY.md SHA-256:** `a255fd99c01eb38b24b2844d2306e233242f28b10c6dbccb1aca1527273e7812`

Verify locally:

```bash
sha256sum SKILL.md src/lib/seed-data.ts SECURITY.md
# compare the output to the SHA-256 values above.
```

---
*Published under the Skill Publishing Standard — see SKILL_PUBLISHING_STANDARD.md.*
