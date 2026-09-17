# 🧠 Inference Expert Agents

A ClawHub skill that turns an AI agent into an **expert at inference**: difficulty
triage, deliberation budgets, self-consistency, claim-level verification, citation
gates, judge ensembles, calibrated abstention, cost cascades, semantic caching,
deep-research loops, agent memory, MCP exposure, eval regression gates, and answer
certificates.

## Safety posture (read before wiring this into a pipeline)

- **Nothing here executes anything.** Every tool is read-only and side-effect-free:
  no file writes unless you pass an explicit `--db`, no network calls except
  `citecheck.py` querying public scholarly registries (arXiv, OpenAlex), no shell
  out, no agent-state mutation. `mcp_server.py` annotates all five exposed tools
  `readOnlyHint` and refuses any call flagged `wants_side_effects` without explicit
  human approval in the transcript.
- **`selfimprove.py` never edits this skill.** It writes proposed rule amendments
  into an opt-in `--db` file and gates adoption on a measured golden-set delta.
  Skill files are inputs, not targets; keep them read-only at runtime.
- **A verdict from this skill is advice, not authorisation.** Any consequential
  action it informs (spending money, deleting data, shipping an answer to a user,
  promoting a model) still needs a human decision. `--fail-on` / `--strict` flags
  exist so a pipeline STOPS on a failed check rather than continuing.

## What it does

Plus a machine-readable `manifest.json` (tool registry + progressive-disclosure loading)
so any AI model can load only what it needs.

When loaded, this skill gives the agent:

- **The Escalation Ladder** — 5 rungs (single pass → self-consistency → claim
  decomposition → tool-grounded verification → draft-verify) with triggers, stop
  rules, hard cost caps, budget forcing, and early-exit/abort thresholds.
- **The trust contract** — decompose-before-asserting, citations-guilty-until-
  verified, explicit uncertainty, honest abstention, no verification theater,
  code-as-oracle for arithmetic.
- **Named failure modes** — overthinking, underthinking, confident hallucination,
  verification theater, budget blowout, answer pressure.
- **29 composable CLI tools** (stdlib-only, JSON in/out) + 1 internal module (`_common.py`):

| Tool | Features |
|---|---|
| `triage.py` | difficulty classification (trivial/standard/hard) + presets |
| `deliberate.py` | rung planner, adaptive budgets, early-exit/abort, budget forcing |
| `selfcheck.py` | SelfCheckGPT-style sampling check + cluster entropy (sentence-level, n>=2 enforced) |
| `citecheck.py` | verify a citation against arXiv/OpenAlex before repeating it |
| `theatre.py` | detect verification theatre: flag checks that could not have failed |
| `grounding_gate.py` | per-sentence citation validation → accept/regenerate/refuse |
| `judge_panel.py` | judge ensembles: majority, minority-veto, weighted; 12-bias checklist |
| `conformal.py` | calibrated abstention thresholds (Hoeffding UB), coverage–risk curve, escalation gate |
| `cascade.py` | FrugalGPT-style model cascade + speculative pairing |
| `cache_kit.py` | exact+semantic answer cache (TTL + LRU) |
| `ladder_trace.py` | per-rung cost telemetry + failure taxonomy |
| `deep_research.py` | deep-research loop planner + source tiering |
| `memory_kit.py` | reflections / rules / skills + deliberate forgetting |
| `tool_guards.py` | tool-call validation, strict structured outputs, Assert/Suggest retries |
| `mcp_server.py` | exposes 5 core tools over MCP (stdio JSON-RPC 2.0) |
| `eval_regression.py` | golden-set gates, baseline compare, runs ledger, annotation queue |
| `sandbox_drill.py` | 5 planted-error recovery drills + hygiene verdicts |
| `debate.py` | multiagent debate schedule + consensus stability |
| `answer_certificate.py` | machine-checkable answer certificates |
| `inference_scorecard.py` | rubric scorer incl. FActScore-style atomic_claim_support |
| `cove.py` | Chain-of-Verification: factored per-claim checks → keep/revise/drop |
| `compress.py` | input-token compression + Chain-of-Draft output contract |
| `portability.py` | model-tier classification + adapted inference settings |
| `speed.py` | tok/s measurement + serving-lever plans + parallel sampling |
| `selfimprove.py` | bandit rule ranking, pruning, gated TextGrad-style amendments |
| `_compact.py` | strip JSON whitespace for machine consumers (~15-25% fewer tokens) |
| `retrieval.py` | local BM25 retrieval (sqlite FTS5): build/query/stats for grounding |
| `brevity.py` | rule-based output condenser with protect-list + saved% report |
| `jsonfix.py` | staged near-JSON repair with repair log |

