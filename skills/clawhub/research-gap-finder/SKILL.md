---
name: research-gap-finder
description: "Find genuine research gaps in a topic and output a ranked, citation-backed gap report with a candidate research question per gap. Uses a stdlib-only CLI over key-free scholarly APIs (OpenAlex, Semantic Scholar, Crossref, Europe PMC, PubMed, arXiv) plus a guided human-in-the-loop layer (Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace, Consensus, Scite, Inciteful, Dimensions). Grounded in gap frameworks (PICO/PICOS, six-type taxonomy, five-dimension importance rubric, AHRQ, Robinson, Arksey-O'Malley) with bibliometric mining and a zero-invented-citation honesty protocol."
version: 2.0.2
categories: [research, knowledge]
topics: [research-gaps, literature-review, systematic-review, citation-analysis, academic-research]
metadata:
  openclaw:
    emoji: "🔍"
    requires:
      bins: ["python3", "curl"]
      python: [stdlib]
      apis: ["OpenAlex, Crossref, Europe PMC, PubMed E-utilities, arXiv, Semantic Scholar are key-free; Elicit, SciSpace, Scite, Dimensions and most citation-map tools need accounts/API keys"]
    network:
      outbound: ["api.semanticscholar.org", "api.crossref.org", "api.openalex.org", "www.ebi.ac.uk", "eutils.ncbi.nlm.nih.gov", "export.arxiv.org", "api.biorxiv.org", "api.medrxiv.org", "api.ssrn.com", "api.elsevier.com", "api.incites.clarivate.com", "litmaps.com", "researchrabbit.ai", "connectedpapers.com", "elicit.com", "scispace.com", "consensus.app", "scite.ai", "inciteful.xyz", "dimensions.ai", "scholar.google.com", "patents.google.com"]
---

# 🔍 research-gap-finder

Turn a topic into a ranked, citation-backed list of genuine research gaps, each with a candidate research question.

Two layers:
- **Automated (CLI)** — build an evidence matrix and classify/score/validate gaps via key-free APIs. Stdlib-only, Python 3.8+, no keys.
- **Guided (human-in-the-loop)** — browser tools (Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace, Consensus, Scite, Inciteful, Dimensions) plus grants/patents/trials; use within their ToS and don't upload proprietary data.

**Honesty guarantee:** a gap is never credited to a source without a resolvable identifier (DOI/accession); unverifiable items are flagged `Exploratory/Hypothetical`.

## When to use
Broad-topic or understudied-angle scanning for proposals, literature-review chapters, or "state of the field" briefs.

## 1 · Automated pipeline

```bash
python3 scripts/research_gap_cli.py init     --dir proj --topic "T" [--pico '{"population":"...","outcome":"..."}']
python3 scripts/research_gap_cli.py search   --dir proj [--query "T"] [--engines openalex,semantic,crossref,europepmc,arxiv] [--limit 100] [--years 2018 2026]
python3 scripts/research_gap_cli.py extract  --dir proj [--cuefile cues.json]
python3 scripts/research_gap_cli.py classify --dir proj [--scores scores.json]
python3 scripts/research_gap_cli.py validate --dir proj [--check-web]
python3 scripts/research_gap_cli.py rank     --dir proj [--min-total 9] [--min-confidence medium] [--top N]
python3 scripts/research_gap_cli.py report   --dir proj [--top 8] [--out report.md]
python3 scripts/research_gap_cli.py status   --dir proj
python3 scripts/research_gap_cli.py selftest
```

