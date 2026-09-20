---
name: pubmed-verifier
license: MIT-0
version: 2.2.1
description: >-
  Batch-verify PMID citations against PubMed and catch the hallucination that
  existence checks miss: a REAL PMID pointing to a DIFFERENT paper (the most
  common AI-fabricated citation). Five-state verdicts (correct / mismatch /
  partial / invalid / unknown), citation-context parsing, dual fuzzy matching,
  Crossref DOI cross-check, correct-PMID suggestion, SQLite cache, CSV/JSON
  claims, HTML/JSON/text reports. Dual data sources with automatic Europe PMC
  fallback, optional NCBI API key (3x faster batches), Crossref polite pool,
  Retry-After backoff, UA rotation, host circuit breaker. Network failures are
  honestly reported as unverified, never as "not found". Zero dependencies,
  runs fully local. Triggers: verify PMIDs, check citations, validate
  references, citation audit, reference check, PMID check, audit references,
  batch verify references, AI hallucination detection, verify DOI, DOI check,
  validate citations, PubMed citation verifier.
---

# PubMed Citation Verifier v2.2.0

Batch verification of PMID citations via the PubMed E-utilities API. Not just
"does this PMID exist" — **does this PMID point to the paper you claim?**
Zero dependencies, pure standard library, fully local.

## The five-state verdict

| Verdict | Meaning |
|---------|---------|
| ✅ Correct | PMID exists AND matches the claimed paper |
| ⚠️ Mismatch | PMID exists but points to a **different** paper (the most common AI hallucination!) |
| 🔶 Partial | Some metadata matches (e.g. author+journal but title differs) |
| ❌ Invalid | PMID does not exist in PubMed |
| ❓ Unknown | Not enough claimed metadata to cross-check — or both data sources unreachable (never misreported as invalid) |

**Why existence checks are not enough:** a large share of fabricated
citations use REAL PMIDs that point to a different paper from the same
year/journal/field — in one of our own audits, 4 of 5 "valid" PMIDs were
wrong this way. A binary exists/not-exists check misses them all.

## Quick start

```bash
# Scan a project directory for PMIDs (parses citation context automatically)
python3 scripts/verify_pmids.py --source /path/to/project --output report.html

# Verify specific PMIDs
python3 scripts/verify_pmids.py --pmids 31018962,22213727

# Mismatch demo: PMID 34078778 is actually a dental-materials paper, so the
# JIA claims below will NOT match it — expect ⚠️ mismatch verdicts
python3 scripts/verify_pmids.py --claims '[{"pmid":"34078778","title":"JIA pathogenesis","authors":["Zaripova"],"journal":"Pediatr Rheumatol Online J","year":"2021"}]' --output report.html

# Claims from a CSV file + suggest correct PMIDs for mismatches
python3 scripts/verify_pmids.py --claims-file claims.csv --suggest --output report.html

# Crossref DOI cross-verification + full pipeline
python3 scripts/verify_pmids.py --source /path/to/files --verify-doi --suggest --output report.html

# Institutional niceties (recommended): NCBI API key + contact email
python3 scripts/verify_pmids.py --source . --verify-doi --ncbi-api-key $NCBI_API_KEY --mailto you@lab.org
```

## v2.2.0 — network hardening

| Feature | Flag | Effect |
|---------|------|--------|
| NCBI API key | `--ncbi-api-key` / env `NCBI_API_KEY` | Rate ceiling 3→10 req/s, batch interval 0.4s→0.12s (~3x faster) |
| Europe PMC fallback | `--meta-source auto\|ncbi\|europepmc` | NCBI batch failure automatically retries via Europe PMC (free, no key); per-entry origin in JSON (`meta_source`) |
| Crossref polite pool | `--mailto` / env `PUBMED_VERIFIER_MAILTO` | `?mailto=` on Crossref + tool/email params on NCBI — more generous limits |
| Retry-After backoff | automatic | 429 responses honored (clamped 1–5 s) instead of failing |
| UA rotation | automatic | 403/406 retried with a browser User-Agent |
| Host circuit breaker | automatic | After 2 call-level transport failures a host is skipped with an actionable message; success resets; HTTP errors never trip it |
| Honest unknown | automatic | Network failures report as ❓ unknown + exit code 2, never as "PMID not found", and are never cached |

