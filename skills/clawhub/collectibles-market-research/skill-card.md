## Description:

Researches public trading-card and sports-collectible markets through the Crawlora API — card identity, PSA certification and price-guide evidence, live listings, auctions, sold items, and market trends. Use when the user wants a sourced collector or buying brief, not authentication, appraisal guarantees, or a purchase action.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Collectors and buyers can use this skill to research card identity, PSA reference data, listings, auctions, completed sales, and market trends, then assemble a brief with source URLs and clearly separated price evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and certification numbers are sent to Crawlora using the configured API key; live service behavior and data retention were not verified.

Mitigation: Send only information needed for the research query and use the skill only if comfortable sending it to Crawlora.

Risk: API requests consume service credits, and broad searches can use credits without producing a focused comparison.

Mitigation: Keep searches bounded and start with the narrowest useful terms.

Risk: Research results do not guarantee a collectible's value or authenticity.

Mitigation: Show source URLs and treat PSA guide values, active listings, bids, and completed sales as distinct evidence rather than guarantees.

## Reference(s):

- [Crawlora service](https://crawlora.net/)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Collectibles Market Research release](https://clawhub.ai/crawlora-org/skills/collectibles-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research brief with source URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates identity, condition, grade, listing and sale status, and distinguishes guide values, asking prices, bids, and realized prices.]

## Skill Version(s):

1.0.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
