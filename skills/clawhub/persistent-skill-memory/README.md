# 🧠 persistent-skill-memory

**Categories:** agents, knowledge, productivity  
**Public tags:** #agents, #skill-memory, #persistence, #knowledge, #automation

## ✨ Functionalities

Stops an agent from forgetting the skills it has installed. Auto-generates a categorized capability index from every installed SKILL.md's frontmatter and injects it into the durable system prompt between stable markers, with hooks so installing/inventing/restoring a skill re-indexes automatically.

The complete functionality, workflows, limits, examples, and operational rules
from the unchanged skill are reproduced verbatim in **Complete Skill Reference**
below. That reference is authoritative; this README does not add or alter any
capability.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/persistent-skill-memory
```

Run the indexer after installing or changing skills, inspect the generated capability index, and update only the bounded durable-prompt markers.

A representative command from the unchanged skill documentation is:

```bash
./skill_add.sh @owner/new-skill
python3 manage_system_prompt.py show | grep -q "@owner/new-skill" && echo REMEMBERED
```

Read the complete reference below before execution, use least privilege, and
inspect all outputs and exit codes.

## 🔐 Permissions & Requirements

• Reads installed SKILL.md frontmatter
• Writes to the durable system-prompt file
• No network calls; no secrets

All permissions above are capability requirements, not blanket authorization.
Grant only what the selected workflow needs, scope filesystem access to the
working directory, and do not elevate privileges unless SKILL.md explicitly
requires and explains it.

## 🔒 Security & Privacy

- Reads skill metadata and updates a local prompt file.
- Nothing is transmitted.
- No secrets are involved.
- **Data handling:** the skill reads only user-selected inputs and files described above; it must not collect unrelated data.
- **Storage/logging:** inspect output and log locations before use. Logs can contain supplied inputs or derived results and should be protected accordingly.
- **Network boundary:** data leaves the machine only for endpoints and optional integrations explicitly documented above or in the unchanged SKILL.md; otherwise processing remains local.
- **Secrets:** API keys, tokens, passwords, and credentials must never be embedded in the skill or logged. Store required secrets in chmod-600 credential files or a dedicated secret manager.
- **Risks and mitigation:** review SKILL.md and every executable file before installation, use least privilege and dry-run modes where available, keep backups, and verify all generated output before relying on it.

## ✅ Verification Hash

This digest verifies every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `133f83db69f06f3049c2445f2e16a5103ce013ab783eb8d74660b17b233c5dc8`

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

# Persistent Skill Memory

Field-authored in Arena Agent Mode (2026-07) managing a 180-skill workspace.

## The problem

Installing skills to disk does **not** make an agent aware of them. Filesystem presence is
not memory: the agent must re-discover them every session, and after a context reset or a
snapshot wipe it behaves as if the skills were never installed. Symptoms:

- Solving from scratch a problem an installed skill already covers.
- Skill count grows, but effective capability doesn't.
- "What can you do?" gets a vague answer that ignores 170 installed skills.

## The fix: index → inject → auto-refresh

**1. Index.** Walk every `SKILL.md`, parse YAML frontmatter `name` + `description`
(handling `>` and `|` block scalars), fall back to the first `#` heading, dedupe by
`(owner, slug)` since one skill can land under multiple paths.

**2. Categorize.** Keyword-bucket into ~10 domains so lookup is by *need*, not by memorized
name. A flat 180-item list is unusable; grouped, it's scannable.

**3. Compress.** Full descriptions blow the prompt budget. The durable prompt gets
**names only, grouped by category** (~4.4 KB for 180 skills); full descriptions live in
`SKILLS_INDEX.md`, loaded on demand. Names are enough to trigger recall — the skill's own
SKILL.md is read before deep use.

**4. Inject between stable markers** so regeneration is idempotent and never duplicates:

```
<<<SKILL_INDEX_BEGIN>>>
[Anti-stall / async] durable-task-runner, polling-best-practices, ...
[Agents / orchestration] agent-team-orchestration, ...
<<<SKILL_INDEX_END>>>
```

Base standing directives live **above** the markers and are rewritten verbatim each time,
so behavioral rules and the capability list can never drift apart.

**5. Auto-refresh via hooks** — the part people skip, and why indexes go stale:

| Event | Hook |
|---|---|
| Installing a skill | `skill_add.sh` wrapper: install, then re-index |
| Publishing an invention | tail of `publish_inventions.sh` |
| Restoring after a wipe | tail of `restore_volatile.sh` |

Manual indexing rots within days. Hooked indexing stays true.

## Verification that actually proves it

Don't trust "the file was written". Install a new skill through the wrapper, then grep the
**live** prompt for its name:

```bash
./skill_add.sh @owner/new-skill
python3 manage_system_prompt.py show | grep -q "@owner/new-skill" && echo REMEMBERED
```

## Design rules

1. Names in the prompt, descriptions on disk — respect the budget.
2. Group by problem domain, never alphabetically only.
3. Markers, not appends — regeneration must be idempotent.
4. Dedupe by `(owner, slug)`.
5. Hook every mutation path; a manual step will be forgotten.
6. Regenerate the whole prompt from a single source of truth.
7. Prove it end-to-end against the live prompt, not the file.

---

*README-only documentation remediation. No functional artifact file was changed.*
