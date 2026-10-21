## Description:

Research SEC EDGAR filings and financial disclosures through Crawlora to produce sourced, period-aware filing briefs and comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, researchers, and developers use this skill to retrieve and compare company filings, financials, insider disclosures, and institutional holdings with identifiable sources and reporting periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filing queries and requested URLs are sent to Crawlora using the user's API key.

Mitigation: Use only if comfortable sharing those inputs with Crawlora, and keep the API key in the environment.

Risk: The public URL scraping capability can retrieve pages beyond SEC filings.

Mitigation: Use scraping deliberately, preferably for relevant SEC filing source URLs or issuer materials.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/sec-filings-research)
- [Endpoint reference](reference/endpoints.md)
- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Sourced filing briefs or comparisons in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies the entity, filing and reporting periods, cited sources, retrieval time, and evidence gaps.]

## Skill Version(s):

1.0.12 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
