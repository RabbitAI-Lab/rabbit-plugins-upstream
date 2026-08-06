# 🛡️ Sandbox Selfheal Guard

**Category:** agents, automation, security

## ✨ What This Skill Does
Anti-stuck / anti-snapshot-wipe guard for agentic sandboxes: self-healing runner, byte-verified GGUF manifest, native CPU rebuild, hard timeouts, binary fallback chain, prompt-cache integration, and light-swarm auto mode.

## 🔐 Permissions & Requirements
• Runs repair/heal scripts (selfheal_runner.sh)
• May modify workspace files it is configured to guard
• May rebuild local binaries (cmake/g++)

## 🔒 Security & Privacy
  - Runs shell repair commands that can modify files, credentials, dependencies, and workspace state.
  - Keep repair recipes narrowly scoped and idempotent; use --dry-run first.
  - Review manifest entries before install.
  - No data is sent off-box unless you configure an off-box sync.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `910799cb446f72b520b56f009b61f60935b63fec3e586c7dbead890b8f60bc3c`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
