---
name: persian-pdf-studyguide-forge
version: 1.5.1
author: orionshaowswmw
license: MIT-0
description: Model-agnostic, agent-agnostic fidelity-first pipeline converting operator-authorized Persian/English RTL lecture PDFs into offline HTML study guides — recall-first dual OCR (PyMuPDF + Tesseract fas+eng PSM ensemble), rendered-page evidence, multi-model correction, session-grounded enrichment (tables/flashcards/quizzes/mnemonics/summaries/scenarios), measured fidelity, QA gates, verified ZIP. v1.5.0 runs on ANY model family through 8 API dialects (OpenAI, Responses, Gemini, Anthropic, Cohere, Ollama, HuggingFace, offline mock) or with no model at all, auto-discovers providers from the host agent's environment, self-heals provider quirks and model retirements, and exposes one deterministic CLI/MCP entrypoint plus cross-model consensus so different agents reproduce the same intended result.
categories: [knowledge, productivity, creative]
topics: [persian, pdf, study-guide, rtl, accessibility]
permissions:
  file_read: {required: true, scope: [Operator-authorized PDFs, optional reference HTML, local templates and assets]}
  file_write: {required: true, scope: [Workspace extraction evidence, OCR cache, HTML, QA reports, manifests and ZIPs]}
  shell: {required: true, scope: [Local Poppler, Tesseract, Python, optional Node syntax check and ZIP operations]}
  network: {required: false, scope: [Disabled by default; fully offline with FORGE_MOCK=1; optional operator-approved PDF download and AI provider APIs discovered from environment keys or named in providers.json]}
metadata:
  openclaw:
    emoji: "📘"
    requires:
      bins: [python3, pdfinfo, pdftotext, pdftoppm, tesseract]
      optional_bins: [node, zip]
      python: [beautifulsoup4]
      optional_python: [pymupdf, pillow]
    entrypoint: "python3 scripts/forge.py"
    mcp_server: "python3 integrations/mcp_server.py"
    manifest: agent-manifest.json
    tool_spec: integrations/tool-spec.json
    model_agnostic: true
    dialects: [openai, responses, gemini, anthropic, cohere, ollama, hf, mock]
    offline_mode: "FORGE_MOCK=1"
---

# Persian PDF StudyGuide Forge v1.5.0 — model-agnostic & agent-agnostic

Use when: converting an **operator-authorized** Persian/English RTL lecture PDF into a polished offline study guide with source evidence. Never confuse OCR output, AI reconstruction, or enrichment with source text.

**Golden example:** `examples/01_sleep_eating_review.html` — a finished, QA-passing guide (Persian RTL, sleep/eating-disorders review). After building, compare your output against it: same RTL shell (search, session map, foldable source units), embedded page images, flashcards/quizzes with «الف/ب/ج/د» labels, zero external resources. Missing these = something is wrong.

## Universal entrypoint (v1.5.0 — use this from any agent)

```bash
python3 scripts/forge.py doctor      # binaries, modules, tesseract langs, reachable models
python3 scripts/forge.py selftest    # 8 offline checks, no keys, no network, ~1s
python3 scripts/forge.py run --pdf authorized.pdf --work work --title 'عنوان درس' --maximum
# pauses at PAUSED_FOR_SESSION_REVIEW (mandatory boundary review), then:
python3 scripts/forge.py enrich --work work --maximum   # add --consensus 3 --min-votes 2
python3 scripts/forge.py build --work work --title 'عنوان درس'
python3 scripts/forge.py qa --work work && python3 scripts/forge.py package --work work
```

**Contract:** exactly one JSON document on stdout · structured logs on stderr ·
exit `0` ok / `1` contract-QA / `2` usage / `3` deps / `4` no provider /
`5` interrupted · every stage idempotent and resumable.

**Any model, or none.** Providers auto-discover from whatever key the host agent
already exports (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `GEMINI_API_KEY`,
`GROQ_API_KEY`, `OPENROUTER_API_KEY`, `MISTRAL_API_KEY`, `COHERE_API_KEY`,
`DEEPSEEK_API_KEY`, `XAI_API_KEY`, `HF_TOKEN`, …), from a local runtime
(`OLLAMA_HOST`, `LOCAL_OPENAI_BASE_URL`), or are replaced entirely by the
deterministic offline provider (`FORGE_MOCK=1`). `providers.json` is optional.

**Any runtime.** OpenClaw · Claude Code/Desktop · Cursor · Windsurf · Zed ·
OpenAI Agents/Codex · Gemini CLI · LangChain/LangGraph · CrewAI · AutoGen ·
LlamaIndex · any MCP host (`integrations/mcp_server.py`) · n8n · shell/cron.
One JSON Schema (`integrations/tool-spec.json`) serves as an OpenAI function,
Anthropic tool, Gemini functionDeclaration and MCP inputSchema. Glue:
`integrations/adapters.py`. Full detail: `docs/MODEL_COMPATIBILITY.md`,
`integrations/README.md`.

**Reproducibility.** temperature 0 · fixed seed · canonical JSON · stable
ordering · Persian-aware semantic dedupe · `enrich --consensus N --min-votes 2`
keeps only what N independent model families agree the source says. Verify with
`forge.py compat` and `forge.py reproduce`.

