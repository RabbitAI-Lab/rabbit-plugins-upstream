## Description:

Estimates travel budgets for supported destinations using local static data, with breakdowns by travel style, trip length, traveler count, flights, visas, insurance, and daily spending categories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[travel-skills](https://clawhub.ai/user/travel-skills)

### License/Terms of Use:

MIT-0

## Use Case:

External users and travel planners use this skill to get rough trip-budget estimates and compare supported destinations before booking. It is best suited for early planning, not real-time pricing or final purchasing decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Budget results can be inaccurate because the skill uses static reference prices and does not check live airfare, exchange rates, hotels, visas, or insurance.

Mitigation: Treat outputs as rough planning estimates and verify final costs with current booking, visa, insurance, and exchange-rate sources before purchasing.

Risk: Destination coverage and price assumptions may not match every itinerary, season, or traveler preference.

Mitigation: Use the skill for supported-destination comparisons and adjust estimates manually for seasonality, route choices, and personal spending patterns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/travel-budget-planner)
- [Publisher profile](https://clawhub.ai/user/travel-skills)
- [Skill README](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [markdown, text, guidance]

**Output Format:** [Markdown tables and bullet lists, with JSON error messages for unsupported requests.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local static estimates and does not perform live airfare, exchange-rate, hotel, visa, or insurance lookups.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
