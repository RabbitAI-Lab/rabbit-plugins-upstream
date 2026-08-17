## Description:

Track product prices across time and stores, alert on price drops, and predict the best time to buy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to track manually entered product prices, review terminal price-history reports, receive price-drop alerts, and get category-based buying timing guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product names, URLs, sources, and price history are stored locally in a JSON file.

Mitigation: Use --db to place the database in an intended location and avoid recording sensitive product or source details when they are not needed.

Risk: Price timing and depreciation predictions are category-based guidance and may not match actual retailer behavior.

Mitigation: Confirm recommendations against current store prices and product availability before making purchase decisions.

## Reference(s):

- [Price Tracking Strategies](references/price-tracking-strategies.md)
- [Seasonal Buying Calendar](references/seasonal-buying-calendar.md)
- [Server-Resolved GitHub Repository](https://github.com/voronindenis5/price-predator)
- [ClawHub Skill Page](https://clawhub.ai/voronindenis5/skills/price-predator)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Terminal text with command examples and local JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Stores user-entered product names, URLs, sources, prices, and price history in a local JSON file; the database path can be set with --db.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
