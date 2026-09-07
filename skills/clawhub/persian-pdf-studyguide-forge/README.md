# 📘 Persian PDF StudyGuide Forge

An executable, fidelity-first toolkit for turning **operator-authorized Persian RTL lecture PDFs** into accessible, offline-first HTML study guides.

**Version 1.5.0 makes the skill model-agnostic and agent-agnostic.** It runs on
any LLM family through eight API dialects — or with no model at all — and any
agent runtime can drive it through one deterministic entrypoint. Everything
from 1.4.0 (recall-first OCR ensemble) and 1.3.0 (Persian/Arabic coercion,
flashcard verification, strict QA gates) is unchanged.

```bash
python3 scripts/forge.py doctor      # what's installed, which models are reachable
python3 scripts/forge.py selftest    # 8 offline checks, no keys, no network
python3 scripts/forge.py run --pdf lecture.pdf --work out --title 'عنوان درس' --maximum
```

| | |
|---|---|
| **Works with** | GPT · Claude · Gemini · Grok · DeepSeek · Qwen · Mistral · Llama · Command · GLM · anything OpenAI-compatible · local Ollama/vLLM/LM Studio · **or fully offline** |
| **Driven by** | OpenClaw · Claude Code · Cursor · Windsurf · Zed · OpenAI Agents/Codex · Gemini CLI · LangChain/LangGraph · CrewAI · AutoGen · LlamaIndex · any MCP host · n8n · plain shell/cron |
| **Needs** | one API key from any provider — or `OLLAMA_HOST`, or `FORGE_MOCK=1`. No config file required. |

See [`docs/MODEL_COMPATIBILITY.md`](docs/MODEL_COMPATIBILITY.md) and
[`integrations/README.md`](integrations/README.md).

## ✨ What it does

- Measures and hashes the source PDF.
- Extracts a logical text layer with PyMuPDF/Poppler.
- Runs an independent Persian–English Tesseract OCR pass.
- Renders compact page evidence for visual checking and offline HTML.
- Normalizes Persian Unicode, digits, whitespace and mixed RTL/LTR safely.
- Optionally uses multiple AI providers as a reasoning team: rotating primary correction, independent reviewer, retries, cache/resume and validated failover.
- Detects candidate session boundaries for mandatory review.
- Generates source-linked tables, flashcards, mnemonics, review points, four-option quizzes and clinical/laboratory scenarios.
- Supports a high-volume `--maximum` enrichment mode while rejecting exact duplicates.
- Coerces Persian/Arabic provider output («صفحهٔ ۳» refs, «الف/ب/ج/د» answer labels, bare arrays, partial batches) instead of silently dropping it.
- Verifies flashcard answers against their source pages with an independent model (`scripts/verify_flashcards.py`).
- Builds a self-contained HTML with embedded images, search, dark mode, folds, deep links, responsive tables, print support and interactive scoring.
- Produces fidelity reports, automated QA results, verified ZIPs and SHA-256 checksums.
- **Speaks eight API dialects** through one stdlib-only adapter layer, auto-discovers providers from the environment, and self-heals provider quirks and model retirements (v1.5.0).
- **Reproduces the same intended result across model families** via canonical artifacts, stable ordering, Persian-aware semantic dedupe and n-way cross-model consensus (v1.5.0).

See [`docs/WORKFLOW_PLAYBOOK.md`](docs/WORKFLOW_PLAYBOOK.md) for every production method, procedure, recovery trick and QA rule.

**v1.4.0: recall-first OCR** — PSM+scale ensemble, Sauvola/deskew preprocessing,
per-page coverage reports, and token-gated LLM repair data (fix only flagged
words, not whole pages). Ground-truth: 100% word recall on clean pages.

A complete, QA-passing **example output** ships in `examples/01_sleep_eating_review.html` (open it in a browser — this is what a finished guide looks like).

## 🆕 What 1.5.0 adds

- **`scripts/model_adapters.py`** — one stdlib-only layer (urllib, no SDKs) speaking
  `openai`, `responses` (OpenAI Responses), `gemini`, `anthropic`, `cohere`,
  `ollama`, `hf`, and a deterministic offline `mock`.
- **`scripts/forge.py`** — a single entrypoint with a frozen contract: one JSON
  document on stdout, logs on stderr, stable exit codes, `--stdin` job objects.
