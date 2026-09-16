---
name: inference-expert-agents
description: "Turn an AI agent into an expert at inference — difficulty triage, deliberation budgets, self-consistency, claim-level verification, citation gates, judge ensembles, calibrated abstention, cost cascades, semantic caching, deep-research loops, agent memory, MCP exposure, eval regression gates, and answer certificates. Use for deciding how much inference compute to spend, verifying claims before asserting them, avoiding overthinking/hallucination/verification-theater, and controlling inference cost."
version: 3.0.2
categories: [agents, productivity, knowledge]
topics: [inference, test-time-compute, self-verification, uncertainty, cost-control]
metadata:
  openclaw:
    emoji: "🧠"
    requires:
      bins: [python3]
---

# 🧠 Inference Expert Agents

Load this skill to become an **expert at inference**: spend inference compute where it buys
truth, verify before asserting, abstain when uncalibrated, and never pay cost without a
measurable quality return. v2 adds: triage+planner, sampling self-check, citation gate,
judge ensembles, conformal abstention, cascades, caching, run tracing, deep research,
memory, tool-call guards, debate, eval gates, drills, answer certificates, chain-of-verification (`cove.py`), token-efficiency
(`compress.py`), model portability (`portability.py`), throughput (`speed.py`), and
mechanical self-improvement (`selfimprove.py`) — all as
composable stdlib-only CLI tools in `tools/` (JSON in/out; chain with `|`). v2.2 adds local retrieval (`retrieval.py`), output condensing (`brevity.py`), near-JSON repair (`jsonfix.py`), and opt-in upgrades across eight tools — all additive, no default output changed.

**Grounded in verified research** — see `references/verified-grounding.md`. Machine agents:
read `manifest.json` first (tool registry + progressive-disclosure loading plan); pipe any
tool output through `tools/_compact.py` when a machine is the consumer (~15-25% fewer tokens).

## Workflow: triage → plan → execute → verify → certify

```bash
python3 tools/triage.py --text "QUERY"                  # F1 difficulty + preset
python3 tools/deliberate.py --difficulty hard --budget-tokens 3000 \
    --force-final-at 2500 --cost-cap-usd 0.20           # F2-F6 rung plan w/ early-exit
# ... execute the plan (ladder below) ...
python3 tools/inference_scorecard.py --text-file ans.md --difficulty hard
```

## The Escalation Ladder — spend compute in stages, stop when calibrated

Escalate ONLY when the previous rung fails its check. De-escalate on cost cap.

| Rung | Pattern | Use when | Stop rule |
|---|---|---|---|
| **L0** | Single fast pass | Simple/factual/conversational | Confidence ≥ τ (0.9) |
| **L1** | Self-consistency: 3–5 sampled chains, majority | Math, logic, multi-step | Convergence; else escalate |
| **L2** | Decomposition + self-check (`selfcheck.py`) | Answers asserting facts/numbers/names | Every atomic claim checked |
| **L3** | Tool-grounded verification (`grounding_gate.py`) | Citations, quotes, dates, computations | Each load-bearing claim confirmed by primary source/execution |
| **L4** | Draft-verify loop + judge panel | High-stakes synthesis | Rubric passes, or abstain with partial answer + gaps |

**Hard caps before starting** (token/wall/cost); at cap, deliver best-verified answer +
state what is unverified. Budget forcing: `--force-final-at` makes "Final Answer" a hard
requirement, not a hope. Early-exit at confidence ≥ 0.90; abort (likely ill-posed) at ≤ 0.20
mid-rung. **F7** — scorecard now reports `atomic_claim_support` (FActScore-style % of atomic
factual claims with per-claim support). **F12 code-as-oracle**: route ALL arithmetic, data
transformation, date math, and simulation to executed code; debug the code on error, never
re-improvise the arithmetic.

## Verification toolkit (run before delivering)

- **F8/F9 `selfcheck.py`** — SelfCheckGPT-style: sample N responses to the same prompt,
  score each atomic fact by max token-overlap with samples; cluster entropy flags
  model-uncertainty. `likely`-risk facts → L3, never deliver raw.
