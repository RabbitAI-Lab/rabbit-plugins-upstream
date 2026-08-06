# 🧠 Persistent Skill Memory

**Category:** agents, knowledge, productivity

## ✨ What This Skill Does
Stops an agent from forgetting the skills it has installed. Auto-generates a categorized capability index from every installed SKILL.md's frontmatter and injects it into the durable system prompt between stable markers, with hooks so installing/inventing/restoring a skill re-indexes automatically.

## 🔐 Permissions & Requirements
• Reads installed SKILL.md frontmatter
• Writes to the durable system-prompt file
• No network calls; no secrets

## 🔒 Security & Privacy
  - Reads skill metadata and updates a local prompt file.
  - Nothing is transmitted.
  - No secrets are involved.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `69fa84ec3dab7df6a8d1e3a49ed264ba2b4031c32daa664cb8d4d196b750e4a2`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
