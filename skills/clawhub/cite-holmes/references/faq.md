# FAQ (moved out of SKILL.md in v1.9 to keep the main guide short)

**Q: Is a `verified` citation guaranteed real?**
No. The mechanical layer catches machine-checkable fakes: nonexistent DOIs,
fabricated PMIDs (via E-utilities), fabricated arXiv IDs (via the official
arXiv API), dead links, duplicates, stitched DOI↔PMID pairs, wrong-paper
DOIs (title similarity), and retracted papers. A fabricated citation pointing
to a real, plausible page still relies on the semantic layer — never a
guarantee.

**Q: How are arXiv references checked?**
Same treatment as DOIs since v1.5: the official export.arxiv.org API returns
the registered title/year; similarity below 0.50 → `invalid` (fabricated or
wrong ID), 0.50–0.82 → `partial` (human review), above → consistent. An ID the
API has never heard of is `invalid`, not `unreachable`.

**Q: What do I do with `unreachable` references?**
Open them manually once — the report automatically attaches a Wayback Machine
archive link when one exists. If it matters and keeps failing, switch sources.

**Q: Did the PMID check fail because of my network?**
No. "不存在/编造" verdicts come from the official E-utilities API — that means the
PMID genuinely isn't in PubMed. Only "校验失败" wording means a network/API issue
(the reference is then treated as reachable and flagged).

**Q: Do I always need `--profile medical`?**
Use `--easy`: one flag auto-detects medical references, enables the medical
profile, and exports BibTeX + CSV automatically. For real clinical
conclusions, still prefer explicit `--profile medical`.

**Q: Can verified references go straight into my paper?**
Yes: `--export bibtex` exports only `verified` entries (with PMID / arXiv
eprint notes) and imports into Zotero/EndNote; `--export csv` is the full
audit ledger for advisors and editors; `--export auditjson` (v1.9) is the
machine-readable per-check working paper for institutional audit.

**Q: Which services does verification touch, and what if my network is slow or blocked?**
DOI.org (DOI metadata), NCBI E-utilities (PMID), export.arxiv.org (arXiv
metadata), archive.org (archived copies), api.crossref.org (retractions),
api.openalex.org (bibliographic confirmation), api.semanticscholar.org (third
source, v1.9). CN networks occasionally throttle several of them. The verifier
never stalls: transient failures retry once (429 honors `Retry-After`), error
notes tell you the cause with a fix (`--timeout 20` for slow links), and a
host-level circuit breaker skips a host after 2 consecutive transport
failures — with an honest note — instead of hanging the batch. Degraded
checks are always labeled, never silently dropped.

**Q: Do I need API keys?**
No — everything runs keyless within public rate limits. OpenAlex has required
keys for *production* use since 2026-02 (free daily allowance; this skill
survives keyless but benefits from `--openalex-key` / `OPENALEX_API_KEY`).
Semantic Scholar keyless shares a rate pool; `--s2-key` / `S2_API_KEY` gets a
dedicated lane. Crossref asks heavy users to identify themselves — pass
`--mailto you@lab.edu` to join the polite pool.

**Q: Can I verify references straight from my reference manager?**
Yes, since v1.9: `--refs bibliography.bib` reads Zotero/EndNote/JabRef BibTeX
exports directly (entry types, nested braces, `\url{}` macros; DOI/PMID/arXiv
fields are picked up automatically).