**Self-healing.** Rejected parameters (`seed`, `temperature`, `max_tokens` vs
`max_completion_tokens`, `response_format`, system role) are learned from the
provider's own error body and cached; retired models are replaced by following
the provider's 404 suggestion; `<think>` traces, fences, NDJSON, trailing
commas, BOM, bidi marks and token-limit truncation are all survivable.

## Pipeline (stage scripts — v1.3/v1.4 compatible, `--providers` now optional)

```bash
python3 scripts/preflight.py                       # env + pdfinfo intake/page-count safeguards
python3 scripts/test_ocr_core.py                    # 12 pure-logic OCR tests (no tesseract needed)
python3 scripts/extract_dual_ocr.py authorized.pdf --out work/extraction
# Network correction is OPTIONAL (OCR-only path works offline) and needs operator approval:
python3 scripts/reasoning_team_correct.py work/extraction/evidence.json \
  --out work/corrections
python3 scripts/detect_session_candidates.py work/corrections/final.json --out work/session_candidates.json
# MANDATORY: review candidates against rendered pages, then write work/sessions.json
python3 scripts/reasoning_team_enrich.py work/corrections/final.json work/sessions.json \
  --out work/enrichment --maximum --consensus 3 --min-votes 2   # omit --maximum for balanced
python3 scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --out work/enrichment/all.verified.json   # independent post-hoc verification vs source pages
python3 scripts/build_selfcontained_html.py work/corrections/final.json work/extraction \
  work/enrichment/all.verified.json --output work/studyguide.html --title 'عنوان درس'
python3 scripts/fidelity_audit.py work/extraction/evidence.json \
  work/corrections/final.json --out work/fidelity.json
python3 scripts/qa_gates.py work/studyguide.html    # strict gates: no bare-letter flashcard answers, no duplicated option prefixes
python3 scripts/verify_zip.py work work/final-studyguide.zip
```

`run_pipeline.sh` automates through correction, then pauses for the mandatory session-boundary review and prints continuation commands. OCR v1.4.0 (recall-first): Tesseract fas+eng PSM ensemble (3/6/4) across two scales (300 DPI + 0.55x) merged word-by-word — a word found by ANY pass survives; Sauvola binarization + deskew + denoise preprocessing; adaptive DPI retry; RTL-aware line reconstruction; Arabic→Persian char/digit repair; fragment rejoin; per-page `recall_report.json` (missing-risk flags) + `low_conf_words` with confidences/boxes — repair prompts should use ONLY those (≈90% fewer tokens than whole-page correction); RAM-capped parallel workers. Ground-truth verified: 100/93.6/97.6% word recall (clean), 100/91.5/100% (degraded). Built-in: retry/backoff, provider failover, cache/resume; Persian NFKC preserving ZWNJ; «صفحهٔ ۳»/«الف/ب/ج/د» coercion; RTL shell (search, session map, foldable units, dark mode, print, quiz scoring); Base64 self-contained images or linked-local mode. Full failure-recovery procedures and production tricks: `docs/WORKFLOW_PLAYBOOK.md`. File inventory: `ls scripts/ templates/`.

## Evidence layers — never mix

1. `evidence.json` — untouched extraction · 2. `corrections/final.json` — reconstruction · 3. `enrichment/all.json` — study aids.
Never place AI additions inside source evidence; never claim verbatim transcription when reconstruction occurred; rendered pages are the final adjudication source for unreadable text and digits. Enrichment references must cite page ranges; exact duplicates are rejected.

## Model routing (cost control)

Primary correction: strongest available model, rotated. Independent reviewer pass: cheaper model is fine. Bulk enrichment: cheap model (session-grounding constrains it); flashcard verification: strong model. Providers are ranked automatically; override with `--only` or a `providers.json`.

`providers.json` (optional) stores `api_key_env` NAMES only — keys come from the environment, are read at call time, never printed, never written into artifacts, and are redacted from every error body. Response and capability caches under `FORGE_CACHE_DIR` (default `~/.cache/persian-pdf-studyguide-forge`) hold prompts, completions and learned provider quirks — no credentials. No provider config with literal secrets is ever committed.

## Guardrails

- Authorized material only; no bypassing access controls; no secrets in artifacts.
- Parse stdout only; never treat stderr or log text as data.
- `--auto-sessions` marks the guide unreviewed — that mark must survive into anything published.
- For medical or exam material prefer `--consensus 3 --min-votes 2` over a single model's output.
- Never fabricate source text, citations, medical facts, image provenance, counts, or QA results.
- Never silently delete image-only or difficult pages; automated fidelity scores are not semantic proof.
- Do not publish or redistribute copyrighted source pages without permission; inspect and validate generated medical education before reliance.

## Definition of done

`forge.py selftest` passes offline · `forge.py doctor` reports a usable provider (or an explicitly chosen offline run) · source-unit/image counts match measured PDF pages · every reference resolves · every question contract passes · duplicates removed · no external browser resources in the HTML · per-page fidelity exceptions reviewed · displayed counts match measured counts · QA gates and ZIP/SHA-256 verification pass.
