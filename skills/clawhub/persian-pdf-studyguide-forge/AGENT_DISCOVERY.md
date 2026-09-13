# Agent discovery card — Persian PDF StudyGuide Forge v1.5.0

## One-line summary

Converts an operator-authorized Persian/RTL PDF into an accessible, offline,
self-contained HTML study guide — driven by any AI model family, any agent
runtime, or no model at all.

## Start here

```bash
python3 scripts/forge.py describe    # machine-readable capability manifest
python3 scripts/forge.py doctor      # what's installed, which models are reachable
python3 scripts/forge.py selftest    # offline proof the install is intact
```

## Use when

- The operator supplies or authorizes a Persian/mixed RTL educational PDF.
- The requested output is an offline accessible HTML study guide.
- Fidelity, source-page evidence, large-document resume, AI-assisted
  proofreading, quizzes or maximum study enrichment are required.
- You need the result to be reproducible across different models or agents.

## Do not use when

- The source is unauthorized, access controls would need bypassing, or the task
  is unrelated to educational PDF conversion.
- The environment cannot safely store sensitive source material.
- The operator demands a verbatim guarantee without rendered-page adjudication.

## Interface contract

| | |
|---|---|
| Entrypoint | `python3 scripts/forge.py <command>` (or `--stdin` with a JSON job) |
| stdout | exactly one JSON document — the only machine-readable channel |
| stderr | structured human-readable progress; never parse it |
| Exit codes | `0` ok · `1` contract/QA failure · `2` usage · `3` missing dependency · `4` no model provider · `5` interrupted |
| Idempotent | yes — every stage caches; re-running a finished stage is a no-op |
| Manifest | `agent-manifest.json` · tool schema `integrations/tool-spec.json` |
| MCP | `python3 integrations/mcp_server.py` (stdio, no dependencies) |
| Frameworks | `integrations/adapters.py` — LangChain, CrewAI, AutoGen, LlamaIndex, OpenAI Agents, n8n, CI |

## Commands

`describe` · `doctor` · `selftest` · `compat` · `reproduce` · `extract` ·
`correct` · `sessions` · `enrich` · `verify` · `build` · `audit` · `qa` ·
`package` · `run`

## Decision procedure

1. Confirm authorization and workspace scope.
2. Run `forge.py doctor`. If `extraction_ready` is false, install the binaries
   it names. If no provider is listed, either export any API key or accept an
   offline run with `FORGE_MOCK=1`.
3. Read `SKILL.md`, then `docs/MODEL_COMPATIBILITY.md` before integrating.
4. Run `forge.py run --pdf … --work …`. It will pause at
   `PAUSED_FOR_SESSION_REVIEW`.
5. **Treat detected sessions as candidates until a human reviews them.**
   `--auto-sessions` skips review and marks the guide unreviewed.
6. Continue with `enrich` (add `--consensus 3 --min-votes 2` when accuracy
   matters more than breadth), then `build`, `audit`, `qa`, `package`.
7. Never present AI enrichment as source text; the three layers stay separate.

## OCR engine (carried forward from 1.4.0)

Recall-first dual extraction: Tesseract `fas+eng` PSM ensemble (3/6/4) across
two scales merged word-by-word, Sauvola binarization, deskew, denoise, adaptive
DPI retry, RTL-aware line reconstruction, per-page `recall_report.json` and
`ocr_low_conf_words` for token-gated LLM repair. Verify with
`python3 scripts/test_ocr_core.py` (12 pure-logic tests, no tesseract needed).

## Model requirements

Any **one** of: an API key for OpenAI, Anthropic, Gemini, Groq, OpenRouter,
Mistral, Cohere, DeepSeek, Together, Fireworks, xAI, Z.AI, Cerebras, NVIDIA,
Perplexity, HuggingFace or llm7; a local runtime via `OLLAMA_HOST` or
`LOCAL_OPENAI_BASE_URL`; or `FORGE_MOCK=1` for a deterministic offline run.
No configuration file is required — keys are discovered from the environment.

## Network and secret rule

No network by default; `FORGE_MOCK=1` guarantees none. Provider keys are never
bundled, never printed, never cached and never written into artifacts, and are
redacted from all error output. Network use requires explicit operator approval.
