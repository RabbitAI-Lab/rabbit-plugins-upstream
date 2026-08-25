# 🔍 Research Gap Finder

**Category:** research, knowledge

Turns a broad topic into a ranked, citation-backed list of genuine research gaps with a candidate
research question per gap.

## 🔐 Permissions & requirements
- **Runtime:** Python 3.8+ (stdlib only) and `curl` — no packages, no API keys for the automated core.
- **Network (key-free):** OpenAlex, Semantic Scholar, Crossref, Europe PMC, PubMed E-utilities, arXiv.
- **Network (guided, needs accounts):** Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace,
  Consensus, Scite, Inciteful, Dimensions, Google Scholar, Patents.
- **Filesystem:** reads/writes only inside the project dir it is given (`config.json`, `evidence.json`,
  `evidence_matrix.csv`, `gaps.json`, `gaps.csv`, `report.md`, `.cache/`).

## 🔒 Security & privacy
- Only your own queries leave the machine; no telemetry; no secrets read/stored/logged.
- API/rate-limit failures never abort the run; raw responses are cached under `.cache/`; a fully offline
  run degrades to gaps labeled `Exploratory/Hypothetical`.
- **Zero-invented citations:** no source is reported without a resolvable identifier. Browser tools must
  be used within their ToS, and don't upload proprietary/sensitive data to untrusted services.
- Risk: AI-summarized "gaps" can be wrong → honesty rules require DOI/Crossref verification and confidence
  caps. A missing paper may be a search artifact → cross-check with the AHRQ framework first.

## 🚀 Quick start
```bash
python3 scripts/research_gap_cli.py init --dir proj --topic "My topic"
python3 scripts/research_gap_cli.py search --dir proj --query "My topic"
python3 scripts/research_gap_cli.py extract --dir proj
python3 scripts/research_gap_cli.py classify --dir proj
python3 scripts/research_gap_cli.py validate --dir proj --check-web
python3 scripts/research_gap_cli.py rank --dir proj --min-total 9
python3 scripts/research_gap_cli.py report --dir proj --out report.md
```

## 📚 Included
- `SKILL.md` — methodology + CLI workflow, taxonomy, rubric, honesty rules.
- `resources.md` — the 100-resource gap-finding catalog.
- `scripts/research_gap_cli.py` — stdlib-only CLI (`init/search/extract/classify/validate/rank/report/status/selftest`).
- `scripts/verify_integrity.py`, `tests/test_cli.py`.

## ✅ Verification
```bash
python3 scripts/verify_integrity.py
sha256sum -c CHECKSUMS.sha256
```
**Canonical artifact SHA-256:** `005894fe00112f8c99adacc24d5fe297434b0782e00d618c349075bc1610c735`

## License
MIT-0. See `skill-card.md` and `resources.md` for references.
