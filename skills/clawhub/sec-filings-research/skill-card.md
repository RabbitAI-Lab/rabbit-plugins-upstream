## Description:

Helps agents research SEC EDGAR filings and financial disclosures through Crawlora to produce sourced, period-aware briefs and comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to locate SEC filings, inspect disclosures and financial data, and prepare cited company briefs or period-aware comparisons.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Filing-related queries, URLs, and request bodies are sent to Crawlora using an API key.

Mitigation: Use an authorized key and public filing sources; exclude confidential or personal data from queries and scrape bodies.

Risk: Truncated filing text or delayed datasets may support incomplete or misleading comparisons.

Mitigation: Confirm claims against identified filings, report coverage gaps and data-as-of dates, and verify comparable periods before drawing conclusions.

## Reference(s):

- [SEC Filings Research on ClawHub](https://clawhub.ai/crawlora-org/skills/sec-filings-research)
- [Crawlora](https://crawlora.net)
- [SEC EDGAR API documentation](https://www.sec.gov/search-filings/edgar-application-programming-interfaces)
- [Supported endpoints](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown brief or comparison]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies filings, reporting periods, source links, retrieval time, and evidence gaps.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
