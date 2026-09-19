## Description:

Researches stocks, crypto, SEC filings, congressional trading disclosures, and private-market profiles through the Crawlora API, returning normalized JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and finance-focused agents use this skill to retrieve public market, crypto, SEC, congressional trading, and private-market profile data from Crawlora for research workflows. It should be treated as data retrieval support, not investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Finance research queries and supplied identifiers are sent to Crawlora under the user's Crawlora account.

Mitigation: Avoid sending confidential watchlists, deal targets, or proprietary due-diligence prompts unless Crawlora's data handling terms are acceptable.

Risk: Public market data, SEC data, congressional disclosures, crypto data, and private-market teaser profiles can be incomplete, delayed, or unsuitable as standalone investment advice.

Mitigation: Use the results as research inputs, cross-check important conclusions against authoritative sources, and avoid presenting outputs as investment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/finance-markets-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends supported finance research requests to the Crawlora API.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
