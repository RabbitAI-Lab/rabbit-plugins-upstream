## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora, including company filings, extracted sections, normalized financials, insider transactions, and institutional holdings, for sourced filing briefs and period-aware company or disclosure comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to resolve EDGAR entities, retrieve SEC filings and sections, compare disclosures across periods, and produce sourced filing briefs. It also guides use of normalized financials, insider disclosures, institutional holdings, and dataset snapshots while preserving reporting-period context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call broader Crawlora API paths than the SEC-focused workflow requires.

Mitigation: Use it with trusted prompts and keep calls within the documented SEC and dataset endpoints unless broader access is deliberately reviewed.

Risk: A configurable API base can send the Crawlora API key to an unintended endpoint.

Mitigation: Keep CRAWLORA_API_BASE unset during normal use and only set it for trusted test endpoints.

Risk: Request bodies, query parameters, or scrape URLs can expose sensitive private data.

Mitigation: Avoid passing confidential material through the helper or scrape requests.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with sourced filing facts, links, calculations, and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include entity and CIK, accession, form, filing and reporting dates, cited sections or facts, source URLs, retrieval time, calculations, and explicit evidence gaps.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
