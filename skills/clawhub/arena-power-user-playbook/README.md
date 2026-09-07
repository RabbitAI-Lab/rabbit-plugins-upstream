#  arena-power-user-playbook

**Categories:** productivity, research
**Tags:** #productivity #arena-ai #model-selection #leaderboard #power-user

## ✨ What this skill is

An **executable** power-user playbook for arena.ai: a dated, sourced model
snapshot plus offline python3-stdlib scripts for mode selection
(Direct / Agent / Side-by-Side / Battle), leaderboard rotation checking,
measurable weak-response screening, chunked multi-chat state carry, cloud-only
fallback, and a local feedback log.

v2.0.0 rebuilt the skill after a grounded audit found the v1.x package
documented scripts that were not present, cited unverifiable statistics, and
carried a local-GGUF fallback matrix that conflicts with cloud-only practice.
Everything claimed here either runs (scripts), is dated and sourced
(`references/`, `data/`), or is explicitly labeled a heuristic.

## 🚀 Usage

Install from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/arena-power-user-playbook
```

```bash
cd arena-power-user-playbook
python3 scripts/arena_playbook.py selftest            # verify the install
python3 scripts/arena_playbook.py mode --task "build a dashboard from this csv" --files 1 --steps 3
python3 scripts/arena_playbook.py weak --response "$(cat reply.txt)"
python3 scripts/arena_playbook.py model-check --dump my_leaderboard_dump.json
python3 scripts/arena_playbook.py state --file SESSION-STATE.md --action init --goal "Ship X"
python3 scripts/arena_playbook.py stats report
```

Exit codes: 0 ok · 1 findings/changes · 2 usage or no data · 3 internal error.
All outputs are machine-readable; one summary line on stdout, full JSON with `--out`.

## 🔐 Permissions & Requirements

- python3 (standard library only) — no dependencies, no network access.
- Read/write only the files you pass to it (state files, dumps, logs).
- No credentials are read, stored, or logged by this skill.

## 🔒 Security & Privacy

- Local scripts process only user-supplied files; nothing leaves the machine.
- Using arena.ai sends your prompts to arena.ai's servers — share only data
  appropriate for that service.
- The model snapshot is a dated comparison baseline, not a recommendation
  engine; verify names against the live board before acting.

## ✅ Verification Hash

This digest covers every stable artifact file except `README.md`
(self-reference), generated `skill-card.md`, registry-generated `_meta.json`,
and `.clawhub/` bookkeeping.

**Artifact SHA-256 (TREE-SHA256-v1):** `c8f27b5341bac5d2ef700758d25e50f839c915c8d3a6b4336b654ff67806d93e`

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
file differs from the published artifact; review before use.