- **Zero-configuration providers.** Keys auto-discovered from the host agent's
  environment; `providers.json` optional; local Ollama/vLLM/LM Studio supported.
- **Self-healing capability probe.** Rejected parameters (`seed`, `temperature`,
  `max_tokens` vs `max_completion_tokens`, `response_format`, system role) are
  detected from the provider's own error body, dropped, retried and cached.
  Retired models are replaced by following the provider's 404 suggestion.
- **Quirk-proof parsing.** `<think>` traces, markdown fences, NDJSON, trailing
  commas, Python constants, smart quotes, BOM, RTL bidi marks and token-limit
  truncation are all survivable.
- **Cross-model consensus.** `enrich --consensus N --min-votes 2` keeps only
  what several independent model families agree the source says.
- **`compat` / `reproduce` commands** producing machine-readable compatibility
  and cross-model agreement reports.
- **Interop manifests** — `agent-manifest.json`, `integrations/tool-spec.json`
  (one schema → OpenAI/Anthropic/Gemini/MCP), `integrations/mcp_server.py`
  (dependency-free MCP server), `integrations/adapters.py` (LangChain, CrewAI,
  AutoGen, LlamaIndex, n8n, CI).
- **Fully offline mode.** `FORGE_MOCK=1` runs the whole pipeline with no keys and
  no network; two runs are byte-identical.

## 🚀 Minimal workflow

### One command (any runtime, any model)

```bash
python3 scripts/forge.py run --pdf lecture.pdf --work work --title 'عنوان درس' --maximum
```

It pauses with `status: PAUSED_FOR_SESSION_REVIEW` so a human can confirm
session boundaries, then continues with `forge.py enrich` / `build`.
`--auto-sessions` accepts detected boundaries and marks the guide unreviewed.

### Stage by stage (v1.3/v1.4 scripts, all still valid)

```bash
python3 scripts/preflight.py
python3 scripts/extract_dual_ocr.py lecture.pdf --out work/extraction
python3 scripts/reasoning_team_correct.py work/extraction/evidence.json \
  --out work/corrections          # --providers is optional in 1.5.0
python3 scripts/detect_session_candidates.py work/corrections/final.json \
  --out work/session_candidates.json
# Review and create sessions.json.
python3 scripts/reasoning_team_enrich.py work/corrections/final.json sessions.json \
  --out work/enrichment --maximum --consensus 3 --min-votes 2
python3 scripts/verify_flashcards.py work/corrections/final.json work/enrichment/all.json \
  --out work/enrichment/all.verified.json
python3 scripts/build_selfcontained_html.py work/corrections/final.json work/extraction \
  work/enrichment/all.verified.json --output work/studyguide.html --title 'عنوان درس'
python3 scripts/fidelity_audit.py work/extraction/evidence.json work/corrections/final.json \
  --out work/fidelity.json
python3 scripts/qa_gates.py work/studyguide.html
python3 scripts/verify_zip.py work work/studyguide.zip
```

## 🔐 Permissions and requirements

### Required local reads

- PDFs and optional reference HTML explicitly supplied/authorized by the operator.
- Bundled templates and locally generated extraction/OCR evidence.

### Required local writes

- Workspace-only rendered pages, OCR caches, JSON evidence, HTML, reports, manifests and ZIPs.

### Required commands

- Python 3
- Poppler: `pdfinfo`, `pdftotext`, `pdftoppm`
- Tesseract with `fas` and `eng`

Optional: PyMuPDF, Pillow, BeautifulSoup4, Node.js.

### Optional network access

Disabled by default. Network is used only when the operator explicitly requests either:

1. download of an authorized PDF URL; or
2. AI-assisted correction/enrichment through endpoints listed in a local provider configuration.

### API keys

No key is bundled and none is ever written anywhere. In 1.5.0 the skill reads
whatever the host agent already has in its environment — any **one** of:

```
OPENAI_API_KEY  ANTHROPIC_API_KEY  GEMINI_API_KEY / GOOGLE_API_KEY  GROQ_API_KEY
OPENROUTER_API_KEY  MISTRAL_API_KEY  COHERE_API_KEY  DEEPSEEK_API_KEY
TOGETHER_API_KEY  FIREWORKS_API_KEY  XAI_API_KEY  ZAI_API_KEY  CEREBRAS_API_KEY
NVIDIA_API_KEY  PERPLEXITY_API_KEY  HF_TOKEN  LLM7_API_KEY
OLLAMA_HOST                # local models, no key at all
LOCAL_OPENAI_BASE_URL      # vLLM / LM Studio / llama.cpp server
FORGE_MOCK=1               # no model at all — deterministic offline run
```

