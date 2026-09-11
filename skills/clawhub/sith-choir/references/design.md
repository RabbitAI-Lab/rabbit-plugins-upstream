# Design & Research Foundation — sith-choir 🦞

This skill packages a set of *validated* multi-model orchestration techniques
into one CLI. Nothing here is invented: each move cites the primary source.

## 1. Mixture-of-Agents (MoA) — `moa`, `harvest`
> Wang, Wang, Athiwaratkun, Zhang, Zou. *Mixture-of-Agents Enhances Large
> Language Model Capabilities.* arXiv:2406.04692 (2024). — MoA builds layers of
> LLMs: each agent sees the outputs of previous-layer agents and produces a
> refined answer. Key empirical results:
> - "Collaborativeness": a model produces better output when it sees other
>   models' outputs — **even when those outputs are lower quality** than its own.
> - MoA (open-source models only) beat GPT-4 Omni on AlpacaEval 2.0 (65.1% vs
>   57.5% LC win rate) and substantially outperform an LLM **ranker** that only
>   selects one answer.
>
> ⇒ `moa` runs N cheap/weak proposers in parallel, then a strong reasoning
> model **synthesizes** (rather than selects). This is the "Sith drains the
> choir: the best final text is more than any single singer produced."

## 2. Model cascades / FrugalGPT — `ask` → `escalate`
> Chen, Zaharia, Zou. *FrugalGPT: How to Use Large Language Models While
> Reducing Cost and Improving Performance.* arXiv:2305.05176 (TMLR 2024). — An
> LLM cascade sends each query to a cheap model first and escalates to a more
> expensive/capable one only when a scorer says the cheap output is unreliable.
> FrugalGPT matched GPT-4 with up to **98% cost reduction** (or beat it by ~4%
> at equal cost). Related: *Cost-Saving LLM Cascades with Early Abstention*
> (arXiv:2502.09054) shows cheap models may predict when escalation is needed.
>
> ⇒ `escalate` implements the rule the user asked for: **a model that is making
> mistakes must ask the best reasoning models.** Cheap primary answers with
> `CONF:`; below threshold or on repeated error signals (—force) the reasoning
> court takes over — mandatory, not optional.

## 3. LLM-as-a-Judge — `judge`, ledger rewards/punishments
> Zheng et al. *Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena.*
> arXiv:2306.05685 (2023). — Strong LLM judges agree ~80% with human
> preferences (≈ human–human agreement). Documented biases: **position,
> verbosity (longer≠better), self-enhancement** (a model grades itself kindly),
> limited reasoning on hard questions.
>
> ⇒ The skill uses several independent judges and takes the mean; the judge
> prompt forbids length/order favouritism; the authoring model is never its own
> sole judge; a "reference answer" can be supplied for objective tasks. The
> reward ledger operationalizes **reward for good answers, punishment for bad**
> across sessions (EWMA score, rewards, punishments, best).

## 4. Adaptive compute / verifiers — `harvest`
> Snell, Lee, Xu, Kumar. *Scaling LLM Test-Time Compute Optimally can be More
> Effective than Scaling Model Parameters.* arXiv:2408.03314 (2024). — Compute
> should be allocated per-prompt difficulty; easy prompts benefit from
> parallel sampling, hard ones from sequential revision + a verifier. A
> compute-optimal policy beat best-of-N by >4×; a small model + test-time
> compute can outdo a 14× bigger one.
>
> ⇒ `harvest` spends reasoning budget adaptively: cheap proposers (parallel
> sampling) when the question is easy, escalating to revision by the strongest
> model + judge verification when it is hard.

## 5. Weak-to-strong generalization — why strong aggregators win over weak proposers
> Burns et al. *Weak-to-Strong Generalization.* arXiv:2312.09390 (2023). Also:
> Lang, Sontag, Vijayaraghavan (arXiv:2405.16043) on **pseudolabel correction**
> and **coverage expansion**; Uzunoglu et al., *Trust Functions* (arXiv:2606.01000)
> on filtering weak supervision by trust score.
>
> ⇒ A strong model reading weak models' outputs can extract signal the weak
> models never encoded themselves. The aggregator prompt tells the lead model
> to *ignore quality issues and reuse the good reasoning*, matching the paper's
> advice that letting the student see weak reasoning beats hiding it.

## 6. Vision asymmetry — `vision`
> *Visual Reasoning Evaluation of Grok, DeepSeek Janus, Gemini, Qwen, Mistral
> and ChatGPT* (arXiv:2502.16428): measured — models differ hugely in vision
> ability; o1 led accuracy 82.5%, Gemini 2.0 Flash 70.8%; QVQ (Qwen-VL)
> strongest at abstaining (rejection accuracy 85.5%) when it cannot see well.
> Qwen2.5-VL (arXiv:2502.13923): docs, grounding, video, OCR; Zhipu GLM-4.5V:
> image/video/GUI understanding with grounding; Mistral Pixtral: images + docs;
> Moonshot Kimi K2.5 added native vision (MoonViT encoder) and Kimi K3 adds
> reasoning; Google Gemini is natively multimodal (image/audio/video/text).
>
> ⇒ The correct architecture for "a model without vision asks a model with
> vision to perform the job": keep text models on text; route images to members
> tagged `vision`; have vision members *abstain* when unsure (that behaviour is
> measurable, 2502.16428) and a reasoning model synthesizes the reports.

