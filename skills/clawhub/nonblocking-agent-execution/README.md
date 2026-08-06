# ⏳ Nonblocking Agent Execution

**Category:** agents, automation, operations

## ✨ What This Skill Does
Prevents 'agent stopped responding / stuck / no output' failures in sandboxed agent runtimes (Arena Agent Mode, OpenClaw, Codex) by providing a detach → bounded-poll → durable-state pattern plus a ready-to-use jobctl.sh runner.

## 🔐 Permissions & Requirements
• Runs and supervises subprocesses
• Writes durable job state files
• May use background/daemon execution

## 🔒 Security & Privacy
  - Supervises the processes you ask it to run.
  - Job state is written to local disk.
  - No secrets are collected beyond what the supervised command uses.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `e8ba94516a5cddca6acbb3dd71f9074143ec4dc9ba1dfb5e9f454749ad502069`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
