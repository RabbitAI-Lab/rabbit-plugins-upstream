# 🎛️ Free Tier Ai Router

**Category:** automation, agents, development

## ✨ What This Skill Does
Quota-aware LLM router that squeezes maximum usable AI out of free-tier API keys across Gemini, Mistral, OpenRouter, Kilo and Cerebras. Probes model availability/quality, applies published rate limits, and routes requests to the cheapest capable model while preserving scarce daily quota.

## 🔐 Permissions & Requirements
• Reads API keys from ~/.config/<provider>/credentials.json and the router keystore
• Sends prompts and system text to the selected third-party providers
• Writes persistent cache/cooldown/state under your home directory (e.g. ~/.cache/ai_router/)

## 🔒 Security & Privacy
  - Handles live provider API keys — keep the keystore permissions 600.
  - Prompts and system text you send are forwarded to selected third-party AI providers.
  - Persistent cache/cooldown/state is written under your home directory.
  - Use --no-cache for sensitive work and clear local state when trust boundaries change.
  - Review get-ai-router.sh and setup scripts before use, especially on shared systems.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `4959c58cb96f0f1f4348611a34f8cbf75132c74964fc8963e9459a61094c26d1`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