- **CoVe `cove.py`** — high-stakes answers: plan verification questions per claim, answer them
  in a FRESH context that never saw the draft (factored — joint checking re-imports the draft's
  hallucinations), `crosscheck` → keep/revise/drop, `revise`, then grounding gate. Halved
  hallucinated entities per response in the source study.
- **F10/F11 `grounding_gate.py`** — per-sentence citation gate: cited sentences must match
  their evidence (lexical ≥0.10 or trigram-cosine ≥0.40; v2.2 also reports `rouge_l_recall`); uncited factual sentences →
  regenerate; unsupported → refuse. Verdicts: accept/regenerate/refuse.
- **F13/F36 `tool_guards.py`** — validate tool calls against a declared spec (hallucinated
  tools/args rejected pre-execution), strict JSON-schema subset checks for structured
  outputs, DSPy-style Assert (halt) vs Suggest (warn) retry semantics.

**`citecheck.py`** — verify a citation against the registry that minted it BEFORE you
repeat it. `scan` proves the id resolves; `check` proves the attribution (title /
first author / year) — you need both, because in the v3.0.0 audit all 18 cited ids
resolved while 12 were still wrong about what they point at. Verdicts:
CONFIRMED / MISMATCH / NOT_FOUND / **UNREACHABLE** (registry unreachable is *not* a
verdict — never report it as verified). `--strict` exits 2 so a pipeline stops.

**`theatre.py`** — audits whether a check you already ran could actually have failed.
Feed it the JSON of any verify tool; it reports `theatre_risk` and names the exact
field that proves it: thresholds set so every sentence passes, a `grounded` verdict
with zero overlap, zero sentences audited behind `decision=accept`, a selfcheck with
<2 samples, a certificate whose claims are still unverified, judges that are not
independent. `--fail-on high` makes the pipeline stop. This is trust-contract rule 4
made executable.

## Judge ensembles (F14–F17) — `judge_panel.py`

Never trust a single judge: aggregate ≥3. Modes: `majority`, **`minority-veto`** (any fail
vetoes — robust to validator agreeableness), `weighted` (inverse per-judge FP+FN rates,
label-free). Embed the 12-bias checklist (`bias-checklist` subcommand: position, style,
bandwagon, authority, self-preference, length, sentiment, fabricated-citation, sycophancy,
confirmation, anchor, capability-leniency) into judge prompts; randomize option order,
mask style. Low inter-judge agreement → escalate to L3 evidence, not more judges.

## Calibrated abstention (F18–F21) — `conformal.py`

Log (uncertainty u, correct?) pairs from real traffic; `calibrate` picks the largest
accept-threshold whose Hoeffding upper bound on accepted-error ≤ α (default 0.10/δ=0.05).
`curve` = coverage–risk tradeoff. `gate`: accept / **escalate** (UCCI: try stronger rung
before abstaining) / abstain. Hoeffding is conservative at small n — collect ≥200 labeled
points before tightening α.

## Cost control (F22–F26)

- **`cascade.py`** — FrugalGPT/RouteLLM: cheapest-first model cascade with quality target
  + expected savings; speculative draft-verify pair (2–3× decode).
- **`cache_kit.py`** — exact+semantic (token-Jaccard) answer cache, TTL + LRU, state only in an
  opt-in `--db` file (0600); lower `--threshold` (~0.45) for paraphrase hits; re-verify semantic hits against
  time-sensitive facts.
- **`ladder_trace.py`** — per-rung token/cost/latency telemetry + failure taxonomy
  (prompt|tool|retrieval|orchestration|verification). Highest-cost rung with least gain =
  your triage bug.

## Deep research (F27–F29) — `deep_research.py`

plan → search → read → synthesize → verify → report, with source tiering
(primary/secondary/tertiary) and stopping rules: ≥2 independent sources per load-bearing
claim or declare unknown; reserve ~⅓ of budget for the verify phase; deliver with
per-sub-question confidence + explicit unknowns.

## Memory (F30–F34) — `memory_kit.py`

Three stores: `reflection` (task→failure→lesson episodes), `rule` (distilled rules-of-thumb,
surfaced when relevant), `skill` (named reusable procedures, Voyager-style). Deliberate
forgetting via `forget --older-than-days` + per-kind caps; accidental forgetting is the
failure mode, so caps are generous and eviction is explicit.

