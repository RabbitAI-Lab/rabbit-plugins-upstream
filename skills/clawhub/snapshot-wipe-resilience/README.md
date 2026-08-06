# 🧬 Snapshot Wipe Resilience

**Category:** productivity

## ✨ What This Skill Does
Detects and auto-repairs partially-wiped agent workspaces, with hybrid post-quantum end-to-end encryption (X25519+ML-KEM-1024, ML-DSA-87) for any data sent off-box, and syncs the recovery manifest off-box so it survives a total wipe.

## 🔐 Permissions & Requirements
• Read/write access to the workspace it protects
• May run restore recipes (shell commands) that modify files/credentials/dependencies
• Optional off-box manifest sync (encrypted)

## 🔒 Security & Privacy
  - Restore recipes are shell commands that can modify files, credentials, dependencies, and workspace state — review manifest entries, sign manifests yourself, and use --dry-run first.
  - Off-box sync can expose restore commands/credential placeholders/payload metadata; keep redaction enabled and treat recovery manifests as sensitive.
  - Uses post-quantum encryption (X25519+ML-KEM-1024, ML-DSA-87) for off-box data.
  - Do not run restore recipes from untrusted manifests unless signatures/fingerprints verify.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `55fa8432d187e031268dddfd4f3fd8f980aab3f348ce5c2c59763a7b29e8ce2f`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
