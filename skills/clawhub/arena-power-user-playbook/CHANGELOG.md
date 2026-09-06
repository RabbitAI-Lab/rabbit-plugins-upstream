# Changelog

## v2.0.0 — 2026-09-06 — full rebuild: grounded + executable

### Why
A grounded, evidence-based audit of v1.2.6 found the package did not do what
its documentation claimed:

- **Phantom scripts.** SKILL.md documented `arena_mode_detector.sh`,
  `pineapple_detector.py`, `chunk_manager.py`, `run_max_speed.sh` plus
  external scripts (`selfheal_runner.sh`, `prompt_cache_layer.py`,
  `run_swarm_optimized.sh`) — none present in the bundle, none verifiable.
- **Unverifiable statistics.** "5M+ pairwise votes", "+12 Elo", "82M+ votes",
  "$250M+ funding", "34 t/s" — no source; removed.
- **Factual errors vs the live product** (verified against arena.ai official
  pages and the live leaderboard, 2026-09-05/06): "Max router" is not a
  router — Max/High/xHigh are per-model compute tiers on the leaderboard;
  "Code Arena" is not a documented mode (Documented modes: Battle, Direct,
  Side-by-Side, Agent); "Fable 5 suspended June 2026 export control" is
  contradicted by Fable 5.1 (Max) ranking #1 on 2026-09-05; "GPT-5.4-High
  removed" contradicted by GPT 5.4 (High) active at #26.
- **Constraint conflict.** The local-GGUF fallback matrix (llama.cpp-style
  0.6B–1.5B models) conflicts with the standing cloud-only rule and is not a
  frontier-equivalent fallback.
- **Version drift.** Registry 1.2.6 vs frontmatter 1.3.0.
- **Untestable heuristics.** The "Pineapple" detector was prose regex, not a
  runnable or testable check.

### Added
- `scripts/arena_playbook.py` — offline, python3-stdlib-only CLI (7
  subcommands): `mode` (deterministic mode advisor with complexity heuristic
  and budget-conscious downgrade), `weak` (weighted weak-response screener:
  refusal/short/apology/vagueness/repetition/truncation, 3-band output,
  explicit "not a quality judgment" contract), `model-check` (dated
  snapshot vs fresh dump: rank drift, rotated-out, new/renamed, historical
  dump warning, normalized (name, tier) matching that reports — not guesses —
  unmatched entries), `snapshot` (write new dated snapshots with rank
  contiguity validation), `state` (SESSION-STATE.md manager: init with
  overwrite protection, add with de-duplication, summary, next, validate),
  `stats` (local feedback log/report — the self-improvement loop), `selftest`.
- `data/model_snapshot_2026-09-05.json` — top-30 of the live Agent Arena
  leaderboard with real signal values, source URL, fetch date, methodology
  citation, and the board's own "signal leaders".
- `references/modes.md` — the four documented modes with official sources
  and dates; Agent Mode capabilities and official task mix (coding 29%,
  research 11%, planning 11%, automation 3.9%); what is NOT a documented mode.
- `references/leaderboard.md` — causal-tracing methodology and the five
  official signal definitions; (model, tier) entry semantics; executable
  rotation protocol; what not to read into the numbers.
- `references/fallback.md` — cloud-only fallback table (no local GGUF),
  measurable 3-strike weak-response escalation, chunking/state-carry pattern,
  local stats loop.
- `tools/playbook_selftest.py` — 10 offline groups: consistency + phantom-
  reference scan, mode advisor cases (incl. single-file → Direct regression),
  weak screener bands/determinism, model-check drift/rotation/stale-dump,
  snapshot writer validation, state manager lifecycle/corruption, stats
  loop, snapshot data integrity, CLI contract, honesty-phrase checks.

### Changed
- "Max" reframed from "router" to per-model compute tier (matches live
  leaderboard entry format).
- Mode selection: complexity heuristic replaces "files ⇒ Agent" (single-file
  questions stay Direct; Agent is for multi-step tool workflows — matches
  official task-mix data).
- Fallback: cloud-only, family-equivalence with "verify the model exists"
  step; local GGUF matrix removed.
- Version: single source of truth (frontmatter == registry == CHANGELOG).

