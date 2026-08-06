# 🔁 Idempotent Rebuild Verification

**Category:** development, operations, security

## ✨ What This Skill Does
Verifies that hash-pinned workspace rebuild scripts survive sandbox snapshot wipes, and detects self-mutating config files whose checksum drifts because a later step rewrites an earlier step's output.

## 🔐 Permissions & Requirements
• Read access to workspace build scripts and config files
• Runs hashing/verification (sha256sum)
• No network calls by default

## 🔒 Security & Privacy
  - Reads scripts and config files to verify checksums — does not modify them.
  - No data leaves the machine.
  - No secrets are handled.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `660282b024b16f439dae040271adcc8a1ee1df3c002b82a8fe3fa976fc964ae9`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
