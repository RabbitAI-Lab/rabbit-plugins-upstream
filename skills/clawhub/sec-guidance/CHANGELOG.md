# Changelog

## 0.2.0 — 2026-08-03

Self-contained light mode + auto-detect dispatcher.

- New `sec_guidance_light.py`: fetches the latest 10-K/10-Q directly from
  SEC EDGAR, extracts text (BeautifulSoup), chunks in memory, ranks with
  BM25, calls Claude or OpenAI with inline citations. No Elasticsearch,
  no Ollama, no external RAG pipeline required.
- `extract_guidance.py` now dispatches by runtime detection:
  `--mode auto` (default) runs heavy if `SEC_PIPELINE_DIR` is set AND the
  pipeline is importable AND Elasticsearch is reachable; otherwise light.
  `--mode {light,heavy}` forces one.
- `SEC_PIPELINE_DIR` demoted from required to optional; light mode needs
  only `ANTHROPIC_API_KEY` (or `OPENAI_API_KEY`).
- `requirements.txt` added: `requests`, `beautifulsoup4`, `rank-bm25`,
  `anthropic`.
- Filings cached under `~/.cache/sec-guidance/` for repeat runs.

## 0.1.0 — 2026-07-26

Initial ClawHub release.

- `extract_guidance.py`: runs 5 standard guidance queries (or a single
  custom `--query`) against a local SEC filing RAG pipeline
  (Elasticsearch + sentence-transformers + cross-encoder rerank + Ollama),
  printing cited answers with source file / page / filing date.
- Pipeline location is taken strictly from the `SEC_PIPELINE_DIR`
  environment variable (no hardcoded paths); the script exits with a
  clear error when unset, when the pipeline can't be imported, or when
  the index is empty.
- SKILL.md documents setup (env var, Elasticsearch, ingestion), trigger
  scenarios, and all commands.
