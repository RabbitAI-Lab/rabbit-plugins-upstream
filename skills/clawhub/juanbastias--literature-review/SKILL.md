---
name: literature-review
description: Plan and document academic literature searches, verify source identifiers, and synthesize a cited review using available research tools.
license: MIT-0
---

# Literature Review

## Contract

This package is a self-contained research procedure, not an executable multi-database search integration. It includes no Python search helper. Do not invent `lit_search.py`, install dependencies, request API keys, or claim automatic deduplication or full abstracts on its behalf.

## Workflow

1. Define the review question, population or topic, date range, study types, and inclusion/exclusion criteria. Record them in the review notes before searching.
2. Choose available research tools and appropriate source databases. PubMed covers biomedical literature; Crossref provides DOI metadata; OpenAlex and Semantic Scholar provide scholarly discovery. Check each source's current access requirements. Record which sources were actually searched and any unavailable ones.
3. Build source-specific queries. Save the exact query, filters, search date, retrieved count, and relevant identifiers. Use only an existing verified connector or source website. Report a missing integration instead of pretending to execute a command.
4. Screen results against the criteria. Deduplicate verified DOI/PMID records; when those are absent, compare title, authors and year and flag uncertain matches. No automatic deduplication is bundled.
5. Retrieve available abstracts or full text. Record the evidence level of each item. Missing abstracts remain missing; never reconstruct scientific findings from title alone.
6. Extract study design, population, methods, outcomes, limitations and funding from the available evidence. Separate preliminary findings, observational associations and causal conclusions.
7. Synthesize by theme with source-level citations and disagreements. Verify DOI/PMID and bibliographic details before delivery. Citation counts are not a substitute for evidence quality.

## Output

Produce a local search log, screened source table and cited draft as requested. Each source row should include title, authors, year, database, DOI/PMID when available, evidence actually accessed, inclusion decision and limitations. Do not claim a systematic review or complete coverage without the corresponding protocol and reproducible searches.

## Verification and boundaries

- Every factual synthesis claim must be traceable to evidence actually accessed.
- State source failures, missing full text and incomplete coverage.
- No patient identifiers, private files or credentials in public search queries.
- Research assistance is not individualized diagnosis or treatment.
- No installation, publication, upload, email or submission is authorized by this skill.