## Chain-of-verification (v2.1.x) — `cove.py`

Draft → `plan` (split into claims + factored verification questions) → answer every
question in a FRESH context that never saw the draft → `crosscheck` (claims-file +
answers-file → supported/refuted/unverified per claim, keep/revise decision; v2.2: `UNSUPPORTED`/hedged answers → `unverified`, never `refuted`) → `revise`
(refuted removed, unverified labeled `[unverified]`), then `grounding_gate` before
delivery. Factored execution is the load-bearing detail (Dhuliawala et al., ICLR 2024).

- **`manifest.json`** — tool registry (name/file/purpose/subcommands) + `loading_plan`
  (core → verify → ops) for progressive disclosure.
- **`_compact.py`** — strip JSON whitespace for machine consumers (~15-25% fewer tokens). `--keys` maps keys to k0…kn under a header (`--expand` restores losslessly).
- **`_common.py`** — internal: the clean-error contract — tools emit `{"error":…}` +
  exit 2 on bad input/state, never a traceback.

## Integration & ops

Persistent state is **strictly opt-in**: `cache_kit`, `memory_kit`, `ladder_trace`,
`eval_regression`, `retrieval`, and `selfimprove` write nothing unless you pass `--db PATH`. State files can
contain prompt/eval text — keep the path private; 0600 perms are ENFORCED on every write AND
every load (loose pre-existing files are repaired automatically). Without `--db` they refuse
stateful operations — zero files, zero residue. Corrupt or unreadable state files are
refused with a clean error and left untouched — never silently reset (delete or restore
the file, then retry); all state writes are atomic (tmp + rename).

- **F35 `mcp_server.py`** — expose triage/scorecard/conformal-gate/cache/certificate over
  MCP (stdio JSON-RPC 2.0). **F38 approval gate**: tool calls that execute side effects
  require explicit human approval in the transcript before dispatch — treat approval as a
  first-class step, not a nicety. All five built-in tools are side-effect-free; the gate
  validates call structure (known tool, required args present, no extra args) and refuses
  any call flagged `wants_side_effects` unless a human approved it in the transcript
  (run the underlying CLI directly instead). All five tools carry MCP `readOnlyHint` annotations.
- **F39/F47 `eval_regression.py`** — golden-set regression gates (pass-rate gate blocks
  promotion), baseline-vs-candidate comparison, runs ledger, `schedule` continuous-eval recipe.
  **F40 annotation queue** — every gate failure lands in `queue`; humans label → golden
  case. Treat evals like CI.
- **F42 `sandbox_drill.py`** — 5 planted-error drills (stale wheel, missing interpreter,
  dirty env, OOM-137, stale index) + transcript hygiene verdicts.
- **F44/F45 `debate.py`** — round schedule + consensus stability for multiagent /
  heterogeneous-expert debate; contested consensus → L3, never ship it.
- **F46 `answer_certificate.py`** — bind the answer to per-claim {method, verdict,
  evidence}; `validate` before delivery; refuted claim ⇒ revise or abstain;
  `unverified` ⇒ conditionally-certified (label it).

## Efficiency & portability (v2.1) — spend fewer tokens, run on any model

**INPUT tokens — `compress.py`**: contexts ≥ ~500 est-tokens are worth compressing (LLMLingua
guidance); below that, overhead wins. Never drop sentences carrying numbers, quotes, or
citations; review `dropped_review` for lost connectives. `stats` gives the token budget first.

**OUTPUT tokens — the Chain-of-Draft contract** (`compress.py draft`): ≤5 words per reasoning
step, then `Final answer:`. ~80% fewer reasoning tokens at matched accuracy (arXiv:2502.18600).
Enable ONLY for models ≥7B (`portability.py` gates it) and only after an `eval_regression` A/B
passes on your golden set.

**Machine-readable mode**: all tools emit JSON; for machine consumers add
`| python3 tools/_compact.py` (`--keys` for a deeper cut, `--expand` to restore). Manifest-driven loading: an agent that needs one check reads one
manifest row + `--help`, not the whole SKILL.md.

