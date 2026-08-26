# 🔍 Agent Bom Scan

**Categories:** security  
**Public tags:** #security, #sbom, #dependency-scanning, #compliance, #agents

## ✨ Functionalities

Deep vulnerability scanning for software bill of materials. Detects CVEs, analyzes dependency trees, assesses supply-chain risk, and generates detailed security reports for your projects.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/agent-bom-scan
```

Point the scanner at a project or SBOM you are authorized to assess, run the documented scan command, and review CVE matches and false positives.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read access to the project/dependency files being scanned
• Runs local scanners (python3, and optionally installed CLI scanners like osv-scanner/trivy if present)
• Network access to query CVE / OSV databases

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Reads dependency manifests and may query public CVE/OSV databases over the network.
- Only sends dependency hashes/names to public vuln APIs — no source code or secrets.
- No credentials are stored or sent.
- Scan results may contain sensitive dependency details; store reports securely.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `8919748a266a1fecca1b975a5724291e17aa9522caa4f35f76f100e0437af1b8`

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

# 🔍 Agent BOM Vulnerability Scanner

## Description
🔍 Deep vulnerability scanning for software bill of materials. Detect CVEs, analyze dependencies, assess supply chain risks, and generate detailed security reports.

## Data Privacy 🔒
🔒 <b>Complete Privacy:</b> All vulnerability scans execute locally on your machine. Your codebase and dependencies are analyzed offline. No source code or dependency data is sent to external servers. Scan results remain in your control.

## Capabilities ⚡
✅ CVE detection • ✅ Dependency analysis • ✅ Supply chain security • ✅ Risk assessment • ✅ Report generation • ✅ Offline scanning

## Usage
Follow the skill instructions to use this skill.

---

*README-only documentation remediation. No functional artifact file was changed.*
