## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora, including company filings, extracted sections, normalized financials, insider transactions, and institutional holdings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to prepare sourced SEC filing briefs and period-aware company or disclosure comparisons. It helps resolve entities, retrieve filings and sections, compare reported facts, and inspect financials, insider transactions, institutional holdings, and XBRL frames.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when Crawlora is an acceptable processor for the intended filings work, and keep the API key in the agent environment rather than in prompts, files, or command history.

Risk: The /web/scrape fallback can send public URLs outside the core SEC filing endpoints to Crawlora.

Mitigation: Use /web/scrape only for SEC filing source URLs or other public URLs the user explicitly intends to process through Crawlora.

Risk: Truncated filing sections, lagging datasets, amendments, restatements, or delayed 13F reporting can support incomplete conclusions.

Mitigation: Preserve source URLs, reporting periods, retrieval time, data-as-of dates, and explicit gaps; verify comparable periods and do not make buy or sell conclusions from filing lookup alone.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [SEC EDGAR application programming interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with cited SEC source links and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include entity and CIK, accession, form, filing date, reporting period, cited section or fact, source URL, retrieval time, and calculations.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