## Capability survey used for routing hints (as of Sep 2026)
Heuristic, id-based. Override with `"tags"` in your credentials file.

| Vendor/model family | vision | reasoning | notes (sources above) |
|---|---|---|---|
| Google Gemini (2.5→3.x flash/pro) | ✅ | ✅ | natively multimodal, huge context |
| OpenAI GPT-5.x/6 (Sol/Terra/Luna) | ✅ text+image in | ✅ effort knob | tiered pricing/reasoning |
| Anthropic Claude (Opus/Sonnet/Fable) | ✅ | ✅ | docs + screenshots |
| xAI Grok 4.x | ✅ | ✅ | image input |
| Qwen3-VL (Alibaba) | ✅ | ✅ | grounding, video, agentic (2502.13923) |
| Zhipu GLM-4.5V / GLM-5 | ✅ | ✅ | GUI/video/docs |
| Moonshot Kimi K2.5/K3 | ✅ | ✅ | native vision encoder + reasoning |
| Mistral Pixtral / devstral / codestral | Pixtral ✅ | devstral/codestral ✅ | coding/reasoning lane |
| Cohere Command A / Aya-Vision | aya-vision ✅ | Command A reasoning ✅ | |
| Meta Llama (3.3/4) | llama-4 partial | ✅ | via cloudflare/groq/hf |
| DeepSeek V4 / R1 | some VL | ✅ | strong open reasoning |

## Multi-key mesh (v1.1): every stored credential is a voice
This skill runs against a **fleet of API keys**, not one key per provider: the
credentials store carries `api_key` plus up to 17 `alt_api_keys` per provider
(the workspace holds 55 distinct keys across 10 providers). Each distinct key
becomes an independent voice with its own health record (`fleet.json`):
- a 429/5xx/401/403/402 cools *that key* for a backoff proportional to its
  failure count (401/403/402 get a 1h cooldown — they need human action);
- callers fail over across a provider's keys with bounded attempts (3), so a
  rate-limited 17-key account costs seconds, not minutes;
- cooldowns rotate load: after mistral k1–k4 were rate-limited in a live run,
  the next choir automatically sang on mistral#k5;
- **cross-provider help** is first-class: `escalate --helpmates gemini,llm7`
  composes the reasoning court from the *named* providers' keys, then tops up
  from other reasoning voices. This is the design consequence of the user's
  requirement that an openrouter/mistral-key model that needs help should use
  gemini/llm7 keys.
Key rotation policy mirrors the mature `tools/router.py` engine in this
workspace (per-key cooldowns, health-ordered pick, free-tier-aware model ids).

## v1.2 feature set — where each feature comes from
Distributed grounding: the skill's own choir (10 providers, 55 keys) was asked,
via `harvest` (propose→aggregate→judge, REWARD 10/10) and an escalation court of
5 providers, which features add the most value. The fleet's answers matched the
literature; each feature below maps to its citation.
- **`consensus` (self-consistency plurality/weighted vote)** — Wang et al.
  *Self-Consistency Improves Chain of Thought Reasoning* arXiv:2203.11171
  (sample diverse reasoning paths, plurality vote); weighted by confidence so a
  majority of weaker ballots cannot outweigh a strong one — *Confidence
  Improves Self-Consistency (CISC)* arXiv:2502.06233 and *Dynamic
  Self-Consistency* arXiv:2408.17017.
- **`refine` (judge→critique→revise loop)** — Shinn et al. *Reflexion*
  arXiv:2303.11366 (verbal self-reflection in episodic memory → better next
  attempt); *Scaling LLM Test-Time Compute* arXiv:2408.03314 (revision +
  verifier beats best-of-N). Guards against the review's anti-patterns: bounded
  rounds, `--budget`, critiques carry concrete judge reasons, ledger only on
  the final panel.
- **Answer cache & `--session` memory** — recommended by the fleet court
  (gemini lead) for cost and statefulness; matches framework practice
  (LangGraph durable state / memory; CrewAI memory). Cache is exact-match
  sha256 — deterministic repeats are served free, saving free-tier quota.
- **Token usage accounting + `--budget`** — FrugalGPT (arXiv:2305.05176) is a
  *cost*-aware cascade; per-key token capture (from provider usage reports) is
  the substrate for later price tables. `--budget` enforces a stop-before-next-
  stage guard once the provider-reported total exceeds the cap.
