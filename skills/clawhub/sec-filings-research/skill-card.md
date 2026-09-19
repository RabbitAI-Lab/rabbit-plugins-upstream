## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora, including company filings, extracted sections, normalized financials, insider transactions, and institutional holdings. Use for sourced filing briefs and period-aware company or disclosure comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to retrieve and compare SEC EDGAR filings, filing sections, normalized financial statements, insider transactions, and institutional holdings with source links and period context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC research queries, selected URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only where that data sharing is acceptable, keep the API key in the environment, and avoid private URLs or sensitive text.

Risk: The /web/scrape endpoint can fetch broader public URLs beyond SEC-native endpoints.

Mitigation: Keep scraping limited to SEC filings or directly relevant public source documents.

Risk: Filing excerpts, normalized financials, and stored datasets can be truncated, delayed, or reflect restatements.

Mitigation: Preserve source URLs, dates, reporting periods, truncation indicators, and degraded fields; avoid unsupported investment conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/sec-filings-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [SEC EDGAR application programming interfaces](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or text briefs with cited filing facts, source URLs, calculations, and optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include entity and CIK identifiers, accession numbers, forms, filing dates, reporting periods, retrieval time, and explicit evidence gaps.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