A `providers.json` (recording only `api_key_env` names, never values) is still
supported and takes precedence. Keys are read at call time, never printed,
never cached, never written into artifacts, and are redacted from every error
message. Never paste keys into HTML, prompts, logs, README, Git, or ClawHub.

Tuning: `<PROVIDER>_MODEL`, `<PROVIDER>_BASE_URL`, `FORGE_SEED` (default 7),
`FORGE_TIMEOUT`, `FORGE_CACHE_DIR`, `FORGE_VERBOSE=0`.

## 🔒 Security & Privacy

- Local extraction/build/QA sends nothing off-device. `FORGE_MOCK=1` makes the
  entire pipeline network-free.
- Response and capability caches live under `FORGE_CACHE_DIR` (default
  `~/.cache/persian-pdf-studyguide-forge`) and contain **no credentials** —
  only prompts, completions and learned provider quirks. Delete to purge.
- `stdout` carries only the JSON result; diagnostics go to `stderr`, redacted.
- AI mode sends only the selected OCR/source batches to explicitly configured providers.
- The skill does not transmit files to ClawHub during normal use.
- Scripts do not print authorization headers or key values.
- Successful AI batches are cached without credentials to make long jobs resumable.
- Remote download enforces HTTPS by default, a size cap, PDF magic and SHA-256 recording.
- Source PDFs may contain private/copyrighted material. Confirm authority before processing and distribution.
- AI can introduce factual errors. Use rendered-page evidence, fidelity reports and QA; medical/academic content still requires qualified review.
- Self-contained HTML can be large because page images are embedded. Use linked-image mode when required.
- Review all bundled scripts before execution and restrict them to a dedicated workspace.

## Known risks and mitigations

| Risk | Mitigation |
|---|---|
| OCR omissions or garbled RTL | dual OCR, rendered-page evidence, primary + reviewer, manual adjudication |
| AI hallucination | source-only prompts, strict JSON, page-range references, independent review, fidelity audit |
| Partial/truncated provider output | schema/count validation, retries, provider rotation, split batches, cache/resume |
| Secret disclosure | environment variable names only; no literal keys; never log headers |
| Inflated “maximum” content | session grounding, exact duplicate rejection, source links and question contracts |
| False completeness claim | measured PDF/unit/image counts and QA gate report |
| Broken offline bundle | no external browser loads, embedded CSS/JS/images, ZIP verification |
| One model's idiosyncrasies shipped as fact | `--consensus N --min-votes 2` keeps only what several independent model families agree on |
| Silent divergence between agent runtimes | one entrypoint, one JSON contract, frozen exit codes; `selftest` runs it offline in CI |
| Provider quirk or retirement breaking a run | capability probe learns rejected parameters; retired models replaced via the provider's own 404 suggestion; failover across families |
| Truncated model output shipped as complete | `finish_reason: length` surfaced, valid prefix salvaged, section re-asked |

## ✅ Verification

Prove the installation is intact and model-agnostic, offline, in about a second:

```bash
python3 scripts/forge.py selftest     # 8 checks incl. the full unit suite
python3 scripts/forge.py doctor       # binaries, modules, reachable models
python3 scripts/forge.py compat       # per-model compatibility matrix
python3 scripts/forge.py reproduce    # cross-model agreement report
python3 scripts/test_ocr_core.py      # 12 pure-logic OCR tests
```

The published artifact includes `MANIFEST.sha256`, covering executable scripts, templates, documentation and skill metadata. Verify after installation:

```bash
cd persian-pdf-studyguide-forge
sha256sum -c MANIFEST.sha256
```

Manifest SHA-256: `31602495837535c8c4e72bd823e2f8bf80c78610ab419625a32be5a9edc8d452`

`README.md`, `MANIFEST.sha256`, and registry-managed `skill-card.md` and `_meta.json` are excluded from the file list to avoid a self-referential hash; the manifest hash above authenticates the list itself.

## License

MIT-0 — free to use, modify and redistribute without attribution.
