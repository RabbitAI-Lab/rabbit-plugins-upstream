---
name: cite-holmes
license: MIT
description: >-
  Deep research that interrogates its own sources (Verified Deep Research):
  calibrates scope first (3-5 sharp questions), plans sub-questions, searches
  iteratively across sources and languages, then machine-verifies every
  citation (verified / partial / unverified / unreachable / invalid) before a
  confidence-graded report ships. Never outputs unverified references;
  fabricated DOIs, dead links and missing sources are first-class catch
  targets. Medical evidence mode (Cochrane/BMJ/ClinicalTrials/NMPA/CDC/NICE/Wanfang 
  Wanfang tier presets, PMID existence check via NCBI E-utilities) and
  verified-bibliography export (BibTeX + audit CSV) built in.
when_to_use: >-
  Use when the user says "deep research", "look into", "investigate",
  "compare A vs B", "fact check", "verify this claim", "is it true that...",
  "check these references", "are these citations real", wants a research
  report with sources, a literature review, a medical evidence lookup, or
  wants references verified before submission — even if they never say the
  word "research".
---

# cite-holmes (Cite Holmes): deep research with citation verification

One line: **a question goes in — a verified report comes out.**

Three differences from a plain "search and summarize":

1. **Calibrate before working** — ask sharp questions first; the most expensive
   waste is researching the wrong question.
2. **Conclusions carry evidence grades** — 🟢 two independent sources agree /
   🟡 single authority / 🔴 contested.
3. **Every citation is checked** — mechanical layer (reachability, domain
   authority, field completeness, dedup) plus semantic layer (does the source
   actually support the claim?). Unverified references never masquerade as real.

## ⛔ Iron rules (zero exceptions)

1. **Never fabricate**: citations must come from pages actually fetched this
   session. Re-search rather than write URLs from memory.
2. **Never pretend**: unchecked references are marked `unverified`; fetch
   failures are `unreachable` (≠ nonexistent — flagged for human review).
3. **Don't hide conflicts**: when sources disagree, present the disagreement,
   mark 🔴, show each side's evidence.
4. **Budgeted search**: QUICK ≤6 searches, FULL ≤15. Out of budget → state the
   gaps honestly instead of forcing conclusions.
5. **Calibrate before searching** (FULL mode): scope / timeframe / audience /
   output format must be locked first.

## Step 0: mode selection

| Mode | Fits | Calibration | Budget | Output |
|---|---|---|---|---|
| **QUICK** | Single fact-check: "is this claim true", "when was X released" | skipped | ≤6 | short report |
| **FULL** | Open research: "state of X", "A vs B", "do a survey" | mandatory | ≤15 | full report |

A question answerable by one verifiable fact → QUICK. Needs synthesis or
trade-offs → FULL. "Quick check" forces QUICK; "thorough/comprehensive" forces
FULL. When unsure, default FULL.

## Five-phase workflow

### 1. CALIBRATE (FULL only)

Ask 3–5 high-leverage questions at once (no drip-feeding): scope, timeframe,
audience/depth, output format, decision context. Never re-ask what the user
already provided. If the user declines ("your call"), proceed with stated
defaults.

### 2. PLAN

Show a short plan: 3–7 sub-questions, source priority (primary/official >
major media > community/blog as leads only), budget.

### 3. SEARCH (iterative, not one pass)

**Read `references/search-strategies.md` first** (diamond expansion, source
pyramid, query matrix, gap-driven iteration). Essentials: each round targets
one sub-question; evolve queries with discovered terms; search both English
and Chinese for topics that span both internets; fetch full text of the 2–5
most valuable sources (never conclude from search snippets); verify key
numbers/dates in the original page before quoting.

### 4. VERIFY (the heart of this skill)

Register every reference in `research_refs.json` (schema in
`references/report-template.md`), then verify on two layers:

**Semantic (the model must do this)**: for each reference ask "does the source
page actually support the sentence I cite it for?" → `supports` /
`partial_support` / `not_in_source` (drop or demote).

**Mechanical (run the script)**:

```bash
python scripts/verify_refs.py --refs research_refs.json --out verify_report.md
```

