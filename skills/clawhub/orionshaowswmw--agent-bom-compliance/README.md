# 🏛️ Agent BOM Compliance

**Categories:** security  
**Public tags:** #security, #compliance, #owasp, #nist, #audit

## ✨ Functionalities

Comprehensive compliance engine for AI agents. Evaluates agent systems and their software supply chains against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, and AISVS. Automatically generates Software Bill of Materials (SBOM) and compliance reports.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/agent-bom-compliance
```

Run the compliance/SBOM workflow against a project you own, select the desired framework, and review the generated compliance report before relying on it.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read/write access to the project directory being audited
• Ability to run local analysis scripts (python3)
• Network access if SBOM enrichment or report templates are fetched
• No external API keys required by default

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Reads project files and dependency manifests to build SBOMs and assess compliance.
- Data stays local by default; only network calls are made if you explicitly enable remote template/enrichment.
- No secrets are stored or transmitted.
- Review generated reports for accuracy before acting on them.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `d8c8cd9f5aa805cc3fb6c11296a619228c37196f2cdfc3d156d683b232950f8b`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.


## 📚 Complete Skill Reference (Unchanged)

The text below is copied from the installed `SKILL.md` body so every
functionality and usage instruction remains available without rewriting or
changing the skill itself.

---

# 🛡️ Agent BOM Compliance Engine

## Description
🏛️ Comprehensive compliance engine for AI agents. Evaluate against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS, and more. Generate SBOMs and compliance reports automatically.

## Data Privacy 🔒
🔒 <b>Complete Privacy:</b> All compliance scans run locally. Your code, configurations, and system data are analyzed on-device. No sensitive information is transmitted. Reports are generated locally and stored only in your workspace.

## Capabilities ⚡
✅ Multi-framework compliance • ✅ SBOM generation • ✅ Policy enforcement • ✅ Report generation • ✅ Audit trail • ✅ Offline analysis

## Usage
Follow the skill instructions to use this skill.

---

*README-only documentation remediation. No functional artifact file was changed.*
