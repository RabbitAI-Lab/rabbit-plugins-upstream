# Verified Grounding — facts this skill is built on

All facts below were verified against primary sources during workspace research
sessions (Sept 2026). Sources listed; do not cite beyond these without
re-verification (see SKILL.md Verification Rules).

## Inference-time compute works

- **DeepSeek-R1** (Jan 2025, GRPO reinforcement learning): AIME accuracy
  15.6% → 71% via extended chain-of-thought at inference; 86.7% with majority
  voting — matching OpenAI o1-class models. Source: DeepSeek-R1 release;
  analyses: introl.com inference-time-scaling review; Turing Post TTC guide.
- **Self-consistency** (Wang et al., ICLR 2023): sampling multiple
  chains-of-thought and majority-voting reduces variance; used in the R1
  majority-voting result above.
- **AlphaProof + AlphaGeometry 2** (Google DeepMind): solved 4/6 problems at
  IMO 2024, 28/42 points = silver-medal level, including the hardest problem
  (P6, solved by only 5 human contestants); proofs verified in the Lean formal
  system. Peer-reviewed: Nature s41586-025-09833-y (2025).
  Lesson: LLMs perform best as policy generators for a verified search process.

## Inference cost is the dominant spend

- OpenAI 2024 inference spend ≈ $2.3B ≈ 15× the training cost of GPT-4
  (industry analyses). Analysts project inference ≈ 75% of total AI compute
  by 2030. Source: introl.com inference-time scaling review (Dec 2025).

## Serving-speed facts (for agents that control their own stack)

- **PagedAttention / vLLM** (Kwon et al., SOSP 2023, arXiv:2309.06180,
  UC Berkeley): the abstract verifies "near-zero waste in KV cache memory" and 2–4× throughput vs
  FasterTransformer/Orca at equal latency. The 60–80% → <4% figures are paper-body
  measurements, not abstract-verified.
- **Speculative decoding** (Leviathan, Kalman, Matias — Google, ICML 2023,
  arXiv:2211.17192): 2–3× wall-time speedup with provably unchanged outputs;
  NVIDIA TensorRT-LLM reports 2.6–3.5× on Llama 3.3 70B (H200).
  Independent equivalent: Chen et al. (DeepMind), speculative sampling, 2023.

## Hallucination is endemic — verification is mandatory

- In workspace-verified distributed-research runs (3 separate multi-provider
  swarms, Sept 2026), every specific citation produced by cloud LLM workers
  that was checked turned out fabricated or wrong (plausible authors, real
  journals, non-existent DOIs/PMIDs). Verified instances: fake
  "PagedAttention — Xiao et al., Meta AI"; fake i.p.-BITC GDM/nephropathy
  studies; fake Fisher 1922 dating; multiple fabricated biomedical DOIs.
- Consequence encoded in SKILL.md: citations are guilty until verified against
  a primary source in the same session.

## Calibrated uncertainty & abstention

- **Conformal prediction** provides distribution-free coverage guarantees and
  is deployed in industry (Air Liquide demand forecasting w/ PUNCC, UAI/PMLR
  v179 2022; QSAR drug discovery; ASR uncertainty). Basis for the skill's
  abstention thresholds.
- **Aleatoric vs epistemic uncertainty** (Kendall & Gal, NeurIPS 2017) — the
  standard framework for marking what uncertainty *is*.

## Causal-inference tooling (for agents doing decision analysis)

- EconML (Microsoft; adopted at Microsoft/TripAdvisor/Uber), CausalML (Uber; arXiv:2002.11631, 2020 — no OpenAlex record was found for a
  "SoftwareX 2022" article under that title, so cite the preprint), DoWhy (Microsoft/PyWhy) — production-grade causal inference
  libraries; the skill's "compute, don't guess" rule extends to causal claims.

## v2.0.0 additions (verified Sept 2026)

