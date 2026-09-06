# 🎨 speechcanvas-free-expression-swarm

**v2.0.3 — Structured, validated, self-improving edition.**
A 4-agent image-prompt swarm (Muse drafts → Guardian safety-checks → Critic perfects realism →
Composer finalizes) that turns a lawful creative brief into a **validated symbolic image prompt
pack** (JSON) for journalism, protest, censorship, debate and civil-liberties themes.
Lawful, consent-aware, non-deceptive: deception is a subject portrayed through allowed motifs,
never a method (no fake evidence, no real-person depiction, no hate).

## ✨ What it does

- **Reply-first speed protocol**: shows the concept draft immediately, refines in parallel.
- **Deterministic pattern-based safety gate (best-effort)**: `scripts/safety_validator.py` — 13 block rules + 2 warn rules,
  leetspeak/obfuscation normalization, negation-aware (a pack's own safety fences never
  self-trigger), motif enforcement for deception themes. Machine-readable JSON verdict, exit
  codes 0/1/2.
- **Structural schema gate**: `schema/prompt_pack.schema.json` (JSON Schema 2020-12) +
  offline stdlib checker `scripts/validate_pack.py`.
- **Machine-readable roles**: `swarm/roles.json` — terse goal/must/never/output_fields per
  role; works in any SKILL.md-compatible agent, no vendor-specific syntax.
- **Self-improvement**: `scripts/record_run.py` — builds a validated run record; prints it to
  stdout by default (zero file writes) and appends to a JSONL log only when the operator
  explicitly passes `--out`. The review protocol re-injects recurring critic fixes and
  guardian failures into future runs.
- **5 validated example packs** in `references/examples.md`; **authoritative rules** with a
  manual checklist in `references/rules.md`.
- **Sandboxed selftest**: `scripts/selftest.sh` — 25+ checks, runs in a throwaway `HOME`.

## 🚀 Usage

```bash
openclaw skills install @orionshaowswmw/speechcanvas-free-expression-swarm
# or: npx --yes clawhub@latest install speechcanvas-free-expression-swarm
```

Give the agent a lawful brief ("symbolic image about censorship"). The agent runs the swarm,
then gates the result:

```bash
python3 scripts/safety_validator.py --file pack.json   # exit 0=PASS 1=BLOCK 2=WARN
python3 scripts/validate_pack.py pack.json --final     # structural schema check
python3 scripts/record_run.py --brief-hash <sha> --iterations 2 --guardian PASS \
  --critic "colder light" --pack pack.json             # self-improvement log (append-only)
```

No python3? The agent follows the manual checklist in `references/rules.md` and says so.

## 🔐 Permissions

- **Reads**: the brief text the operator provides; optional pack/JSON files the operator
  points at; this skill's own files. Nothing else.
- **Writes**: NONE by default. `record_run.py` prints the run record to stdout; it appends to
  a file only when the operator explicitly passes `--out`, and then append-only — never
  overwrites, deletes, truncates, or writes outside the given path. No other script writes
  anything (the validator and pack checker are read-only; the selftest writes only inside
  its own throwaway sandbox directory).
- **Network**: none. **Secrets**: none. **Shell**: optional (python3 only); the swarm
  instructions work fully without executing anything.
- **System calls**: standard file I/O only (read, append). No environment mutation, no
  background processes, no package installs.

## 🔒 Security & Privacy

- No data leaves the machine: no network calls, no telemetry, no API keys, no cookies.
- **Persistent local run history is opt-in**: by default the skill writes no files at all;
  a run-history JSONL is created only if the operator explicitly passes `--out` to
  `record_run.py`, and that log is append-only with a documented schema.
- The selftest runs inside `mktemp -d` with a throwaway `HOME` and cleans up after itself —
  it never touches real user state (verified pattern against the ClawHub security scanner).
- The safety validator is read-only by construction (single `open(..., "r")` paths).
- The validator intentionally inspects only the pack's generative fields
  (subject/motif/lighting/lens/setting/gesture/critic_notes) and strips negated spans, so
  safety *fences* ("no fake documents") are never misread as *content*.
- Review before install: everything is plain text (Markdown/JSON/Python) — read
  `references/rules.md` and `scripts/*.py`; they are short on purpose.
- **Honest limitations of the safety gate**: the validator is deterministic *pattern*
  detection (regex + normalization). A `PASS` means "no known violation pattern was found" —
  it is NOT a proof of safety. Novel paraphrases, unfamiliar languages, or semantic
  violations can evade it. The executing agent MUST still apply the judgment checklist in
  `references/rules.md` and ask the operator when anything is ambiguous. The gate exists to
  catch known classes of violation, not to replace judgment.
- The `npx clawhub install` / `openclaw skills install` lines above are the standard ClawHub
  registry CLI — this skill performs no installation, download, or upgrade itself.

## ✅ Verification hash

sha256 of `SKILL.md` (this version):

```
d1c22d8c0c686f87326d8bbb3f04140a7eedb88b661f18d9afe31420436c21d5
```

Check it:

```bash
sha256sum SKILL.md   # compare with the hash above
```

## Compatibility & license

Plain files + optional stdlib Python 3 (no third-party dependencies, ever). Works with any
SKILL.md-compatible agent (Claude Code, Cursor, Codex CLI, OpenClaw, …) and any model that
can read JSON. MIT-0.