**Portability — `portability.py`**: classify the model (name or `--params-b`) → tier settings:
samples (frontier 3 → mid/small 5 → local 1), checklist size (12 → 0), flat schemas below large,
CoD off below 7B, `abstention_tau` 0.90 → 0.80, verbosity budget 1.0 → 0.25. **Never use strict
JSON mid-reasoning on any tier** — reason freely, then emit the structured verdict. `--emit-prompt` prints the tier settings as a ready system-prompt snippet.

**Throughput — `speed.py`**: measure tok/s; local stack levers in priority order (continuous
batching 5-10× → EAGLE-2 2-3× / Medusa 2.2-3.6× → INT4 −75% cost at 1-2% quality → prefix
caching with a byte-stable doctrine prefix); API levers (batched `n>1` sampling in one request,
provider prompt caching, cascade routing, early-abort). Log per-rung latency in `ladder_trace`. `measure --samples-file` aggregates batch runs (n/mean/p50).

**Self-improvement — `selfimprove.py`** (mechanical, not vibes): `eval_regression` failures →
`propose` (drafts ≤3 rule amendments via the running model) → re-run evals → `adopt` (gated on
measured pass-rate delta ≥ +0.02; frozen if pass rate < 0.5) → `record` wins/losses per rule →
`rank` by Wilson lower bound → `prune` consistently-lossy rules. Every adopt/reject is audited
in the db. `rank --method thompson` (+`--seed`) explores by posterior sampling instead of the Wilson bound.

**Debate caveat**: debate is the most expensive pattern and judge ensembles often override it —
run it only when judge disagreement is high, cap rounds (≤3), and require consensus ≥ 0.67.

## What changed in v3 (pointer, not payload)

v3.0.0 is a **correctness release**: six tools returned wrong answers (not crashes)
and 12 citations in `references/verified-grounding.md` were mis-attributed. Two new
tools: `citecheck.py` (verify a citation against arXiv/OpenAlex before repeating it)
and `theatre.py` (flag a verification result whose check could not have failed).
`selfcheck.py` no longer flags facts its own samples confirm, and no longer invents a
maximal hallucination score from a single sample; `grounding_gate.py` rejects
thresholds that cannot fail and reports the sentences it skips; `conformal.py`
validates its risk parameters.

Full measurements and rationale: `references/release-notes-v3.md` — load it only when
you need the history; it is not required to use the skill.

## Trust contract (unchanged, non-negotiable)

1. **Decompose before asserting** — verify atomic claims, not narratives.
2. **Citations are guilty until verified in-session** — unverified ⇒ labeled or dropped.
3. **Mark uncertainty explicitly**; honest abstention beats confident hallucination.
4. **No verification theater** — a check that cannot fail is not verification.
5. **Compute, don't guess, arithmetic** — code is the oracle (F12).

## Known limits (reviewer-consulted; do not skip)

Swarm review (groq/gpt-oss-120b, cohere/command-a, gemini-3.1, llm7) converges on the
false-confidence surface: **certificates certify the checking, not the truth** — a
certificate with `unverified` claims is a to-do list, not a pass; never let the artifact's
existence substitute for reading it. **Conformal thresholds assume the calibration
distribution holds** — distribution shift/adversarial prompts invalidate them; recalibrate
on fresh labels and treat long-lived thresholds with suspicion. **Caches and judges inherit
their inputs' errors** — a cache hit is not evidence; a judge majority is not a source.
v2.1.x ships `cove.py` (chain-of-verification), `compress.py`, `portability.py`, `speed.py`,
`selfimprove.py`, `manifest.json`, and `_compact.py`; v2.1.2 merges those with the 1-hour
live-pilot hardening (0600-everywhere, no-traceback contract, triage/scorecard/MCP fixes); v2.2.0 adds local retrieval, output condensing, near-JSON repair, and opt-in upgrades — all additive, no default output changed.
Still open: dynamic context pruning, human-in-the-loop escalation triggers,
feedback-driven trust calibration.

## Failure modes (named, refuse them)

Overthinking · Underthinking · Confident hallucination · Verification theater ·
Budget blowout · Answer pressure. Expert habits: triage every nontrivial query, reserve ~⅓
budget for verification, log every rung to `ladder_trace`, gate releases on
`eval_regression`, certify high-stakes answers.
