---
name: agent-audit
description: Audit all agent ADC accounts, passwords, roles, and workspace configurations. Use when checking for default passwords, verifying agent role assignments, detecting configuration drift, or generating agent health reports. Triggers on "audit agents", "check passwords", "agent health check", "角色检查", "账号检查".
---

# Agent Audit

Run `scripts/audit.sh` from the workspace root to execute all checks.

## What It Checks

1. **ADC Login** — Tests each agent's email/password against ADC API
2. **Default Passwords** — Detects `agent2026` or known weak passwords
3. **Role Mismatch** — Compares ADC role vs expected role from openclaw.json
4. **Workspace Completeness** — Checks for SOUL.md, AGENTS.md, etc.
5. **SOUL.md Template** — Detects agents still using default "You're not a chatbot" template

## Usage

```bash
# Full audit (login + roles + souls)
bash skills/agent-audit/scripts/audit.sh --all

# Role audit only (compare DB against manifest)
bash skills/agent-audit/scripts/role-audit.sh
```

## Role Manifest

`references/role-manifest.json` contains the expected `role` and `internal_role` for every agent.
Run `role-audit.sh` to detect mismatches between DB and manifest.

To fix a mismatch: edit the manifest, then update DB via:
```bash
SQL_B64=$(python3 -c "import base64; print(base64.b64encode(b\"UPDATE users SET role='xxx' WHERE email='xxx';\"))")
ssh root@8.163.44.127 "echo '$SQL_B64' | base64 -d | docker run --rm -i -e PGPASSWORD=... postgres:16-alpine psql -h 172.21.0.2 -U postgres -d agent_dev_center"
```