Five verdicts: `verified` / `partial` / `unreachable` (needs_human_check) /
`invalid` / `unverified`. Options: `--offline` (structure check only),
`--strict` (CI), `--profile medical` (medical source presets: Cochrane/BMJ/
ClinicalTrials/NMPA/CDC/NICE/Wanfang 万方 into the journal tier; community-tier
sources flagged "unfit for medical conclusions"), `--export bibtex,csv`
(verified-only BibTeX bibliography for the paper + full audit-CSV ledger).
References may carry `url`, `doi`, or `pmid` (auto-resolves to PubMed) —
and every PubMed URL gets its PMID existence-checked via NCBI E-utilities,
which is what actually catches AI-fabricated PMIDs (PubMed's own page returns
2xx even for nonexistent ones). Dedup covers URL + DOI + PMID.

**Medical research mode (v1.2)**: for clinical questions — drug efficacy,
prevalence, guidelines, diagnosis/treatment claims — read
`references/medical-mode.md` first (source pyramid, PubMed query patterns,
CEBM grade mapping, regulator/trial-registry sources) and run the verifier
with `--profile medical --export bibtex,csv`.

### 5. SYNTHESIZE

Follow the skeleton in `references/report-template.md`: executive summary
first; every key conclusion carries a confidence grade + citation ids; the
reference table carries verdicts; `unverified/unreachable` items live only in
the "human review" section; finish with gaps, disagreements, and follow-up
questions.

## Files

| File | When |
|---|---|
| `scripts/verify_refs.py` | VERIFY phase mechanical check (pure stdlib, cross-platform, rate-limited) |
| `references/search-strategies.md` | read before SEARCH |
| `references/report-template.md` | skeleton for SYNTHESIZE; refs schema |
| `references/medical-mode.md` | read before medical/clinical research (v1.2) |
| `examples/demo_refs.json` | general demo: 8 refs, 3 planted fabrications |
| `examples/medical_refs.json` | medical demo: PMID/DOI refs + planted fake PMID + planted duplicate |

## Honest limits

- A fabricated citation pointing to a real, live, plausible page passes the
  mechanical layer; the semantic layer may catch it — model judgment, not a
  guarantee.
- `unreachable` ≠ fake.
- Reproducible demo: `python scripts/verify_refs.py --refs examples/demo_refs.json`
  (8 refs, 3 planted fabrications, all caught — measured 7.7 s).
- Medical demo: `python scripts/verify_refs.py --refs examples/medical_refs.json
  --profile medical --export bibtex,csv` (real tocilizumab/sJIA references;
  a fabricated PMID is caught via E-utilities, a re-registered duplicate via
  PMID dedup).


## FAQ (common questions)

**Q: Is a `verified` citation guaranteed real?**
No. The mechanical layer catches machine-checkable fakes: nonexistent DOIs,
fabricated PMIDs (via E-utilities), dead links, duplicates. Since v1.4, DOIs are
cross-checked against official DOI.org metadata (title similarity + year), which
also catches "real DOI, wrong paper". A fabricated citation pointing to a real,
plausible page still relies on the semantic layer — never a guarantee.

**Q: What do I do with `unreachable` references?**
Open them manually once; check an archived copy if available. If it matters and
keeps failing, switch sources.

**Q: Did the PMID check fail because of my network?**
No. "不存在/编造" verdicts come from the official E-utilities API — that means the
PMID genuinely isn't in PubMed. Only "校验失败" wording means a network/API issue
(the reference is then treated as reachable and flagged).

**Q: Do I always need `--profile medical`?**
Use `--easy`: one flag auto-detects medical references, enables the medical
profile, and exports BibTeX + CSV automatically.

**Q: Slow access to DOI.org / PubMed from CN networks?**
Both are reachable directly; rate-limiting and transient retries are built in.
Use `--timeout 20` for slow links. If E-utilities is blocked, that step degrades
gracefully and says so in the note.

## Environment fallback

Without web tools: state honestly that only the "user-supplied material +
mechanical verification" mode is possible; never pretend to search.
