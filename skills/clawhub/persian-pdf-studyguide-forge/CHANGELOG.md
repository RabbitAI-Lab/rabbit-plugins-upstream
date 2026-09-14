# Changelog

## 1.5.1 (2026-08-26)

### Fixed

- `templates/providers.example.json` and the Ollama default base URL used the
  raw loopback address `http://127.0.0.1:11434`, which the ClawHub static
  analyser flags as `suspicious.install_untrusted_source`. Both now use
  `http://localhost:11434`; behaviour is unchanged.


## 1.5.0 (2026-08-26) — model-agnostic & agent-agnostic

Rebuilt the model layer so the skill produces the same intended result no
matter which AI model or which agent runtime drives it. Every quirk listed
below was reproduced against live provider responses, not assumed.

### Added

- **`scripts/model_adapters.py`** — a stdlib-only layer (urllib, no SDKs,
  Python 3.9+) speaking eight API dialects: `openai` (OpenAI, Groq, OpenRouter,
  Mistral, DeepSeek, Together, Fireworks, xAI, Z.AI, Cerebras, NVIDIA,
  Perplexity, LiteLLM, vLLM, LM Studio, llama.cpp server), `responses`
  (OpenAI Responses API), `gemini`, `anthropic` (`/v1/messages`, `x-api-key`,
  `anthropic-version`), `cohere` (`/v2/chat`), `ollama` (`/api/chat`), `hf`
  (HuggingFace router) and `mock` (deterministic, offline).
- **`scripts/forge.py`** — one entrypoint for every runtime with a frozen
  contract: exactly one JSON document on stdout, structured logs on stderr,
  stable exit codes (0 ok, 1 contract/QA, 2 usage, 3 deps, 4 no provider,
  5 interrupted), and `--stdin` JSON job objects. New commands `describe`,
  `doctor`, `selftest`, `compat`, `reproduce` alongside every pipeline stage.
- **Zero-configuration provider discovery.** Providers are resolved from
  `providers.json` (optional), then from whatever keys the host agent already
  exports, then local runtimes (`OLLAMA_HOST`, `LOCAL_OPENAI_BASE_URL`), then
  the offline mock. `--providers` is no longer required anywhere.
- **Self-healing capability probe.** Rejected parameters are parsed out of the
  provider's own error body, dropped, retried and remembered in
  `~/.cache/persian-pdf-studyguide-forge/capabilities.json`: `max_tokens` vs
  `max_completion_tokens`, fixed `temperature`, unsupported `seed`
  (including Pydantic `extra_forbidden` bodies from Mistral/vLLM),
  `response_format`/`json_schema`, missing system role, `top_p`, `stream`.
- **Model-retirement following.** A 404 that names a replacement model
  (observed live on Gemini) is parsed and the replacement is used automatically.
- **Reproducibility machinery**: `canonical_json`/`write_json` (sorted keys,
  stable indent), `stable_sort_items`, Persian-aware `content_key`
  (ezafe hamza, harakat, ZWNJ, digits, punctuation), `similarity`,
  `dedupe_items`, and `consensus_pick` with semantic grouping and vote ranking.
- **`reasoning_team_enrich.py --consensus N [--min-votes 2]`** — send the
  identical prompt to N different model families and keep only what they agree
  the source says.
- **Interoperability manifests**: `agent-manifest.json`;
  `integrations/tool-spec.json` (one JSON Schema reused as an OpenAI function,
  Anthropic tool, Gemini functionDeclaration and MCP inputSchema);
  `integrations/mcp_server.py` (dependency-free MCP stdio server);
  `integrations/adapters.py` (LangChain, CrewAI, AutoGen, LlamaIndex, OpenAI
  Agents, n8n, GitHub Actions).
- **`docs/MODEL_COMPATIBILITY.md`** — the 18 cross-model quirks and their
  defences, failure taxonomy, reproducibility mechanisms, runtime matrix.
- **Fully offline mode** (`FORGE_MOCK=1`): the entire pipeline runs with no keys
  and no network, and two runs are byte-identical.
- 18 new unit tests (28 total) plus an 8-check `self_test.py` that exercises the
  CLI contract, manifest consistency and the model layer without network.

### Fixed

- `extract_json` mis-sliced documents containing a nested array
  (`{"a":[1,2,]}` parsed as `[1,2]`); slicing is now start-bracket aware.
- Persian near-duplicates escaped deduplication when models disagreed about the
  ezafe hamza («حافظهٔ» vs «حافظه») or harakat; `content_key` now folds them.
- `--auto-sessions` wrote the raw detector payload into `sessions.json`,
  crashing enrichment. Candidates are now converted into contiguous
  `{name, start, end}` ranges covering every page, falling back to a single
  whole-document session, and are explicitly marked unreviewed.
- Truncated model responses (`finish_reason: length`) were silently discarded;
  the valid prefix is now salvaged by auto-closing brackets and the truncation
  is reported instead of hidden.
- HTTP 402 (credits exhausted) was retried through the full backoff schedule;
  it now skips the provider immediately, as 401/403 already did.
- API keys are no longer placed in Gemini request URLs (header auth instead),
  keeping them out of any proxy or server log.

### Changed

- `common.call_provider()` keeps its v1.3 signature but now routes through the
  adapter layer; `call_provider_reply()` exposes the full normalized reply
  (text, finish reason, provider, model, usage, timing).
- `load_provider_config()` accepts both the v1.3 `kind` and v1.4 `dialect`
  shapes and returns `ProviderInfo` objects that still behave like the old
  dicts (`p["name"]`, `p.get("kind")`).
