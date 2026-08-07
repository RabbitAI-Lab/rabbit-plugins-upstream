# 🔐 agentkey

**Categories:** security  
**Public tags:** #security, #credentials, #agent-identity, #key-management, #authentication

## ✨ Functionalities

Secure API key management and rotation for AI agents. Store, encrypt, rotate, and audit API keys used by your agents, with centralized management across multiple providers.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/agentkey
```

Initialize the local encrypted keystore, add provider credentials interactively, and use the documented list, rotate, test, and audit commands without printing secrets.

A representative command from the unchanged skill documentation is:

```bash
# Follow the invocation workflow reproduced below from SKILL.md
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Creates/stores an encrypted local keystore (chmod 600)
• Read/write to the keystore path (e.g. ~/.agentkey/)
• Calls provider APIs only when you rotate/test a key
• Requires you to provide the master passphrase

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Stores API keys encrypted at rest in a local keystore with restrictive permissions (600).
- Keys never leave the machine except when you explicitly rotate/test against a provider.
- The master passphrase is never stored — it is asked each time.
- Back up the keystore securely; losing the passphrase loses the keys.
- Review scripts before first use (they handle sensitive material).
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `16d3d7f5b233caa0cbdfa2d3409163581e75c6cea4dd303a09c9205ee4650a85`

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

# 🔑 AgentKey - Universal API Key Manager

## Description
🔐 Secure API key management and rotation for AI agents. Store, encrypt, rotate, and audit API keys used by your agents. Supports multiple providers with centralized key management.

## Data Privacy 🔒
🔒 <b>Complete Privacy:</b> All API keys are encrypted locally using AES-256. Your keys NEVER leave your machine. No key data is transmitted to ClawHub or any external server. You maintain full control and ownership of all credentials.

## Capabilities ⚡
✅ Secure key storage • ✅ Automatic rotation • ✅ Usage auditing • ✅ Multi-provider support • ✅ Encryption at rest • ✅ Access logging

## Usage
Follow the skill instructions to use this skill.

---

*README-only documentation remediation. No functional artifact file was changed.*
