# 🧬 Kaggle OpenMM MD Runbook

A battle-tested field manual **plus** a static preflight checker for running long (≥10 ns,
up to 100 ns) OpenMM molecular dynamics on Kaggle's free GPU tier. It was born from a
22-kernel-version (v34→v56) debugging saga of a real 100 ns mebendazole ↔ 1LPB
pancreatic-lipase–colipase simulation on a Tesla P100 — every command that actually worked,
every trap that cost hours, and every false-positive "fix" to avoid.

**Honest scope.** This is not a click-button MD service. It is:
1. `SKILL.md` — the distilled quick-start: non-negotiable rules, the three fatal traps,
   equilibration ladder, production/checkpoint design, debugging toolkit, API-drift matrix.
2. `RUNBOOK.md` — the complete original field manual (every command and log line, verbatim).
3. `references/traps-and-api-matrix.md` — the RECELL postmortem, OpenMM 8.3.1↔8.6 drift table,
   GPU/Kaggle traps, false-positive list, toolkit code sketches.
4. `references/operations.md` — session budget math, supervisor-loop pattern, command trios.
5. `scripts/md_preflight.py` — stdlib-only static checker (15 gates, G01–G15) that scans your
   kernel + input dirs before you push, so the known footguns never reach a GPU session.
6. `scripts/selftest.sh` — proves the skill itself is intact (runs the checker's fixture-based
   `--selftest` plus file-presence checks).

Use it when you plan multi-hour MD on Kaggle and want to skip the ~30 GPU-hours of debugging
the original author already paid.

## How to use

```bash
# fast path
cat SKILL.md
python3 scripts/md_preflight.py --kernel /path/to/md_run/kernels --input /path/to/md_run/input
bash scripts/selftest.sh
```

Then follow `RUNBOOK.md` §0 (TL;DR) for the operational loop: `kaggle kernels push/status/output`,
checkpoint-resume dataset versioning, and the single supervisor loop.

## 🔐 Permissions

| Action | Scope |
|---|---|
| Files read | **Only** inside the directories you pass via `--kernel` / `--input`. The checker is static — it opens nothing else. |
| Files written | None by the checker. `selftest.sh` and `--selftest` build fixtures only in `tempfile` dirs (auto-cleaned by the OS). |
| Network calls | **None.** Zero outbound traffic. The `kaggle` CLI, if you use one, is invoked by you in your own shell — never by this skill. |
| Credentials read | None. The skill does not read `~/.kaggle/kaggle.json`, env vars, or any key file. (Gate G14 actively *detects* keys accidentally embedded in `run.py`.) |
| Privileges | None beyond read access to the dirs you pass. |

## 🔒 Security & Privacy

- **No data leaves your machine.** The checker reads files, pattern-matches, prints one line per
  gate, and exits. No telemetry, no remote calls, no caching.
- **No credentials handled.** It never reads or stores secrets; it only *warns you* if a secret
  looks embedded in your kernel file.
- **No logging of file contents.** Gate outputs name files and short matched fragments only —
  never full file bodies, SMILES, or protein sequences.
- **Review before install.** `scripts/md_preflight.py` (~400 lines of pure stdlib Python) and
  `scripts/selftest.sh` (plain bash) are short enough to read in minutes. No compiled code, no
  binaries, no fetched dependencies.
- **No persistence.** Nothing is written to `~/.config`, `~/.cache`, or shell profiles.
  Uninstall = delete the skill folder; nothing to deregister, no daemons to stop.
- **Selftests never touch real user state.** Fixtures are built under `tempfile.mkdtemp` only.
- **Human-in-the-loop for anything live.** The reference docs describe operating a personal Kaggle
  pipeline; any command that mutates remote state (pushes, dataset versions) or launches the
  opt-in monitoring loop is executed only on the human's explicit instruction, with their own
  credentials, and the docs say so explicitly (see "Safety boundaries" in `SKILL.md`).
- **Credential-handling policy.** No file in this skill reads credential contents; gate G14
  exists precisely to *prevent* secrets from being committed into kernel code.

## ✅ Verification

After installation, verify the quick-start's integrity:

```bash
sha256sum skills/kaggle-openmm-md-runbook/SKILL.md
# Expected: 1031412f8c1f4f4b243dcef15a05a5cce03b75793e331ec2d9207f925869b5bc
```

If the hash does not match, do not trust the file — re-fetch the skill from the publisher.
