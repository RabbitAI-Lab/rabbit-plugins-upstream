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
5. `scripts/md_preflight.py` — stdlib-only static checker (**22 gates, G01–G22**, with
   `--explain Gxx` one-line fixes and `--json`) that scans your kernel + input dirs before
   you push, so the known footguns never reach a GPU session — including **G21
   (`enable_gpu` missing → the silent-CPU-session trap)** and **G22 (unguarded CPU
   fallback)**, both born from the 2026-09-08 incident.
6. `registry/` — **machine-readable fact layer** with stable IDs: `traps.json` (TRAP-01..24),
   `rules.json` (R01..R20), `errors.json` (ERR-001..023: error text → cause → one-line fix),
   `params.json` (exact simulation parameters + budget math + calibration mode),
   `calibration.json` (**CAL-01..12 literature-verified acceptance gates** for a 5 ns
   orlistat–1LPB positive control, with the verified citation table and the 2026-09-09
   corrections log), `lessons.jsonl` + schema.
7. `scripts/skill_query.py` — **surgical fact retrieval for any model size**: fetch one trap /
   rule / error / param subtree by ID, `error <text>` lookup, or `essence` (an ultra-compact
   ~45-line briefing + `--json`) — grounding without 40 KB of prose in the context window.
8. `scripts/learn.py` — **safe self-improvement loop**: schema-validated append-only lesson
   log (hypothesis → observed → verified, the last only with `--human-approved`); entries are
   promoted into the registry by a human at publish time, never automatically.
9. `scripts/selftest.sh` — proves the skill itself is intact (compiles all scripts, runs the
   checkers' fixture selftests, validates registry JSON + cross-references, CLI smoke tests).

Use it when you plan multi-hour MD on Kaggle and want to skip the ~30 GPU-hours of debugging
the original author already paid.

## What's new in v1.2.3 (2026-09-09)

- Completes the v1.2.2 QA polish: the R17↔R03 contrast line is now actually present
  (a silent edit miss in 1.2.2 — caught by the post-publish byte-size audit). All other
  content identical to 1.2.2.

## What's new in v1.2.2 (2026-09-09)

- QA polish from the 8-model post-publish audit: `registry/calibration.json` version field
  synced with the skill version; R17 now explicitly contrasts R03 (WHICH GPU vs WHETHER you
  get one); the micromamba bootstrap documents the Kaggle-runs-as-root fact (and the
  `$HOME/.local/bin` fallback for non-root hosts). No behavioral changes — all 19
  deterministic regression checks and the full selftest pass unchanged.

## What's new in v1.2.1 (2026-09-09)

- **Security-audit hardening** (ClawHub A.I.G findings fixed):
  - **T03 (Error) fixed** — the micromamba bootstrap is now a pinned release (1.5.10) with
    SHA-256 verification before extraction and a single reviewed archive member; the mutable
    `latest` pipe-to-tar variant is retired everywhere, including as a documented pattern.
  - **T08 (Warning) fixed** — the kaggle CLI install is pinned (`kaggle==2.2.4`) and the
    reproducible conda lock-file variant is documented next to the env create.
  - **T09 (Warning) fixed** — preflight gate G14 now scans run.py + run_md.py +
    kernel-metadata.json against 5 secret shapes (JSON hex key in either order, username+key
    pair, KAGGLE_KEY/TOKEN assignments, private-key blocks, generic token literals) and states
    plainly that PASS is a heuristic, not proof — run a real scanner before publishing.
  - SkillSpector notes addressed: the safety-boundaries section now states exactly what
    learn.py writes and when, defines a machine-checkable trigger for the opt-in supervisor,
    and recommends the platform process supervisor over `nohup &`.

## What's new in v1.2.0 (2026-09-09)

- **Calibration protocol**: a literature-grounded positive-control run (5 ns orlistat in 1LPB,
  dt 2 fs, no HMR) validated against 12 published-observable gates CAL-01..12 — every number
  verified against the primary-source full text (Veeramachaneni 2015 DDDT 9:4397,
  doi:10.2147/DDDT.S84052 and seven more anchors; model-hallucinated citations were caught
  and corrected during verification).
- **The Silent CPU Session hardening**: TRAP-22/23/24, rules R17–R20, errors ERR-021..023,
  and preflight gates G21/G22 — a kernel-metadata.json without `"enable_gpu": true` can no
  longer slip through and burn a 12 h session at ~100× slowdown unnoticed.
- Fixed the version lag (SKILL.md said 1.1.3 while the published version was 1.1.4).

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
# Expected: be7a8ff2e23de1abb6daf3998bb7c6d1bfd87d2217ccda5fcbd92a3af70161b1
```

If the hash does not match, do not trust the file — re-fetch the skill from the publisher.
