# Verification details (v1.9)

Full semantics of every check `verify_refs.py` performs. SKILL.md keeps the
short version; this file is the complete reference.

## Cross-check rules by identifier

- **DOI** (v1.4+): DOI.org content negotiation returns the registered CSL
  metadata. Title similarity < 0.50 → `invalid` ("real DOI, wrong paper" —
  fabricated or mis-cited); 0.50–0.82 → `partial` (human review); ≥ 0.82 →
  consistent. Year difference ≥ 2 adds a warning note. A DOI the registry has
  never heard of (404) → `invalid`, never `unreachable`.
- **PMID**: NCBI E-utilities esummary. PubMed's own web pages return 2xx even
  for nonexistent PMIDs, so only the API actually catches fabrications.
- **DOI ↔ PMID cross-check** (v1.6): when both keys are present, the PMID's
  registered DOI must match the claimed DOI — a mismatch is `invalid`
  ("stitched fake": each key real, pointing at different papers).
- **Journal name** (v1.6): claimed source vs DOI-registered container-title.
  NLM-style abbreviations are treated as equivalent (word-initial sequential
  match, stop-words skipped); cross-language names are not comparable and are
  skipped. A real mismatch downgrades to `partial` (journals do rename).
- **Author names** (v1.7): claimed surnames matched against the CSL author
  list; any hit counts (spelling variants tolerated); single-letter initials
  never substring-match (APA "Torvalds, L." would otherwise match any "G.").
  CJK-vs-Latin names are skipped (not comparable). A full miss downgrades to
  `partial`.
- **arXiv** (v1.5): official export.arxiv.org API (≥3 s/request politeness
  pause). Unknown ID or API error element → `invalid`. Same 0.50/0.82
  similarity thresholds as DOI.
- **Retraction** (v1.8): Crossref REST API `updated-by[]` (Retraction Watch
  data, updated daily). Any `type == "retraction"` → capped at `partial` +
  human-review flag. Check failures are silently skipped — never penalize a
  reference for the checker's network.
- **OpenAlex bibliographic check** (v1.8, v1.9 keys): for references without
  DOI/PMID/arXiv, title search against OpenAlex. Best of full/prefix title
  similarity ≥ 0.82 → "confirmed exists"; 0.60–0.82 → "near match, review";
  below → honest "no obvious match, not evidence of fabrication" (coverage
  lag). HTTP 403 → actionable hint to configure `--openalex-key` /
  `OPENALEX_API_KEY` (OpenAlex requires API keys for production use since
  2026-02; keyless calls still work within a free allowance).
- **Semantic Scholar third source** (v1.9): when a DOI reference's DOI.org
  metadata could not be fetched (network restricted / transient 5xx), the DOI
  is re-queried at the S2 Graph API. Confirmation (title similarity ≥ 0.82)
  adds a second-source note and enables the anti-bot rescue below. S2 record
  quality is uneven (real papers registered as journal ToC pages have been
  observed), so **S2 never speaks negatively**: mismatches and misses are
  silent. Optional `--s2-key` / `S2_API_KEY` (keyless shares a rate pool;
  client paces ≥1.5 s between S2 calls).

## Rescue rules (anti-bot, anti-flaky-network)

- Landing page 403/429 but registry metadata confirmed (DOI.org, arXiv, or
  S2): existence is proven, so the reference is NOT `unreachable` — it is
  judged on tier/fields like any 200 page (trusted tier + complete fields →
  `verified`; any partial adjustment or missing field → `partial`). This
  prevents "metadata confirmed + 403 blog page" from slipping through.
- arXiv resolver 404 with unconfirmed metadata → `invalid` (official registry
  says no such ID).
- Wayback Machine (v1.5): every `unreachable` link is checked against
  archive.org; an archived copy adds a dated comparison link for human review.

## Rate limiting & resilience

- Host circuit breaker (v1.6): 2 consecutive *transport* failures
  (timeout/DNS/refused) → remaining calls to that host are skipped for the
  batch with an honest note. HTTP responses (403/404/429…) never trip it.
  Retries within one logical call count once.
- Transient failures retry once; error notes carry the cause (timeout / DNS /
  refused) and the fix (`--timeout 20` for slow links).
- 429 with `Retry-After` (v1.9): the DOI metadata check waits the requested
  duration (capped at 5 s) before its retry.
- `--mailto you@lab.edu` (v1.9): appended to Crossref requests — enters the
  Crossref polite pool with more generous rate limits. Recommended for CI and
  institutional batches. arXiv politeness (3 s/request) and S2 pacing (1.5 s
  keyless) are always on.

## Exports

- `--export bibtex`: verified-only bibliography, Zotero/EndNote-ready (PMID /
  arXiv eprint noted). Field values sanitized (brace/newline stripped).
- `--export csv`: full audit ledger (all refs, all fields, formula-injection
  neutralized, utf-8-sig for Excel).
- `--export auditjson` (v1.9): machine-readable working paper — per reference,
  which checks ran and what they found (`checks_catalog` documents every check
  type), plus a generation timestamp. Purpose: transparency and institutional
  audit. The July 2026 arXiv survey of citation checkers (arXiv 2607.22693)
  found none of five evaluated tools reliable enough to run unsupervised and
  calls for "transparent multi-source detection systems" — the audit trail is
  this skill's answer: a human can re-trace every mechanical verdict.

## BibTeX input (v1.9)

`--refs bibliography.bib` is auto-detected (extension `.bib`, or content
starting with `@` when JSON parsing fails). Minimal pure-stdlib parser:
`@article`/`@inproceedings`/`@book`/`@misc` and other entry types, nested
braces, quoted and bare values, `@comment`/`@preamble`/`@string` skipped.
Mapped fields: title, author (` and ` → `, `), year, journal/booktitle/
journaltitle/publisher → source, doi, url (including `\url{...}` macros in
howpublished/note), pmid, eprint+archivePrefix → arxiv. Unparseable entries
degrade to missing-field references and are judged honestly by the normal
pipeline; zero entries → actionable error.

## Verdict meanings (unchanged since v1.3)

| Verdict | Meaning | Score |
|---|---|---|
| `verified` | reachable + trusted tier + fields complete | +10 |
| `partial` | reachable but community tier / field or metadata concerns | +4 |
| `unreachable` | fetch failed — needs human check, ≠ nonexistent | 0 |
| `unverified` | skipped (`--offline`) | −2 |
| `invalid` | no identifier, registry says no, or stitched fake | −8 |
