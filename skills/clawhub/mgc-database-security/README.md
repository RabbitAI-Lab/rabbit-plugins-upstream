# Database Credential Security (Zero‑Exposure Edition)

Secure database credential management using MGC Blackbox. Supports MySQL, PostgreSQL, SQLite, MariaDB and more.

## What This Skill Does

This skill provides a pattern for managing database credentials securely:
- Store credentials encrypted in MGC Blackbox
- Retrieve at runtime without AI seeing plaintext
- Execute database operations safely
- Support multi‑node collaboration via script sealing

## What’s New in v1.1.0

- **Complete Examples**: MySQL, PostgreSQL, SQL Server credential storage
- **Troubleshooting**: Common errors and solutions
- **FAQ Section**: Database‑specific common questions
- **Anti‑Patterns**: Common mistakes and correct practices
- **When to Use**: Clear guidance on use cases
- **Capability Boundary**: What this skill does and does not do
- **Advanced Scenarios**: Multi‑database, credential rotation, version management

---

## Prerequisites

- Python 3.10+
- pip install mgc-blackbox
- MGC service running
- Database driver (mysql‑connector‑python, psycopg2, etc.)

---

## Quick Start

### 1. Install MGC

```
pip install mgc-blackbox
mgc
```

### 2. Store Database Credentials

Use `mgc_save` to store credentials:

```
Tool: mgc_save
Parameters:
  info_type:   "config"
  info_owner:  "my_mysql_prod"
  content:     "{json_content}"
```

See SKILL.md for complete examples for MySQL, PostgreSQL, SQL Server.

### 3. Use in Your Script

Your local script retrieves credentials from MGC, connects to database, and executes queries - all without exposing credentials to AI.

---

## When to Use This Skill

**Use when:**
- Production environments with sensitive data
- Automation tasks requiring database access
- Multi‑node collaboration (use mgc_seal)
- AI needs database access but must not see passwords

**Not needed when:**
- Public databases with no authentication
- Local development with mock data
- Interactive manual database access

---

## What's Inside

- Complete credential storage workflow examples
- Troubleshooting guide
- FAQ section
- Anti‑patterns with correct practices
- Database credential patterns
- Security best practices
- SKILL.md and local script templates

---

## MCP Tools

- `mgc_save`: Store credentials
- `mgc_get`: Retrieve credentials
- `mgc_list`: List stored credentials
- `mgc_seal`: Encrypt scripts for multi‑node execution

---

## Security

- Credentials never exposed to AI
- Encrypted storage via MGC
- Runtime credential retrieval only
- No plaintext in logs
- Separate credentials per environment

---

## License

MIT