- **`runs`/`report` provenance, `--plan`, `--lane`** — observability and
  deterministic choice of voices; the fleet harvest ranked "provenance &
  reporting" and "dynamic budget caps & rate-limiting" in its top features.

## v1.3 improvements — evidence map (distributed grounding, round 3)
Round-3 research ran through the fleet itself (consensus/moa/escalate across
the stored keys) plus web grounding; every change maps to a source.
- **Reduce tokens per call** — prompt/context caching discounts are
  provider-side and automatic (Anthropic cached reads ~0.1x, OpenAI ~0.5x
  automatic with 1,024-token prefix minimum, Gemini implicit + explicit
  caches, ~0.1-0.25x; cache hits require a byte-identical prefix): the skill
  now (a) keeps the static system prompt byte-stable, (b) **parses cache-read
  tokens from each provider's usage shape** (OpenAI
  `prompt_tokens_details.cached_tokens`, Gemini `cachedContentTokenCount`,
  Anthropic `cache_read_input_tokens`) and excludes them from `--budget` and
  token totals, and (c) reports `cached=` per voice. System prompts were
  distilled, judge/verifier/vote micro-tasks got tight per-call output caps,
  aggregator inputs are trimmed (smaller prefill = fewer input tokens + lower
  TTFT), and `--session` context is budget-compacted (deterministic
  truncation, no extra model call). Fleet findings: cache first, cap outputs,
  trim verbose model speech, tighten max_tokens per stage.
- **Tokens/sec + latency** — fleet advice: parallelize independent sub-calls
  (judges/verifiers/proposals already run concurrently), keep micro-tasks on
  small/fast models with short output caps, and *measure*. The skill now
  times every call and reports avg ms + **tok/s per voice** in `report`, with
  latency in `runs` provenance. Groq/Cerebras are the fastest hosted lanes for
  proposal work (web benchmark evidence), which the fast-lane picker already
  prefers via tags.
- **Reduce hallucinations** — fleet ranking (highest ROI first):
  instruction-level fact-pinning & citation-forcing, grounding/abstention,
  verifier double-checks, disagreement triggers. v1.3 adds: an **abstention
  protocol** (proposers/voters may answer `UNKNOWN`; consensus drops
  abstentions and never asserts a guess; judges reward honest refusals),
  an **independent adversarial `verify`** round (2 voices, VERDICT
  PASS/FAIL/PARTIAL, any FAIL wins) wired to `ask --verify` and standalone,
  **near-tie arbitration** that only overrides when a reasoning arbiter
  explicitly picks one of the tied groups, and AGGREGATOR instructions that
  attribute disputed facts instead of inventing new claims.
- **Self-improvement** — a cheap offline eval loop: `calibrate` scores one
  voice per provider against a frozen 8-question set (facts/arithmetic/code,
  few-words answers), accumulates accuracy in `calibration.json` (0600), and
  `consensus` vote weights + `report` accuracy read it (clamped [0.2, 3.0])
  before falling back to the reward-ledger EWMA. Cost is operator-controlled
  (`--questions`, `--providers`, `--plan` shows the estimated call count).
- **Model compatibility / machine-readable** — single-file self-contained
  CLI, plaintext protocol, `--plan`/`--json` on every command (single JSON
  document; human banners never pollute stdout), exit-code contract
  (0 ok / 1 runtime / 2 usage / 3 selftest failure), `selftest` as the host
  readiness gate returning 3 on failure, and machine-readable SKILL.md
  frontmatter (`id`, `version`, `license`, `dependencies`,
  `host_compatibility`, `invariants`, `cli`). Per-provider usage/response
  shape variance is handled by shape-agnostic parsers covered by offline
  fixture tests.
- **Distributed debug pass (round 3)** — the debug protocol research
  (deterministic offline reproduction, provider contract fixtures, golden
  answers, structured observability) was applied: `selftest` grew fixture
  tests for every usage shape, abstention rules, verdict parsing, cropping,
  calibration scoring, weight fallbacks and session compaction; a reasoning
  moa audit of the new code found 9 candidate issues, of which the material
  ones were fixed (atomic 0600 state writes with no world-readable window,
  abstention tail threshold tightened, arbitration adoption gated on an exact
  group match, task-tuple padding in parallel_calls). Live smokes against the
  workspace fleet verified verify/ask --verify/calibrate/consensus/
  escalate/moa/session/report/runs end-to-end.

## Thematic note
"Let the Sith be the choir" = orchestration inversion: the *many* weak models
provide raw intelligence (voices), the *one* conductor model — plus its judge
panel — decides what is worth keeping and who gets rewarded or punished. It is
a division-of-labour pattern (propose → aggregate → verify), not a claim about
consciousness or harm. No copyrighted material is "sucked": models return their
own generations to the prompt context of another model, standard MoA practice.
