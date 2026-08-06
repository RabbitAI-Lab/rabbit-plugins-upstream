# 🔍 Agent Bom Scan

**Category:** security

## ✨ What This Skill Does
Deep vulnerability scanning for software bill of materials. Detects CVEs, analyzes dependency trees, assesses supply-chain risk, and generates detailed security reports for your projects.

## 🔐 Permissions & Requirements
• Read access to the project/dependency files being scanned
• Runs local scanners (python3, and optionally installed CLI scanners like osv-scanner/trivy if present)
• Network access to query CVE / OSV databases

## 🔒 Security & Privacy
  - Reads dependency manifests and may query public CVE/OSV databases over the network.
  - Only sends dependency hashes/names to public vuln APIs — no source code or secrets.
  - No credentials are stored or sent.
  - Scan results may contain sensitive dependency details; store reports securely.

## ✅ Verification Hash
Installers can verify this skill matches the published artifact by hashing the
skill files and comparing to the digest below:

- **SHA-256:** `a3247d998c39a963fd1ea720d1d0e8f4edd9921202a79b9e76b7cf9e61c7be93`

Verify locally:

```bash
sha256sum SKILL.md README.md
# compare the output to the SHA-256 above.
```

---
*Generated under the Skill Publishing Standard. See SKILL_PUBLISHING_STANDARD.md.*
