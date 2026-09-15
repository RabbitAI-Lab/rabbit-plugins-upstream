## Description:

Researches public equities, crypto, SEC filings, congressional trading disclosures, and private-market teaser profiles through the Crawlora API and returns normalized JSON-backed research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent builders use this skill to query finance and market data sources through Crawlora for ticker research, SEC filing review, congressional trade checks, crypto market scans, and private-market profile lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora is a third-party data provider and receives API request parameters.

Mitigation: Do not send confidential watchlists, private deal targets, personal financial details, or proprietary research terms unless sharing them with Crawlora is acceptable.

Risk: Financial and market data may be incomplete, delayed, or unsuitable as investment advice.

Mitigation: Use the returned data as research support and verify material decisions against authoritative sources.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY, avoid putting it in query parameters or committed files, and rotate it if exposure is suspected.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to Crawlora's documented finance, SEC, congress, crypto, and PitchBook routes.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