| Command | Result |
|---|---|
| `init` | `config.json` (topic, PICO, engines, years, limit, cache flags) |
| `search` | Queries chosen engines; dedupes by DOI/title; appends to `evidence.json` + `evidence_matrix.csv`; caches raw responses in `proj/.cache/`. A live API failure is skipped, never aborts. Fully offline → gaps labeled `Exploratory/Hypothetical`. |
| `extract` | Pulls gap-cue sentences (limitations/future-work/absence) into candidates; never fabricates one if none is found. |
| `classify` | Tags six-type taxonomy + five-dimension rubric scores (each 0–3, total /15). Baseline scores are marked `estimated`; override per gap via `scores.json`/`--scores`. |
| `validate` | Resolves sources via Crossref (or marks identifiers) and sets confidence: High = ≥2 independent sources & resolved; Medium = 1 source; Low = no resolvable source → `Exploratory/Hypothetical`. |
| `rank`/`report` | Sort by importance × confidence; emit the Markdown gap report. |
| `status`/`selftest` | Project state; offline self-test. |

## 2 · Guided methodology (adds depth)

1. **PICO/PICOS** — define Population, Intervention, Comparison, Outcome, Setting; store in `config.json`.
2. **Recent systematic reviews** — pull 3–5 from PubMed/Cochrane/Scopus; combine with automated results.
3. **Explicit gap cues** — read each review's *Limitations/Future Directions*; log Source, Gap type, Evidence (CLI `extract` automates cue detection).
4. **Citation networks** — Litmaps (reference-gap method), ResearchRabbit/Connected Papers (citation "islands").
5. **Semantic "what is unstudied?"** — Elicit/Consensus questions over the topic + population.
6. **Novelty cross-check** — grants (NIH RePORTER, NSF, EU CORDIS), preprints, trials, patents; downgrade already-funded/published gaps.

## 3 · Classify & rank

**Six-type gap taxonomy** (CLI tags via cue lexicon):

| Type | Signal |
|---|---|
| Evidence | insufficient/no/weak evidence, little is known, understudied |
| Methodological | weak design, small sample, no control, outdated instrument, reproducibility |
| Population | demographic/geographic/severity absent, rural, elderly, underrepresented |
| Contextual | setting/real-world/cultural omitted, low-resource, community |
| Theoretical | no explicit theory, conflicting explanations, mechanism, no consensus |
| Translational | not moved to practice/policy, implementation, uptake |

**Five-dimension importance rubric** (0–3 each, max 15):

| Dimension | Question |
|---|---|
| Theoretical | Advances core concepts / resolves contradictions? |
| Practical | Solves a real problem / informs policy-practice? |
| Feasibility | Data, methods, resources realistically obtainable? |
| Novelty | Genuinely unstudied (check preprints, trials, grants)? |
| Coherence | Logical next step of the field's trajectory? |

**13–15** proposal-ready; **9–12** needs feasibility work; **≤8** re-evaluate. Require Feasibility ≥2.

> **Identification ≠ importance.** Filling the "Gap" cell ends identification; importance is judged afterwards. Many gaps are genuine but unimportant.

## 4 · Output report

Per gap: gap statement · type (+ secondary) · source evidence (DOI/resolvable ID) · five-dimension importance + total · confidence · candidate research question.

### Honesty & anti-hallucination (non-negotiable)
1. **Zero-invented citations** — every gap traces to a resolvable source; otherwise it is `Exploratory/Hypothetical` (a hypothesis, never a citation-backed claim). The CLI enforces this by only emitting sources with a DOI/accession.
2. **Separate identification from importance** — run the rubric; never present a trivial absence as valuable.
3. **Label confidence** — AI-assisted findings unverified by a review cap at Medium.
4. **No invented trends** — if literature is sparse, say "insufficient literature to determine trends".
5. **Absence ≠ algorithm failure** — a missing paper may be a search artifact; cross-check with the AHRQ framework first.
6. **Verify every citation you output** — resolve DOIs/titles via Crossref (`validate`) before writing; never emit an unresolvable citation.

## 5 · Catalog
The full 100-resource catalog (frameworks, tools, databases, strategies, key papers) is in `resources.md`.

---
*Authored and hardened with the repo's AI multi-model team; published under the Skill Publishing Standard.*
