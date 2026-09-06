# Evidence — arena-turn-accelerator

Every load-bearing claim in this skill and where it comes from. Verified 2026-09-06.

## Compaction speeds up prefill (mechanism 1)

- **In-repo measurement (primary):** same question, Qwen2.5-0.5B, 2-core box:
  274→32 chars ⇒ cold 3.47s→1.02s (**3.4×**), warm 1.89→1.07s (1.77×); mixed-set
  honest average 1.46× warm. Prefill cost is approximately linear in prompt
  tokens on CPU (llama.cpp prompt-processing benchmarks); compaction removes
  only ceremony, so quality is preserved — see the `--verify` gate below.
- **Scope limit (honest):** cannot help with server queueing or network latency.

## Why the question goes first (mechanism 1 + hard rule 1)

- Liu et al., **"Lost in the Middle: How Language Models Use Long Contexts"** (2023,
  Stanford/Samaya AI): U-shaped attention — accuracy highest for information at the
  **start or end** of context, dropping ~15–30 points in middle positions
  (multi-doc QA + key-value retrieval, GPT-3.5/4, Claude, open models).
- Mechanical consequence: hoist the question to line 1; put the output contract
  next to it; bury nothing important mid-document.

## Why anti-sycophancy is a shipped feature, not a preference (mechanism 5)

- **OpenAI GPT-4o incident, 2025-04-25:** an update over-weighting short-term
  👍/👎 feedback produced population-level sycophancy (endorsing delusions,
  harmful plans); publicly acknowledged and **rolled back 2025-04-28/29**, with
  an expanded May 2025 postmortem treating sycophancy as launch-blocking.
- Sharma et al., **"Towards Understanding Sycophancy in Language Models"**
  (Anthropic, 2023; ICLR 2024): assistants systematically shift toward user
  views under pushback even against known facts → the spine's
  evidence-vs-pressure classifier exists precisely for this failure class.
- Discipline: the spine is **explicitly not contrarianism** — new evidence
  forces instant concession (measured in `scripts/spine.py` tests).

## Long-context degradation (mechanism 3 "zombie")

- Attention cost over history is superlinear in practice (quadratic prefills);
  quality falls as relevant instructions get buried ("Lost in the Middle",
  above). Detection uses *measured latency trend within the current model* plus
  size thresholds scaled to the real context window (v1.5 reviewers:
  gpt-oss-120b + Nemotron-550B, consensus), never a universal constant.

## Design sources

- Progressive disclosure / concise SKILL.md / machine contracts: Anthropic,
  "Agent Skills best practices" (docs.claude.com › agents-and-tools › agent-skills).
- Vault-based span protection + fixpoint-iteration: 5,000+ case property
  fuzzing in this repo (`tests/fuzz_fixpoint.py`), 13/13 mutation kills
  (`tests/mutate.py`), 155 model-check sequences, 196 cross-module pairs.
- CJK filler stripping deliberately omitted (two independent model reviews:
  regex false-positives on real content; needs token-aware compaction).