- **Judge ensembles**: arXiv 2510.11822 "Beyond Consensus" — LLM validators
  rarely reject (agreeableness); the abstract states simple-majority true-negative rate <25% while minority-veto
  ensembles reach ~96% TPR (the finer 19.2% / 95.5% / 30.9% figures are paper-body
  numbers, not abstract-verified — treat them as indicative); a regression correction
  from a small ground-truth set fixes validator bias (→ judge_panel
  minority-veto + weighted modes). arXiv 2609.12002 — judge accuracy tracks
  examinee accuracy (Pearson r ≥ 0.90); stronger examinees judged more leniently
  (r ≥ 0.83 — the correlation is POSITIVE: capability and leniency rise together.
  **v3.0.0 fix:** previously printed "r ≤ −0.83", inverting the source); label-free weighted majority voting from inter-judge disagreement
  tracks oracle error within 0.5pp. arXiv 2508.02994 (Agent-as-a-Judge survey) —
  committee frameworks (ChatEval, DEBATE, CourtEval, MAJ-EVAL) beat single
  judges; the 12-bias checklist consolidates documented judge biases (the named frameworks
  ChatEval/DEBATE/CourtEval/MAJ-EVAL are surveyed in the paper body, not the abstract) (position,
  style, bandwagon, authority, self-preference, length, sentiment,
  fabricated-citation, sycophancy, confirmation, anchor, capability-leniency).
- **Calibrated abstention**: conformal prediction (Vovk; Angelopoulos &
  Bates 2023 tutorial) — finite-sample distribution-free guarantees; the
  Hoeffding upper bound err + sqrt(ln(1/δ)/2n) is conservative at small n;
  Conformal Inference for Confidence (CIC-style) calibrates answer-level
  abstention thresholds; UCCI-style escalation gates abstain only after trying
  stronger models.
- **Cost**: FrugalGPT (Chen et al., Stanford, arXiv:2305.05176) — cascades of
  cheap→expensive models match GPT-4 quality at up to 98% cost reduction (abstract-verified figure;
  **v3.0.0 fix:** previously stated 96%); RouteLLM (arXiv:2406.18665) — router-trained cascades reduce cost by over 2× without
  compromising quality (abstract); the 2.4× / 90%-quality pairing is paper-body; semantic caching — SCALM (arXiv:2406.00025) and A Generative Caching System for
  LLMs (arXiv:2503.17603). GPTCache is an OSS library with no arXiv paper; do not
  attach an id to it. **v3.0.0 fix:** the previous text cited "GPTCache
  (arXiv:2303.13537)" — that id is *Toxicity and Cultural Entrenchment in
  Peer-Production Communities*, verified via export.arxiv.org. A fabricated id
  that survived two published releases; speculative decoding 2–3× (Leviathan et al., above).
- **Hallucination detection**: SelfCheckGPT (Manakul et al., EMNLP 2023,
  arXiv:2303.08896) — sampling consistency detects black-box hallucinations;
  semantic entropy (Farquhar et al., Nature 2024) — entropy over meaning
  clusters predicts errors; FactSelfCheck — n-gram/graph-level fact scoring;
  FActScore (Min et al., EMNLP **2023**, doi 10.18653/v1/2023.emnlp-main.741,
  arXiv:2305.14251) — % of atomic factual claims supported by
  retrievals (→ scorecard atomic_claim_support).
- **Grounded generation & gates**: RARR/ReClaim-style attribution + revision;
  CiteGuard-style citation grounding; DSPy Assertions (arXiv:2312.13382) — LM Assertions with automatic self-refinement
  (abstract); the Assert/Suspend-Suggest naming is paper-body terminology (→ tool_guards
  retry semantics). Structured-outputs/strict-schema validation as the contract
  for machine-checkable verdicts.
- **Debate**: Du et al. 2023 (arXiv:2305.14325) — multiagent debate improves
  factuality via critique-and-revise; A-HMAD (heterogeneous agents) reports
  ~18% hallucination reduction on TruthfulQA; documented caveat: all-wrong
  consensus is possible — verify load-bearing facts regardless (→ debate.py
  contested-consensus verdict).
- **Deep research**: plan→search→read→synthesize→verify loops with explicit
  stopping rules and source tiering (primary/secondary/tertiary); test-time
  scaling law: more inference compute → better, but verification beats
  generation per token.
- **Memory**: Reflexion (Shinn et al. 2023, arXiv:2303.11366) — verbal
  self-reflection stored and reused across tasks; ExpeL — experience-derived
  rules-of-thumb; Voyager (Wang et al. 2023) — skill library growth;
  documented failure mode: *accidental* forgetting (→ memory_kit deliberate
  forgetting).
