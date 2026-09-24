## Description:

Search and analyse Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address resolution, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer Swedish property questions with Hemnet listing, sold-price, market-statistics, address lookup, photo, and mortgage-calculation information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hemnet results, sold-price comparisons, and mortgage calculations can affect financial or purchasing decisions.

Mitigation: Review listing status, sample size, calculation assumptions, and current market context before relying on results for a purchase or loan decision.

Risk: Address lookup may scan a limited set of listings, so a miss can be inconclusive when results are truncated.

Mitigation: Treat truncated misses as non-definitive and retry with narrower location or price filters.

Risk: The skill may activate for broad Swedish housing questions and retrieve Hemnet-related property information.

Mitigation: Confirm that Hemnet-based Swedish property information is appropriate for the user request and review results before presenting them as authoritative.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or structured text summarizing Hemnet listing data, sold-price comparisons, market statistics, address matches, photo URLs, health checks, and mortgage calculations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include SEK-denominated prices, square-meter areas, room counts, listing identifiers, coordinates, broker details, and truncation or sample-size indicators when relevant.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
