## Description:

Researches public trading-card and sports-collectible markets using PSA references, marketplace listings, sold items, auctions, and market trends through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Collectors, buyers, and researchers use this skill to prepare sourced briefs comparing card identity, PSA references, active listings, auction lots, and completed sales without treating asking prices as realized values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Collectible queries, item identifiers, product URLs, and PSA certification numbers are sent to Crawlora's API.

Mitigation: Share only data you are comfortable sending to Crawlora and keep the API key out of logs and prompts.

Risk: Incomplete or inconsistent marketplace and PSA data can be mistaken for authenticated items or guaranteed values.

Mitigation: Check source URLs and comparable item details, distinguish asks from sales, and do not use the results as guaranteed authentication or formal appraisals.

Risk: Research results could be mistaken for authority to buy or bid.

Mitigation: Limit use to read-only research; do not use it for purchases, bidding, or account actions.

## Reference(s):

- [Collectibles Market Research on ClawHub](https://clawhub.ai/crawlora-org/skills/collectibles-market-research)
- [Crawlora endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API key setup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown collector or buying brief with source URLs and observed price ranges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates asking prices, bids, completed sales, and PSA guide values; includes evidence counts and data limitations.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
