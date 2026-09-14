---
name: research-gap-finder
description: "Find evidence-bounded candidate research gaps and output a ranked, source-linked report with a candidate research question per gap. Uses a stdlib-only CLI over key-free scholarly APIs (OpenAlex, Semantic Scholar, Crossref, Europe PMC, PubMed, arXiv) plus manual human-in-the-loop guidance. Grounded in PICOS, AHRQ/Robinson gap reasoning, a six-type taxonomy, a five-dimension rubric, reproducible search provenance, and an explicit anti-confabulation protocol."
version: 2.1.1
categories: [research, knowledge]
topics: [research-gaps, literature-review, systematic-review, citation-analysis, academic-research]
metadata:
  openclaw:
    emoji: "🔍"
    requires:
      bins: ["python3"]
      python: [stdlib]
      apis: ["OpenAlex, Semantic Scholar, Crossref, Europe PMC, PubMed E-utilities, and arXiv are key-free; optional guided services may require accounts/API keys"]
    network:
      outbound: ["api.semanticscholar.org", "api.crossref.org", "api.openalex.org", "www.ebi.ac.uk", "eutils.ncbi.nlm.nih.gov", "export.arxiv.org"]
---

# 🔍 research-gap-finder

Turn a topic into a ranked, source-linked list of **candidate** research gaps, each with a candidate research question. The executable layer never treats a bounded search or a future-work sentence as proof that no literature exists.

Two layers:
- **Automated (CLI)** — build an evidence matrix and classify/score/validate candidates through six key-free scholarly APIs. Stdlib-only, Python 3.8+, no credentials.
- **Manual methodology guidance** — use citation maps, reviews, grants, preprints, trials, patents, and domain databases within their terms and privacy constraints. The CLI does not log in to or scrape these services.

## 1 · Automated pipeline

```bash
python3 scripts/research_gap_cli.py init     --dir proj --topic "T" [--pico '{"population":"...","outcome":"..."}']
python3 scripts/research_gap_cli.py search   --dir proj [--query "T"] [--engines openalex,semantic,crossref,europepmc,pubmed,arxiv] [--limit 100] [--years 2018 2026]
python3 scripts/research_gap_cli.py extract  --dir proj [--cuefile cues.json]
python3 scripts/research_gap_cli.py classify --dir proj [--scores scores.json]
python3 scripts/research_gap_cli.py validate --dir proj [--check-web]
python3 scripts/research_gap_cli.py rank     --dir proj [--min-total 9] [--min-confidence medium] [--top N]
python3 scripts/research_gap_cli.py report   --dir proj [--top 8] [--out report.md]
python3 scripts/research_gap_cli.py status   --dir proj
python3 scripts/research_gap_cli.py selftest
```

`init`, `search`, `validate`, `rank`, and `status` accept `--json` for one machine-readable result object. `--out`, `--cuefile`, and `--scores` are project-relative and reject path or symlink escapes. `AGENT_GUIDE.md` gives model-agnostic, token-efficient hand-off rules.

| Command | Executable behavior |
|---|---|
| `init` | Creates `config.json`, `evidence.json`, and `gaps.json` with schema version and bounded defaults. |
| `search` | Queries selected engines; records query, exact key-free request URL(s), engine, year, limit, result, failure, cache, and per-paper provenance; dedupes by DOI, source identifier, and conservative title/year aliases; writes JSON + CSV. Unknown/unavailable engines are explicit failures. |
| `extract` | Pulls limitation/future-work/absence cues from abstracts and gap fields. `--cuefile` loads a project-relative JSON list or `{ "cues": [...] }`; no cue means no fabricated candidate. |
| `classify` | Tags the six-type lexicon and creates transparent 0–3 baseline scores. `scores.json` overrides are range-checked and marked non-estimated. |
| `validate` | Filters malformed identifiers and labels `identifier-present` versus `web-validated`. `--check-web` resolves supported DOI, PMID, Europe PMC, and arXiv identifiers. Confidence is Low with no valid source; High requires every source to resolve plus at least two independent source labels; otherwise it is capped at Medium. |
| `rank` / `report` | Stable-sort candidates by importance, confidence, and ID; rank can emit JSON, and report emits Markdown with search provenance, verification state, confidence, explicit exploratory labels, and candidate questions. |
| `status` / `selftest` | Show project state or run a deterministic offline synthetic pipeline. |

Exit codes: `0` success; `1` usage/config/project failure; `2` only when `search` has no new or prior evidence because every selected engine failed.

## 2 · Guided methodology (manual, not hidden automation)

