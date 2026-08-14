# 🎓 ai-era-career-planner

**Categories:** productivity, research, knowledge  
**Public tags:** #productivity, #career-planning, #ai, #skills, #research

## ✨ Functionalities

Career planning for the AI era. Analyzes your skills, identifies opportunities, plans development paths, and helps you navigate career transitions with structured guidance.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/ai-era-career-planner
```

Provide your current skills, goals, constraints, and optional resume text; follow the planning workflow to produce and review a staged career-development plan.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Optional: access to your resume/skills text (only what you provide)
• Network access if an optional LLM provider is configured
• No system-level permissions

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Processes only the personal data you choose to input (resume, skills, goals).
- No data is sent anywhere unless you configure an LLM provider and explicitly request analysis.
- No secrets or system files are read.
- Career output is informational guidance, not guaranteed outcomes.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `d5396e99837a1063ceec5bfc1c53e25919372dc3fd50d8fe903804c866f8609b`

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

# 🎓 AI Era Career Planner

## Description
🎓 Comprehensive career planning for the AI era. Analyze skills, identify opportunities, plan development paths, and navigate career transitions with AI-powered guidance.

## Data Privacy 🔒
🎓 <b>Complete Privacy:</b> Your career data, skills assessment, and professional information stay completely private. All analysis happens locally. Your personal information is never shared, sold, or used for training.

## Capabilities ⚡
✅ Skills assessment • ✅ Career path planning • ✅ Opportunity identification • ✅ Learning recommendations • ✅ Transition guidance

## Usage
Follow the skill instructions to use this skill.

---

*README-only documentation remediation. No functional artifact file was changed.*