Grounded in verified research: test-time compute lifts AIME 15.6%→71% (→86.7%
with majority voting); speculative decoding 2–3×; FrugalGPT cascades at ~4% cost;
conformal calibrated abstention; semantic entropy for hallucination detection;
minority-veto judge ensembles where simple majorities fail. Sources:
`references/verified-grounding.md`.

## Use when

- Deciding how much inference compute a question deserves before answering.
- Verifying claims, citations, quotes, numbers before asserting them.
- Answering high-stakes questions (research, legal-adjacent, medical-adjacent).
- Controlling inference cost across many queries or an agent fleet.
- Wiring verification tools into an agent via MCP.
- Gating releases on golden-set evals; grading answer hygiene.

## Install

```bash
# pin the CLI to a reviewed version — never @latest in security-sensitive installs
npx clawhub@0.23.3 install @orionshaowswmw/inference-expert-agents
```

## Quick start

```bash
python3 tools/triage.py --text "Prove X and derive Y"          # F1
python3 tools/deliberate.py --difficulty hard --budget-tokens 3000
python3 tools/selfcheck.py --claim "..." --samples "a||b||c"   # F8/F9
python3 tools/grounding_gate.py --text ans.md --evidence-file ev.json
python3 tools/inference_scorecard.py --text-file ans.md --difficulty hard
```

Then follow `SKILL.md`: triage → plan → execute the ladder → verify → certify.

## 🔐 Permissions

- **Files read:** only files explicitly passed to the tools (`--text-file`,
  `--evidence-file`, `--labels-file`, …). No other file access.
- **Files written:** nothing by default. Stateful tools (`cache_kit`, `memory_kit`,
  `ladder_trace`, `eval_regression`, `retrieval`, `selfimprove`) are strictly opt-in: they refuse stateful
  operations unless you pass `--db PATH` (0600 enforced on every write and load — loose
  files are repaired). State may contain prompt text; keep the path private. Corrupt state files are refused with an error and left untouched — never silently reset. Selftest uses
  `mktemp -d`, cleaned on exit.
- **Network:** none. All processing is local.
- **Binaries:** `python3` (standard library only — no pip installs).
- **System calls:** none beyond normal process execution.

## 🔒 Security & Privacy

- **Data read/sent:** only the text you pass to the tools; nothing is
  transmitted anywhere.
- **Secrets:** none used, stored, or logged.
- **Sandboxing:** the self-test suite runs inside a throwaway `mktemp -d`
  sandbox and deletes it on exit.
- **Risks & mitigations:** heuristics, not formal guarantees — the gates catch
  the common failure classes but a passed check is not truth. Review `SKILL.md`
  before installing, per ClawHub convention.

## ✅ Verification hash

```
sha256(SKILL.md) = 7162588b6cf8e711de0737475929832119893245557b82694f29f212d02f78f7
```

Check after install:

```bash
# integrity check on THIS skill's own installed copy (no other skill is read)
sha256sum skills/inference-expert-agents/SKILL.md
```

## Self-test

```bash
bash skills/inference-expert-agents/scripts/selftest.sh
```