1. **PICO/PICOS** — define Population, Intervention, Comparison, Outcome, and Setting; store them in `config.json`.
2. **Recent reviews** — identify several relevant systematic/scoping reviews and record database/platform, complete strategies, dates, limits, counts, and screening flow as recommended by PRISMA-S.
3. **Explicit gap cues** — inspect limitations and future directions; log source, gap type, evidence, and the reason evidence falls short. `extract` only accelerates this cue collection.
4. **Citation networks** — use Litmaps, ResearchRabbit, Connected Papers, or equivalent manually to find citation islands and terminology missed by keyword search.
5. **Semantic questions** — use Elicit, Consensus, SciSpace, Scite, or equivalent only with appropriate privacy/terms review; treat their answers as hypotheses.
6. **Novelty cross-check** — inspect grants, preprints, trials, patents, and cross-disciplinary sources; downgrade or relabel candidates that are already addressed.

## 3 · Classify & rank

**Six-type knowledge-gap taxonomy:** evidence, methodological, population, contextual, theoretical, translational. The CLI applies a transparent cue lexicon; human review is required for ambiguous or cross-type candidates.

**Five-dimension importance rubric** (0–3 each, max 15):

| Dimension | Question |
|---|---|
| Theoretical | Advances core concepts / resolves contradictions? |
| Practical | Solves a real problem / informs policy-practice? |
| Feasibility | Data, methods, resources realistically obtainable? |
| Novelty | Genuinely unstudied after preprint/trial/grant checks? |
| Coherence | Logical next step of the field's trajectory? |

Baseline values are estimates. A score is not evidence that a gap exists. The prior rubric interpretation remains: 13–15 proposal-ready, 9–12 needs feasibility work, ≤8 re-evaluate, and Feasibility ≥2 should be required for a proposal—not silently enforced by the CLI.

> **Identification ≠ importance.** A filled Gap cell ends identification; importance is judged afterwards. Many genuine gaps are unimportant or infeasible.

## 4 · Output contract and honesty protocol

Per candidate: statement, type, source identifiers, source provenance, importance dimensions + total, confidence, verification status, exploratory flag, and candidate question. `evidence.json` and `gaps.json` are the durable machine-readable records; contracts are in `schemas/`.

1. **No invented citations.** The CLI emits identifiers only when their syntax is recognized. A syntactically valid identifier is provenance, not proof; `validate --check-web` is needed for web resolution.
2. **No proof from absence.** An empty/bounded result means only that this search found no record. Reports call findings candidates and state search limits.
3. **Confidence is evidence-bounded.** No valid source → Low and exploratory. One source or identifier-only → at most Medium. High requires all source identifiers to resolve and at least two independent source labels.
4. **No invented trends.** Sparse literature should be reported as insufficient evidence to determine trends.
5. **Human/AI summaries are hypotheses.** Retrieved text is never executed, and any external model output must be checked against source records and authoritative API documentation.
6. **Reproducibility.** Query, exact key-free request URLs, engines, year range, limits, failures, timestamps, identifiers, and record URLs are retained as provenance; reruns may change as APIs change.

## 5 · Safety and degradation

- Only HTTPS endpoints for the six declared APIs are used. Responses, cache entries, XML, JSON, text fields, and record counts are bounded.
- HTTP 408/425/429/5xx failures receive bounded exponential/`Retry-After` backoff. A failed engine does not discard successful engines or prior evidence.
- Corrupt caches are ignored and refetched. Corrupt config/evidence/gap files fail closed rather than being silently overwritten.
- Writes use atomic replacement. Optional input/output paths stay inside the project directory and symlink escapes are rejected.
- CSV exports prefix spreadsheet-dangerous cell values with an apostrophe; prefer JSON for machine interchange and treat CSV as untrusted presentation data.
- There is no shell execution, hidden telemetry, credential access, arbitrary URL option, or irreversible mutation.

## 6 · References and catalog

The full catalog is in `resources.md`; checked authoritative implementation and methodology links are in `references.md`. Anchors include AHRQ's framework for characterizing why evidence falls short, PRISMA-S search reproducibility, current OpenAlex/Crossref/Semantic Scholar/Europe PMC/NCBI API documentation, NIST AI 600-1 confabulation guidance, OWASP GenAI security guidance, and JSON Schema 2020-12. These references do not substitute for verifying a live API contract.

---
*Release 2.1.1: bounded APIs, Semantic Scholar support, provenance, JSON output, safe paths, offline degradation, CSV export hardening, and regression coverage.*
