## Description:

Researches public trading-card and sports-collectible markets through the Crawlora API: card identity, PSA certification and price-guide evidence, live listings, auctions, sold items, and market trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Collectors, marketplace researchers, and agents use this skill to build sourced briefs for trading-card and sports-collectible questions. It helps compare PSA reference data, live listings, auction lots, sold items, and market trends without performing purchases, bids, appraisals, authentication, or grading actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, card identifiers, PSA certification numbers, and the Crawlora API key may be sent to Crawlora's API.

Mitigation: Use a dedicated Crawlora API key and avoid entering unrelated private data into collectible searches.

Risk: Returned market data may be mistaken for authentication, appraisal, investment, bid, purchase, or grading advice.

Mitigation: Treat prices and platform records as research evidence; preserve source, status, grade or condition, time window, and sample size, and avoid claims of guaranteed value, authenticity, rarity, or investment return.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/collectibles-market-research)

## Skill Output:

**Output Type(s):** [guidance, shell commands, text, markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The helper emits raw JSON from Crawlora API endpoints; agents are expected to summarize evidence with source URLs, price status, grade or condition, and platform context.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
