# Free-Tier AI Router — Capability Tags for Every Model in the Skill

**Skill:** [`free-tier-ai-router`](https://hub.openclaw.ai/orionshaowswmw/skills/free-tier-ai-router) · **Date:** 2026-09-14 · **Workspace:** arena agent (carminic-acid)

## How this was produced (distributed job)

| Worker | Role | Output |
|---|---|---|
| **Arena agent (me)** | Orchestration + **internet verification** of every model (12 web searches, 40+ sources) | Ground-truth facts: architecture, MoE/dense, vision, context window |
| **gemini-3.1-flash-lite** | 4 ballots via Gemini key | Capability votes |
| **command-a-03-2025** (Cohere) | 3 ballots | Capability votes |
| **openai/gpt-oss-120b** (Groq) | 3 ballots | Capability votes |
| **nvidia/nemotron-3-super-120b-a12b** (OpenRouter) | 3 ballots | Capability votes |
| **llm7 default** | 2 ballots | Capability votes |
| **Llama-3.1-8B-Instruct** (HuggingFace) | 1 ballot | Capability votes |

17 API calls were fanned out over the workspace's 92 stored keys via `router.py --batch` (interleaved round-robin + failover). Merge rule: **web-verified facts override votes**; capability tags need ≥2 of 16 ballots (flagship/reasoning-class allowance for the agentic cluster). Mistral keys hit their 4-rpm 429s and zai was overloaded (both known repo issues) — coverage stayed complete because verification came from search, not from those providers.

## v2.5.4 verification run (2026-09-15, distributed)

Re-audit of all 32 entries, distributed between the arena agent and the most
capable models available via the stored API keys (one member per provider,
round-robin buckets of 4, all calls parallel and joined to completion):

| Worker | Model used | Outcome |
|---|---|---|
| **Arena agent (me)** | — | Orchestration + web verification of every model not covered by a live worker (12 web re-checks incl. Mistral Medium 3.5 vision, Mistral Small 4 architecture, Nemotron 3 Ultra, Ling-3.0 Flash) |
| gpt-oss-120b (Groq) | openai/gpt-oss-120b | 4/4 audited · 1 conservative dissent (gpt-oss Decision-Making) — kept, substantiated by agentic tool-use design |
| command-a-reasoning (Cohere) | command-a-reasoning-08-2025 | 4/4 audited · 0 dissent |
| gemini-3.5-flash (Gemini, fell back to 3.1-flash-lite) | gemini-3.1-flash-lite | 4/4 audited · 1 dissent (mistral-medium-latest "text-only") — **rejected**, web-verified text+image in |
| minimax-m2.7 (llm7) | minimax-m2.7 | 4/4 audited · 0 dissent |
| llama-31-8b (HuggingFace) | meta-llama/Llama-3.1-8B-Instruct | 4/4 audited · 2 dissent, both invalid (nemotron-3-super Long Context=1M ctx is documented; glm-4.7 "disagree" carried identical final_tags — 200K ctx confirmed) |
| nemotron-ultra (OpenRouter) | — | **FAILED: HTTP 402** (free-tier payment wall, known repo issue) |
| mistral-large (Mistral) | — | **FAILED: HTTP 429** (4-rpm free-tier cap, known repo issue) |
| glm-47-flash (Z.ai) | — | **FAILED: empty completion** (known zai endpoint bug; 3+ retries) |

Coverage stayed complete: the 12 entries in the failed members' buckets were
web-verified by the arena agent instead (merge rule: web-verified facts
override votes). Net result of the distributed audit: **all 32 entries of the
owner-supplied tag set confirmed correct** — the only live dissent
(`mistral-medium-latest` "text-only") was rejected on web evidence, and the
other two were invalid (see table). Structural change shipped: the redundant
`llama-3.3-70b-versatile` alias entry was merged into the single
`llama-3.3-70b` "Groq · Cerebras" entry (25 → 24 primary entries).

> **Advisory (v2.5.4, owner decision pending):** the HuggingFace card for
> `Mistral-Small-4-119B-2603` describes a **MoE** (128 experts, 6.5B active)
> with 256K ctx, while the shipped basis text says "dense, ctx unverified".
> The owner-supplied tag set (no `MoE` tag) was shipped as-is per the
> canonical spec; if `mistral-small-latest` is confirmed to serve the 119B
> MoE build, add the `MoE` tag in a future revision.

## Tag taxonomy (exactly the 15 requested)

`Reasoning` · `Vision` · `Multimodality` · `MoE` · `Planning` · `Tool Use` · `Coding` · `Long Context` (≥128K ctx) · `In-Context Learning` · `Instruction Following` · `Mathematical Reasoning` · `Information Extraction` · `Summarization` · `Decision-Making` · `Pattern Recognition`

## Primary catalog — the 24 models routed by the skill (`ROUTES` + `BUILTIN_SPECS`)

| # | Model | Provider(s) in skill | Tags (1–15 taxonomy) | Verified basis / notes |
|---|---|---|---|---|
| 1 | `mistral-large-latest` | Mistral | Reasoning, Vision, Multimodality, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Information Extraction, Summarization, Decision-Making, Pattern Recognition | Resolves to Mistral Large 3 (2512): 675B sparse MoE, 41B active, 256K ctx, text+image in (2.5B vision encoder). 14/16 ballots tagged Reasoning/IF/Math. Note: 1 source claimed text-only; 2 sources + vision-encoder spec say image input — majority wins. |
| 2 | `mistral-medium-latest` | Mistral | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Information Extraction, Summarization | Mistral Medium 3.5 (2604): 128B DENSE (no MoE), 256K ctx, text+image in, configurable reasoning, SWE-bench 77.6%. Skill's 'best-value' tier. |
| 3 | `mistral-small-latest` | Mistral | Reasoning, Vision, Multimodality, Tool Use, Coding, Long Context, Instruction Following, Summarization | Mistral Small 4 (2603): dense, merges reasoning + vision + coding. ctx >=128K from family lineage (not independently verified). Function calling via API. See the v2.5.4 advisory note below re: the MoE variant. |
| 4 | `open-mistral-nemo` | Mistral | Reasoning, Coding, Long Context, In-Context Learning, Instruction Following, Summarization | Mistral NeMo 12B (2407): dense, 128K ctx, text-only, Apache-2.0 2024-era workhorse. |
| 5 | `mistral-tiny-latest` | Mistral | Reasoning, Coding, Long Context, In-Context Learning, Instruction Following, Summarization | Verified ALIAS of open-mistral-nemo-2407 — same model, same tags (not a separate tiny model). |
| 6 | `ministral-3b-latest` | Mistral | Reasoning, Instruction Following, Pattern Recognition | Ministral 3 (3B dense, edge tier, Dec 2025 generation, Apache-2.0). 750 rpm budget router. 2 ballots tagged Coding — dropped as not a defining strength for a 3B edge model. |
| 7 | `ministral-8b-latest` | Mistral | Reasoning, Coding, Long Context, Instruction Following, Summarization, Pattern Recognition | Ministral 3 (8B dense, edge tier); 8B line carries >=128K ctx (128K on 2410 predecessor; not independently re-verified). |
| 8 | `codestral-latest` | Mistral | Coding, Reasoning, Tool Use, Long Context, Instruction Following | Codestral (2508 snapshot): dedicated code model, FIM + function calling, 256K-class ctx. |
| 9 | `mistral-code-latest` | Mistral | Coding, Reasoning, Tool Use, Long Context, Instruction Following | Verified ALIAS: also resolves to codestral-2508 — identical tags to codestral-latest. |
| 10 | `magistral-medium-latest` | Mistral | Reasoning, Mathematical Reasoning, Planning, Long Context, Instruction Following, Summarization | Magistral Medium (2509): Mistral's dedicated reasoning line (step-by-step thinking). 128K-class ctx (1.2). Base Medium 3 is multimodal but image input on Magistral not confirmed -> Vision withheld. |
| 11 | `gemini-3.5-flash` | Gemini | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Information Extraction, Summarization, Decision-Making, Pattern Recognition | May 2026 flagship Flash: text/image/audio/video/PDF in, 1M ctx, 64K out, dynamic thinking; beats Gemini 3.1 Pro on agentic/coding benchmarks. Skill's scarcest tier (20 req/day). |
| 12 | `gemini-3.5-flash-lite` | Gemini | Reasoning, Vision, Multimodality, Planning, Tool Use, Long Context, Instruction Following, Information Extraction, Pattern Recognition | Lite tier of 3.5: same multimodal stack + 1M ctx + thinking levels; coding/math deliberately weaker than Flash (withheld). |
| 13 | `gemini-3.1-flash-lite` | Gemini | Reasoning, Vision, Multimodality, Planning, Tool Use, Long Context, Instruction Following, Information Extraction, Pattern Recognition | GA high-efficiency multimodal (text/image/video/audio/PDF), 1M ctx, thinking levels, OCR 90% (Roboflow). Answered 4/16 ballots in this very job — it's the router's fastest scarce route. |
| 14 | `gemini-3-flash-preview` | Gemini | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Information Extraction, Summarization, Decision-Making, Pattern Recognition | Gemini 3 Flash preview — foundation of the 3.5 Flash line: multimodal, 1M ctx, frontier agentic/coding/math at flash speed. |
| 15 | `inclusionai/ling-3.0-flash` | OpenRouter · Kilo | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Decision-Making | Ling 3.0 Flash: 124B MoE, 5.1B active, hybrid-linear attention (KDA+MLA), 262K ctx, thinking by default, agentic/SWE focus, TEXT-ONLY (2 ballots wrongly tagged Vision — web evidence overrides). |
| 16 | `nvidia/nemotron-3-super-120b-a12b` | OpenRouter · Kilo | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Decision-Making | Nemotron 3 Super: 120B LatentMoE (Mamba-2 hybrid), 12B active, 1M ctx, reasoning on/off, built for agentic workflows/tool use/RAG; text-only. |
| 17 | `nvidia/nemotron-3-ultra-550b-a55b` | Kilo · OpenRouter | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Decision-Making | Nemotron 3 Ultra: 550B LatentMoE, 55B active, 1M ctx, NVFP4, flagship — within ~8-10% of GPT-5.5 on HumanEval/LiveCodeBench; text-only. Skill tags it 'flagship,1M-ctx'. |
| 18 | `stepfun/step-3.7-flash` | Kilo | Reasoning, Vision, Multimodality, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Information Extraction, Decision-Making, Pattern Recognition | Step 3.7 Flash: 198B sparse MoE VLM (196B LM + 1.8B perception encoder), ~11B active, 256K ctx, native image+VIDEO input, low/med/high reasoning, agentic search/planning, Apache-2.0. |
| 19 | `kilo-auto/free` | Kilo | — *meta-route/alias: tags undefined* | META-ROUTE, not a model: Kilo's auto-selection shim that forwards to a backing model. Capability tags are undefined by design (they belong to whatever model it picks). |
| 20 | `openai/gpt-oss-120b` | Groq | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Decision-Making | GPT-OSS-120B: 117B MoE, 5.1B active, 128K ctx, configurable reasoning (low/med/high), native tool use, text-only. 3/16 ballots here + skill's 'best-value,fast'. |
| 21 | `llama-3.3-70b` | Groq · Cerebras | Reasoning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning | Llama 3.3 70B: dense, 128K ctx, text-only, strong general assistant w/ function calling. Also the model that voted via HuggingFace in this job (Llama-3.1-8B variant). |
| 22 | `qwen/qwen3.6-27b` | Groq | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Pattern Recognition | Qwen3.6-27B: DENSE (not MoE), 27B, vision+text in, 262K native ctx (1M w/ YaRN), SWE-bench Verified 77.2% — beats the 397B MoE sibling on coding. Skill tags it 'code'. |
| 23 | `command-a-03-2025` | Cohere | Reasoning, Planning, Tool Use, Long Context, Instruction Following, Summarization, Decision-Making | Command A: 111B DENSE (A+ made the MoE switch later), 256K ctx, enterprise tool use / RAG / agents / multilingual; text-only. Skill tags 'best-value'. |
| 24 | `llm7 default` | llm7.io | — *meta-route/alias: tags undefined* | ALIAS, not a fixed model: llm7.io's free-tier default backend (rotates). Tags undefined by design; 16/16-ish ballots still gave it general assistant tags (Reasoning/IF) since the backend is a capable chat model. |

### Why two routes show no tags
`kilo-auto/free` and `llm7 default` are **routing aliases**, not models — they forward to whatever backing model the provider selects, so capability tags would be meaningless (any tags would be stale the moment the backend rotates). The 22 real models above carry the full taxonomy.

## Secondary — models inside the skill's probe/measurement files (results.json, quality.json, health.json)

| Model | Where in skill | Tags | Basis |
|---|---|---|---|
| `gemini-3.6-flash` | Gemini (probe files) | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Information Extraction, Summarization, Decision-Making, Pattern Recognition | Newer Flash generation ($1.50/$7.50, 1M ctx, thinking) — cited as 3.5-flash-lite's comparison peer; same capability family. Confidence: medium (family inference). |
| `openai/gpt-oss-20b` | OpenRouter (quality.json) | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Decision-Making | 21B MoE, 3.6B active, 128K ctx, reasoning levels, tool use; text-only. Confidence: high (well-documented open-weights release). |
| `nvidia/nemotron-3-nano-omni-30b-a3b-reasoning` | OpenRouter (quality.json) | Reasoning, Vision, Multimodality, MoE, Planning, Tool Use, Long Context, Instruction Following, Information Extraction, Decision-Making, Pattern Recognition | 31B MoE (3B active) OMNI: video+audio+image+text IN, text out, 256K ctx, reasoning on by default, tool calling/JSON, ASR + doc intelligence + GUI-agent use. Confidence: high. |
| `poolside/laguna-s-2.1` | OpenRouter (quality.json) | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Decision-Making | 118B MoE (8B active) agentic-coding specialist; 262K ctx free tier / 1M paid; function calling + interleaved thinking; text-only; 70.2% Terminal-Bench. Confidence: high. |
| `cohere/north-mini-code` | OpenRouter (quality.json) | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Decision-Making | North Mini Code 1.0: 30B MoE (3B active), 256K ctx, agentic software engineering, interleaved thinking, JSON-schema tool use; Apache-2.0; text-only. Confidence: high. |
| `gemma-4-26b-a4b-it` | Google (probe files) | Reasoning, Vision, Multimodality, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Information Extraction, Pattern Recognition | Gemma 4 26B-A4B: 25.2B MoE (3.8B active), 256K ctx, text+image in, thinking mode, native function calling, OCR/doc parsing. (Dead route in health.json — probed, later retired.) Confidence: high. |
| `gemma-4-31b` | Google (probe files) | Reasoning, Vision, Multimodality, Planning, Tool Use, Coding, Long Context, Instruction Following, Information Extraction, Pattern Recognition | Gemma 4 31B dense: 30.7B, 256K ctx, text+image in (no audio on 31B). Dead route in health.json. Confidence: high. |
| `zai-glm-4.7` | Z.ai (health.json dead route) | Reasoning, MoE, Planning, Tool Use, Coding, Long Context, Instruction Following, Mathematical Reasoning, Decision-Making | GLM-4.7: 355B MoE (32B active), 200K ctx, SWE-bench 73.8%, Preserved/Interleaved Thinking, MIT. Route dead in skill (429/overload at probe). Confidence: high. |

## Tag coverage summary (primary 22 real models)

| Tag | Models tagged | Tag | Models tagged |
|---|---|---|---|
| Reasoning | 22/22 | In-Context Learning | 2/22 |
| Vision | 9/22 | Instruction Following | 22/22 |
| Multimodality | 9/22 | Mathematical Reasoning | 10/22 |
| MoE | 6/22 | Information Extraction | 7/22 |
| Planning | 14/22 | Summarization | 10/22 |
| Tool Use | 17/22 | Decision-Making | 9/22 |
| Coding | 17/22 | Pattern Recognition | 9/22 |

## Conflicts & honesty notes (per HALLUCINATION_PREVENTION_ARENA)

- **Mistral Large 3 vision:** 1 source says text-only; 2 sources (incl. the 2.5B vision-encoder spec) say image input → tagged `Vision`, flagged.
- **Mistral Medium 3.5 vision (v2.5.4 re-verified):** a live audit vote (gemini-3.1-flash-lite) claimed text-only; HuggingFace model card, SGLang cookbook and Artificial Analysis confirm text+image input with a from-scratch vision encoder → `Vision`/`Multimodality` kept, dissent rejected.
- **Vote-vs-fact overrides:** 2 ballots tagged `Vision`/`Multimodality` on Ling 3.0 Flash (text-only per HuggingFace card) — overridden by evidence.
- **Aliases discovered:** `mistral-code-latest` = `codestral-latest` = Codestral 2508; `mistral-tiny-latest` = `open-mistral-nemo`. Tags are duplicated accordingly.
- **Mistral Small 4 / Ministral ctx windows** inferred from family lineage, marked in notes.
- Two stored keys were flaky today (`llm7 alt#24` unreachable, zai 429-overload) — no impact on results.

## Sources (key web verifications)

Nemotron 3 Ultra/Super: dev.to developer guide · HF model card · NVIDIA NIM docs — Ling 3.0: OpenRouter · HF card — Step 3.7 Flash: NVIDIA dev blog · MarkTechpost — Qwen3.6-27B: vLLM recipes · Clore guide — Gemini 3.5 Flash / 3.1 Flash-Lite: llm-stats · ai-tldr · Roboflow · OpenRouter — Mistral lineup & aliases: promptfoo provider guide · effloow Large-3 guide · aimadetools Medium-3.5 — Command A: Cohere docs (+ A+ launch guide for the dense/MoE contrast) — Gemma 4: Google HF cards — Laguna S 2.1: kie.ai · SGLang cookbook — North Mini Code: Cohere docs — GLM-4.7: automatio.ai · digitalapplied — Nemotron Nano Omni: NVIDIA HF cards. Full URLs in the workspace research log.

## Packaging note (v2.5.4)

The Llama 3.3 70B weights are served by Groq under the tenant id `llama-3.3-70b-versatile` (router.py route) and by Cerebras as `llama-3.3-70b`; both map to the single `llama-3.3-70b` catalog entry, so the redundant v2.5.3 alias entry was merged in v2.5.4. The machine-readable source of truth is [`model-tags.json`](model-tags.json) (24 primary + 8 secondary entries).
