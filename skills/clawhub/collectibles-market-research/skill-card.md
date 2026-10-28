## Description:

Researches public trading card and sports collectible markets using Crawlora, PSA reference data, marketplace listings, auctions, sales, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Collectors and buyers use it to build sourced briefs about card identity, PSA data, live listings, completed sales, auctions, and trends. It keeps asking prices, realized prices, and reference values distinct.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search parameters and the Crawlora API key are sent to Crawlora, and requests may consume API credits.

Mitigation: Avoid including private information in searches and account for API credit use.

Risk: Market and PSA reference results can be mistaken for guaranteed valuations or authentication.

Mitigation: Present results as research evidence, distinguish source and sale status, and avoid treating them as guaranteed value or proof of authenticity.

## Reference(s):

- [Crawlora API endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/collectibles-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown research brief with source URLs, prices, grades, and listing or sale status.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates guide values, asking prices, bids, and sold prices; reports bounded source evidence without guaranteeing value or authenticity.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
