# ⚡ Arena Turn Accelerator

**Category:** agents, automation, development

## ✨ What This Skill Does
Reduces agent turn latency and improves response quality: prompt compactor, request-lifecycle fence (stale-answer invalidation), context-hygiene monitor, verification-triggers checklist, and an anti-sycophancy engine.

## 🔐 Permissions & Requirements
• May write small local state under ~/.arena_turn (prompt previews/cache)
• Self-test can delete ~/.arena_turn state (run only in an isolated profile)
• No network calls by default

## 🔒 Security & Privacy
  - May keep local state under ~/.arena_turn, including prompt previews.
  - State stays on-machine; nothing is transmitted.
  - Use the self-test only in an isolated profile or after backing up ~/.arena_turn.
  - Review scripts before use.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `7e466cfdcbb75253e722619f442f864811b0a50afc4d7ec1356db4d8e1d58356`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
