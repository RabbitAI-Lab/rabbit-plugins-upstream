# Evidence and implementation references

Checked 2026-09-06. These links ground the implementation and the claims in `SKILL.md`; they are not a substitute for checking an API response at run time.

## Research-gap and reproducibility methodology

- [AHRQ, Research Gaps](https://effectivehealthcare.ahrq.gov/products/methods-future-research-steps-framework/research) — characterize a gap by the question/PICOS and why existing evidence is missing or inadequate; absence alone is not a conclusion.
- [PRISMA-S](https://pmc.ncbi.nlm.nih.gov/articles/PMC7839230/) — report database/platform, complete strategies, limits, dates, counts, and search flow so a search can be reproduced and updated.

## Scholarly API behavior

- [OpenAlex API reference](https://help.openalex.org/api/) — key-free REST access, `select` fields, search/filter/sort, and external text should be treated as untrusted.
- [OpenAlex paging](https://help.openalex.org/api/paging/) — use `per_page` 1–100; cursor paging is for larger traversals and should be bounded for this CLI.
- [OpenAlex field selection](https://help.openalex.org/api/selecting-fields/) — `select` is supported on list endpoints for lower transfer volume.
- [Semantic Scholar Academic Graph API](https://api.semanticscholar.org/api-docs/graph) — paper search supports bounded `limit` and requested fields; API keys, when used, belong in an `x-api-key` header, which this key-free CLI intentionally does not read.
- [Crossref REST access and authentication](https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/) — use polite identification and respect service limits; the CLI uses HTTPS, an identifying User-Agent, bounded rows, and retry handling without inventing an email address.
- [Europe PMC RESTful API](https://europepmc.org/RestfulWebService) — the search service supports JSON result lists, page sizes, and query date fields; the CLI bounds page size and records the query.
- [NCBI E-utilities in depth](https://www.ncbi.nlm.nih.gov/books/NBK25499/) — ESearch/ESummary parameters and date ranges; the CLI includes a tool name, keeps requests below a conservative interval, and does not read an API key.

## Structured output, security, and information integrity

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12/json-schema-validation) — explicit types, required fields, and bounded contracts for machine-readable files; local runtime remains stdlib-only.
- [NIST AI 600-1 GenAI Profile](https://airc.nist.gov/docs/NIST.AI.600-1.GenAI-Profile.ipd.pdf) — confabulation is confidently stated erroneous or unsupported content; source verification and uncertainty labels are therefore explicit.
- [OWASP GenAI LLM Top 10, 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) — current guidance for prompt injection, insecure output handling, sensitive disclosure, denial of service, and overreliance; retrieved scholarly text is data, never executable instructions.