**Exit codes:** `0` clean · `1` invalid/mismatch found · `2` could not verify
(data sources unreachable) — automation can tell "all good" from "no answer".

## How it works

1. **Extract + parse context** — finds `PMID: 12345678` / PubMed URLs in
   `.html .md .txt .htm .json`, and parses the surrounding reference into
   claimed authors / title / journal / year.
2. **Fetch metadata (cached)** — PubMed esummary in batches of 50, SQLite
   cache (30 days, `--cache-days`), 3 retries with backoff.
   Europe PMC steps in per failed batch when NCBI is unreachable.
3. **Cross-check claimed vs actual** — dual fuzzy matching: word-level
   Jaccard overlap ≥ 50% OR SequenceMatcher ≥ 90% on titles; author surname
   hits; journal containment; exact year.
4. **Crossref DOI verification** (optional `--verify-doi`) — resolves each
   cited DOI via Crossref and compares the registered title with the PubMed
   record (`doi_title_match` in JSON). A `doi_verified: false` with note
   "crossref unreachable" is a network fact, not a verdict.
5. **Suggest the right PMID** (optional `--suggest`) — for mismatches,
   searches PubMed with the claimed metadata and proposes top-3 candidates.
   (Suggestion search always uses NCBI, even with `--meta-source europepmc`.)

Context parsing is heuristic — abbreviations like "U.S." can split a title
early. For precise verification, feed structured claims via `--claims-file`.

| Report | Flag | Use |
|--------|------|-----|
| HTML | `--output report.html` | Human review: claimed vs actual side by side |
| JSON | `--output report.json` | Programmatic processing (includes `meta_source` per entry) |
| Text | default | Quick terminal look |

## Performance

Measured on a 225-PMID audit (5 esummary batches): metadata-only verification
runs in seconds; cached re-runs take ~5 s. Each batch waits 0.4 s between
calls (0.12 s with `--ncbi-api-key`). Optional extras are per-citation:
`--verify-doi` adds one Crossref call (~0.5–1 s) per cited DOI, and
`--suggest` adds one PubMed search per mismatch.

## When to use which tool

- **pubmed-verifier (this skill)** — fast, batch, targeted: I have a list of
  PMIDs/DOIs and need to know if they are real and correctly cited.
- **cite-holmes** — deep research: interrogate every citation of a whole
  document across multiple databases, with graded confidence reports.

They share the same five-state philosophy and are safe to use together.

## Use cases

- Systematic review / meta-analysis reference audits
- Verifying citations in AI-generated content
- Pre-submission self-check of a manuscript's reference list
- Medical knowledge base / teaching material QA
- Pharmacovigilance literature verification

## Related skills (Paper Toolbox family)

- **cn-med-oa** — free Chinese medical literature full-text download & metadata
- **cite-holmes** — deep research with machine-verified citations
- **paper-polisher** — academic polishing, terminology & journal precheck
- **academic-figures** — publication-ready scientific figures in one command
- **doc-holmes** — layout-preserving PDF translation (in testing)

Workflow: cn-med-oa (get papers) → pubmed-verifier / cite-holmes (verify
citations) → paper-polisher (polish) → academic-figures (figures) →
doc-holmes (translate PDFs).

## Files

| File | Purpose |
|------|---------|
| `scripts/verify_pmids.py` | Main verifier (v2.2.0, stdlib-only) |
| `references/api_examples.md` | PubMed / Europe PMC / Crossref API notes |
| `tests/` | Offline matrix + real-network acceptance (repo only, not in the package) |

## License

MIT-0 — free to use, modify and redistribute, no attribution required.