### Evidence
- arena.ai homepage, /agent, /leaderboard/agent, /blog/agent-mode,
  /blog/agent-arena-methodology — fetched 2026-09-06 (dates and figures in
  references/).
- Live leaderboard: board date 2026-09-05, 59 models, 2,285,256 sessions.
- Self-test: 10/10 groups pass; functional matrix exercised in CI-less local
  runs (see debug findings below).

### Debug findings (multi-model consensus + direct evidence)

Method: local functional matrix (all 7 subcommands exercised end-to-end,
78-check self-test) + three independent model audits of the full package
(cohere/command-a, llm7, gemini 3.7-flash — openrouter was quota-cooled
mid-run and could not complete a report; its earlier 402 credit failures
are recorded here as tooling evidence, not model findings) + a
two-model diff re-audit of the fixed code. Consensus rule: act on
2+ independent models agreeing or on direct byte-level evidence; every
finding's quote is verified against the file first (findings citing
non-existent lines or misreading quoted code are rejected with rationale).

Acted on (4 fixes):
- State-file phantom placeholder (gemini fragment, byte-verified):
  `_write_state` emits `- (none yet)` for empty Done/Next sections and
  `_parse_state` read it back as a real item, so it leaked into done
  counts and the state-carry message ("completed so far: (none yet); ...").
  Parser now skips the placeholder; regression checks 6d2/6d3 added.
- Vagueness threshold 0.01 -> 0.02 (cohere): with specific multi-word
  hedges, 0.01 flagged one hedge in any ~100-word response; 0.02 encodes
  "one hedge in a short (<50-word) response" and is documented in code
  and references/fallback.md.
- SKILL.md snapshot row now names the source (arena.ai/leaderboard/agent)
  and both dates, not just "sourced" (cohere).
- Documented the known false-positive paths of the weak screener
  (opening "I can't" in a legitimately short answer; "I'm an AI
  enthusiast"-style self-identification; single hedge in a very short
  answer) in references/fallback.md (from the rejected-below discussion —
  documented instead of code-changed, per the screening contract).

Rejected with rationale (6):
- Cohere (x2): "budget flag never passed to cmd_mode / --budget-conscious
  not implemented" — misread: `args.budget_conscious` is passed in both
  the single-task and batch paths, the argparse flag exists, and
  self-test 2f proves the downgrade path executes (mode=direct +
  "downgraded" reason).
- Cohere: GGUF-removal statement in fallback.md "redundant/confusing" —
  it is an intentional guardrail (documents why local GGUF was removed so
  it is not re-added); kept.
- Gemini: "APOLOGY_RE capturing-group bug" in findall — with a single
  group, findall returns one element per match either way; the count is
  identical. No behavior change possible; rejected.
- Cohere (diff pass): refusal in 3rd sentence of a >=80-word response is
  "a false negative" — that is the documented design (a refusal buried in
  a long response is not a task refusal); and the cited no-punctuation
  edge case ("I can't do this because I am an AI") is verified to flag
  correctly (no punctuation => whole text is sentence[0] => early=True).
- Cohere (diff pass): "DeepSeek V4 Pro (High) (0813) only strips (High),
  breaking consistency" — misread: the regex matches the LAST parenthetical
  "(0813)", which is not a tier word, so the full name is kept with
  tier=""; llm7 independently verified the same; snapshot and dump use the
  same normalizer, so matching is consistent.
- llm7: clean bill of health in both passes (no findings to accept or
  reject) — recorded as the third independent clean read.

Also caught during local testing (pre-audit): a nested-tuple return bug in
_load_latest_snapshot (model-check could not find its own baseline
snapshot — self-test group 4 caught it), a tier regex anchored to match
only bare parentheticals (no tier ever extracted — self-test group 5
caught it), and an over-eager refusal rule that flagged "I can't
guarantee ..." mid-response (self-test 3c caught it).

## v1.2.6 — 2026-08-06 (registry; frontmatter claimed 1.3.0)
Registry-published state. Documented executable scripts and integrations that
were not present in the bundle; unverifiable statistics; local-GGUF fallback
matrix; outdated/incorrect frontier-model claims. Superseded by v2.0.0.
