## Description:

Track product prices across time and stores, alert on price drops, and predict the best time to buy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to maintain a local product price history, review price trends, receive threshold-based drop alerts, and get category-aware buying timing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tracked products, prices, timestamps, sources, and optional product URLs are retained in a local JSON database.

Mitigation: Use --db to select a separate database for sensitive shopping lists or shared systems, and delete or edit the JSON file when the history is no longer needed.

Risk: Seasonal buying guidance and depreciation estimates may not reflect current retail conditions for a specific product.

Mitigation: Treat recommendations as decision support and verify current prices, product model numbers, and seller terms before purchasing.

## Reference(s):

- [Price Tracking Strategies](references/price-tracking-strategies.md)
- [Seasonal Buying Calendar](references/seasonal-buying-calendar.md)
- [GitHub Source Repository](https://github.com/voronindenis5/price-predator)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/price-predator)
- [ClawHub Publisher Profile](https://clawhub.ai/user/voronindenis5)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Terminal text with command-line examples and report-style summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a local JSON database; the default path is ~/.price_predator_db.json unless --db is provided.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
