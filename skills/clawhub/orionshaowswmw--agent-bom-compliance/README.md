# 🏛️ Agent Bom Compliance

**Category:** security

## ✨ What This Skill Does
Comprehensive compliance engine for AI agents. Evaluates agent systems and their software supply chains against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, and AISVS. Automatically generates Software Bill of Materials (SBOM) and compliance reports.

## 🔐 Permissions & Requirements
• Read/write access to the project directory being audited
• Ability to run local analysis scripts (python3)
• Network access if SBOM enrichment or report templates are fetched
• No external API keys required by default

## 🔒 Security & Privacy
  - Reads project files and dependency manifests to build SBOMs and assess compliance.
  - Data stays local by default; only network calls are made if you explicitly enable remote template/enrichment.
  - No secrets are stored or transmitted.
  - Review generated reports for accuracy before acting on them.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `c387be7716477d268a991c1446feb186e792a0aed7b8e029d4fa5f2d6f9560cf`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
