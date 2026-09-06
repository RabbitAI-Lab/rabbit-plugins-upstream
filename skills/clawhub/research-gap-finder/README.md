# 🔍 Research Gap Finder

**Category:** research, knowledge · **Release:** 2.1.1

Turn a broad topic into a ranked, source-linked list of **candidate** research gaps with a candidate research question per gap. The CLI is intentionally evidence-bounded: a limitation sentence is not proof of absence, and a DOI/accession is not web verification.

## 🔐 Permissions & requirements
- **Runtime:** Python 3.8+ and the standard library only; no packages, API keys, or `curl` are required for the automated core.
- **Network (key-free):** OpenAlex, Semantic Scholar, Crossref, Europe PMC, PubMed E-utilities, and arXiv. The default is bounded to OpenAlex, Crossref, Europe PMC, and arXiv; opt into the other engines with `--engines`.
- **Guided/manual sources:** Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace, Consensus, Scite, Inciteful, Dimensions, Google Scholar, patents, grants, and trial registries are methodological suggestions only; the CLI does not log in to or scrape them.
- **Filesystem:** project files and optional `--out`, `--cuefile`, and `--scores` paths are restricted to the selected project directory. API caches are bounded and stored in `project/.cache/`.

## 🔒 Security, privacy, and evidence limits
- Only the query and API requests needed for the selected engines leave the machine. The CLI does not read credentials, run shell commands, send telemetry, or execute retrieved text.
- API responses, XML, JSON, cache files, project JSON, and user cue/score files are size-bounded and parsed as data. Corrupt caches are ignored and refetched; malformed project files fail without being silently replaced.
- CSV exports neutralize spreadsheet formula prefixes in untrusted titles, abstracts, identifiers, and project fields. Prefer JSON for machine interchange and treat CSV as untrusted presentation data.
- Retries honor transient HTTP failures and bounded `Retry-After` values. A failed engine is reported and skipped; if all engines fail and no prior evidence exists, `search` exits 2.
- `extract` emits source-linked **candidate** statements only. A candidate with no valid DOI/accession is exploratory; an empty/bounded search never establishes that no literature exists.
- `validate` checks identifier syntax. `validate --check-web` resolves supported DOI/PMID/Europe PMC/arXiv identifiers. Only a complete web check with at least two independent source labels can produce High confidence; otherwise confidence is capped.

## 🚀 Quick start
```bash
python3 scripts/research_gap_cli.py init --dir proj --topic "My topic" \
  --pico '{"population":"...","outcome":"..."}'
python3 scripts/research_gap_cli.py search --dir proj --query "My topic" \
  --engines openalex,semantic,crossref,europepmc,pubmed,arxiv --limit 50 --years 2018 2026
python3 scripts/research_gap_cli.py extract --dir proj
python3 scripts/research_gap_cli.py classify --dir proj
python3 scripts/research_gap_cli.py validate --dir proj --check-web
python3 scripts/research_gap_cli.py rank --dir proj --min-total 9 --min-confidence medium
python3 scripts/research_gap_cli.py report --dir proj --top 8
```

For automation, `init`, `search`, `validate`, `rank`, and `status` accept `--json` and emit one JSON result object. Search results retain exact key-free request URLs plus query/engine/year/limit provenance. The persistent `evidence.json` and `gaps.json` files have `schema_version`, provenance, confidence, verification, and explicit estimate fields. Formal output contracts are in `schemas/`.

Custom extraction cues and score overrides are project-relative JSON files:
```json
{"cues": ["future direction", "not evaluated in primary care"]}
```
```json
{"gap-abc123": {"theoretical": 2, "practical": 3, "feasibility": 2, "novelty": 2, "coherence": 3}}
```

## 📚 Included
- `SKILL.md` — methodology, workflow, evidence limits, and CLI contract.
- `resources.md` — research-gap framework and tool catalog.
- `references.md` — checked authoritative methodology, API, schema, security, and information-integrity sources.
- `AGENT_GUIDE.md` — compact, model-agnostic JSON hand-off and token-efficient interpretation rules.
- `schemas/` — machine-readable contracts for evidence and gap files.
- `scripts/research_gap_cli.py` — stdlib-only CLI (`init/search/extract/classify/validate/rank/report/status/selftest`).
- `scripts/verify_integrity.py`, `tests/test_cli.py`.

## ✅ Verification
```bash
python3 -m unittest discover -s tests -v
python3 scripts/research_gap_cli.py selftest
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```

**Canonical artifact SHA-256:** `3cec277ae17009b85b2731a46c56efd43978804f2215bcf705db1302a946fcd6`

## License
MIT-0. See `skill-card.md` and `resources.md` for references.