- **Agent infrastructure**: Inspect AI (UK AI Security Institute) —
  dataset+solver+scorer evals, sandboxed tool execution (Docker/K8s/Modal),
  tool-call approvers, transcripts (→ sandbox_drill, approval-gate policy);
  Model Context Protocol (Anthropic, spec 2024-11-05) — stdio JSON-RPC tool
  servers (→ mcp_server.py); continuous-eval practice (LangSmith/Langfuse
  model): golden sets, regression gates on every change, human annotation
  queues for failures.

## v2.1.0 additions (verified Sept 2026)

- **Chain of Draft** (Xu et al., arXiv:2502.18600): ≤5-words-per-step reasoning matches/beats
  CoT accuracy with as little as 7.6% of tokens (~80% reduction); documented limitation: models
  under ~3B fail it — gate by tier (portability.py), A/B before adoption.
- **LLMLingua** (Jiang et al., EMNLP 2023, arXiv:2310.05736) + LongLLMLingua (ACL 2024):
  up to 20x prompt compression "with little performance loss" (abstract); the ~1.5pt
  figure is paper-body; RAG variant cut long-context cost 94%
  while IMPROVING accuracy up to 21.4%; worthwhile only above ~500 input tokens. compress.py is
  an honest lexical approximation (no model), hence conservative thresholds.
- **Chain-of-Verification** (Dhuliawala et al., ICLR 2024, arXiv:2309.11495): draft → plan
  verification questions → answer them FACTORED (without seeing the draft) → revise. Wikidata
  precision 0.17→0.36; hallucinated entities 2.95→0.68 per response; FActScore 55.9→71.4;
  MultiSpanQA +23% F1. Factored execution is the load-bearing detail.
- **Instruction retrieval for small models**: arXiv:2510.13935 (Alkiek et al., *Big
  Reasoning with Small Models: Instruction Retrieval at Inference Time*) — retrieval at
  inference yields consistent gains for models of at least 3B parameters. **v3.0.0 fix:**
  this entry previously claimed "each log-unit of prompt tokens costs ~-8pp accuracy",
  which is not in the abstract and is not this paper's result; the figure was removed.
  Keep the >=3B threshold (abstract-supported); treat any per-log-unit penalty as unverified.
- **Structured outputs**: strict JSON during reasoning suppresses thinking — reason freely, then
  emit the structured verdict; schemas models comply with are flat, short-enum, described
  (production practice, 2025-2026).
- **Throughput levers**: Medusa (arXiv:2401.10774) 2.2-3.6x; EAGLE-2 2-3x (2026 production
  default); vanilla speculative decoding 1.5-2x provably exact; INT4 quantization -75% cost at
  1-2% quality loss, INT8 -50% at <1%; continuous batching 5-10x throughput (batching 32
  requests ≈ -85% per-token cost); PagedAttention KV waste 60-80%→<4%; prefix caching rewards
  byte-stable system prompts; grammar-constrained decoding neutral-or-faster on JSON.
- **TextGrad** (Yuksekgonul et al., arXiv:2406.07496; Nature 2025): LLM textual feedback as
  "gradients" optimizes prompts/rules; complementary to DSPy compile-time optimization.
  selfimprove.py adopts the loop but GATES every amendment on measured golden-set delta.
- **Wilson score interval** (Wilson 1927): lower-bound ranking for small-sample win rates —
  the standard bandit-style ranking for rules with few trials.

## v3.0.0 citation audit (Sept 2026) — method, so it is reproducible

Every arXiv id cited anywhere in this skill was re-fetched from
`export.arxiv.org/api/query` and every DOI/title from `api.openalex.org`, and each
numeric claim was then checked against the paper's own abstract. Result: 18/18 ids
resolve, but **12 attribution errors were found and corrected above**, including one
fabricated id (arXiv:2303.13537 attributed to GPTCache; it is a different paper
entirely) and one inverted correlation sign.

Reproduce it with the tool this audit produced:

```bash
python3 tools/citecheck.py scan  --file references/verified-grounding.md --strict
python3 tools/citecheck.py check --citations-file claims.json --strict
```

Two lessons are now encoded as behaviour, not prose:

1. **A resolvable id is not a correct citation.** All 18 ids resolved; 12 were
   still wrong about what they point at. `citecheck scan` proves existence,
   `citecheck check` proves attribution — you need both.
2. **Abstract-verified ≠ paper-verified.** Numbers that appear only in a paper's
   body are now labelled "paper-body" above. An abstract is the cheapest primary
   source that can be fetched in-session, so it is the floor, not the ceiling.
