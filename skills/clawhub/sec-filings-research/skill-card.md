## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora, including filings, extracted sections, normalized financials, insider transactions, and institutional holdings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and developers use this skill to prepare sourced SEC filing briefs and period-aware comparisons of company disclosures, financials, insider activity, and institutional holdings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: SEC research requests, requested URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when comfortable with that disclosure, and keep the API key in the environment.

Risk: Public web scraping can inspect URLs beyond SEC filings.

Mitigation: Use scraping only to inspect relevant filing documents; avoid unrelated sites.

Risk: Incomplete or lagged filing data may be mistaken for current financial evidence or investment advice.

Mitigation: Cite source filings and reporting periods, disclose gaps, and treat results as research rather than buy/sell advice.

## Reference(s):

- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Skill endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/sec-filings-research)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Sourced filing briefs or comparisons identifying the entity, reporting period, filing, cited facts, retrieval time, and data gaps.]

## Skill Version(s):

1.0.10 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
