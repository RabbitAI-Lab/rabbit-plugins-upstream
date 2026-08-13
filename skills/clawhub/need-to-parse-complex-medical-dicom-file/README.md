# 🩻 Need To Parse Complex Medical Dicom File

**Categories:** knowledge, operations, research  
**Public tags:** #knowledge, #dicom, #medical-imaging, #parsing, #research

## ✨ Functionalities

Detects and autonomously parses complex medical DICOM files using structured fallback and verification to overcome standard tool limitations.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/need-to-parse-complex-medical-dicom-file
```

Provide a DICOM file you are authorized to process, execute the detection–mitigation–verification workflow, and validate output with qualified medical tooling; do not use it for diagnosis.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Read access to DICOM files you provide
• Requires python3 + DICOM parsing libraries (e.g. pydicom)
• May require network if dependencies are installed on demand

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Processes medical imaging data you provide — handle PHI responsibly.
- Data stays local by default.
- No secrets are involved.
- Do not use for diagnosis; verify outputs with a qualified professional.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `9d854bef3c7e5090ba24b0edf1aefc850e91da901f73dde931054751f7eb92cd`

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

# need-to-parse-complex-medical-dicom-file — Agent Innovation Skill

## Problem & Limited Capability
- **Target Weakness:** Need to parse complex medical DICOM files
- **Boundary:** Standard tools or existing skills were insufficient to handle this requirement autonomously.

## Innovative Solution Architecture
1. **Detection:** Identify when `Need to parse complex medical DICOM files` occurs in the workflow.
2. **Mitigation:** Apply structured fallback and self-discover reasoning to resolve the constraint without hallucination.
3. **Verification:** Enforce falsifiable checks to confirm the innovation succeeds.

---

*README-only documentation remediation. No functional artifact file was changed.*