- Default sampling moved from `temperature 0.15` to `temperature 0` / `top_p 1`
  with a fixed seed (`FORGE_SEED`, default 7) for determinism.
- Enrichment output is written as canonical JSON.

### Compatibility

Fully backwards compatible with 1.3.x and 1.4.x: every script, flag and invocation still
works. `--providers` became optional. The v1.4.0 recall-first OCR engine (PSM/scale ensemble, Sauvola, deskew, recall reports, low-confidence word gating) is carried forward unchanged. No breaking changes.

## 1.4.0 (2026-08-25) — recall-first OCR engine (ground-truth validated)

Word-recall guarantee + speed + token economy for the extraction layer;
multi-model audited (mistral-large-latest, gemini-3.1-flash-lite).

### Numbers (synthetic ground truth: 3 Persian pages, clean + degraded)
- clean 100/93.6/97.6% word recall (was 100/91.5/97.6)
- degraded (noise + 1.8° skew + downscale) 100/91.5/100% (was 100/87.2/97.6)
- residual misses = mixed-script tokens, flagged via low_conf_words for LLM repair

### Added
- scripts/test_ocr_core.py — 12 pure-logic unit tests (merge, RTL rejoin/order,
  repairs, coverage, IoU guards); runs without tesseract.
- recall_report.json (per-page logical/ocr/union coverage, missing-risk flags)
- evidence.json now carries ocr_low_conf_words [{w,conf,bbox,votes}] +
  ocr_mean_conf per page: token-gated LLM repair (send ONLY flagged words).

### Changed (extract_dual_ocr.py rewritten as v2 engine)
- 180 DPI single-pass psm6 -> 300 DPI PSM ensemble (3+6) PLUS 0.55x scale pass
  (psm 3+4): fas LSTM loses oversized glyphs at 300 DPI; the small-scale pass
  recovers them; union merge keeps every word any pass found (votes+conf).
- preprocessing: autocontrast -> median denoise -> projection deskew (+-10°)
  -> chunked Sauvola binarization (float32, row bands: no OOM).
- adaptive DPI retry at 400 for low-confidence pages; text-layer triage (dense
  text + <15% image area pages skip the ensemble: 1 verification pass = faster
  than the old engine on text-heavy lecture PDFs).
- RTL-aware reading-order reconstruction (vertical-overlap line grouping,
  within-line right-to-left ordering); direction-aware fragment rejoin.
- RAM-aware worker cap (~650MB/tessdata_best instance; /proc/meminfo).
- Arabic->Persian chars/digits repaired at word level; ZWNJ-edge handling.



## 1.3.2 (2026-08-25)

### Added
- `examples/01_sleep_eating_review.html` — golden reference output (5.4 MB,
  fully self-contained Persian RTL exam-review guide produced by this
  pipeline): agents can diff their built guide against it to confirm
  structure, RTL shell, enrichment contracts, and offline self-containment.
- SKILL.md now points agents to the example as the "what good looks like"
  reference.
- Package hygiene: stale `scripts/__pycache__/*.pyc` artifacts (inherited from
  the original upload, regenerated at runtime) are no longer shipped.



## 1.3.1 (2026-08-25)

Token-optimization release: SKILL.md input tokens cut 24% (1,564 -> 1,185,
o200k_base) with zero behavioral change — verified by independent multi-model
semantic-diff audits (verdict: PRESERVED).

### Changed
- Removed the 21-bullet capability brochure (features are embodied by the
  scripts; a one-line "Built-in" summary remains) and the 19-line file
  inventory (replaced by `ls scripts/ templates/`).
- Fixed the stale "v1.2.2" title; description shortened without losing
  discovery keywords.
- Merged duplicate guardrails; strengthened phrasing (publish/distribute
  without permission, inspect and validate medical education).
- All 10 pipeline commands, flags, evidence-layer rules, and QA/definition-of-
  done criteria are unchanged.

### Added
- Model-routing guidance: strong model for primary correction and flashcard
  verification; cheap model for the reviewer pass and bulk enrichment.



## 1.3.0 (2026-08-21)

Field fixes from a full production run that converted a 48-page Persian
psychology lecture PDF into a study guide and then maximised its six enrichment
sections across multiple free-tier providers.

### Fixed

- `reasoning_team_enrich.validate()` no longer crashes on Persian page
  references («صفحهٔ ۳»), Persian/Arabic answer labels («الف/ب/ج/د», ۱–۴), bare
  JSON arrays, or partial-but-valid batches — these are now coerced into the
  strict contract instead of discarding otherwise-valid content (new shared
  helpers in `common.py`: `coerce_ref`, `coerce_answer`, `is_bare_answer`,
  `strip_option_prefix`).
- Enrichment no longer fails a whole session when a provider returns fewer
  items than requested; well-formed subsets are accepted.
- Multiple-choice-style flashcards no longer keep a bare letter ("A") as their
  answer: such cards are dropped, and the new QA gate `flash-no-bare-answer`
  fails the build if any remain.
- Quiz/bank options no longer duplicate the shell's A–D labels with their own
  «الف) » prefixes (stripped at validation and in the HTML builder; new QA gate
  `quiz-options-no-letter-prefix`).
- The combined `--maximum` schema could be truncated by a smaller provider and
  return empty quiz/scenario sections; enrichment now retries those sections
  with a focused pass.

### Added

- `scripts/verify_flashcards.py`: independent post-hoc verification that
  confirms or corrects each flashcard answer against its source page and drops
  undeterminable ones instead of inventing content.
- New QA gates: `flash-no-bare-answer`, `quiz-options-no-letter-prefix`.

## 1.2.2

Base release used for the production run. See `SKILL.md` for capabilities.
