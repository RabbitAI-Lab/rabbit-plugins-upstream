## Description:

Search and analyse Swedish real estate on hemnet.se, including active for-sale listings, sold prices, listing details, photos, market statistics, address resolution, and a Swedish mortgage calculator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and real-estate analysts use this skill to search and compare Swedish property listings, inspect sold-price comparables, calculate mortgage costs, and summarize local market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches and address lookups may send user-provided Swedish address or location terms to Hemnet's public service.

Mitigation: Avoid submitting sensitive personal data and use the skill within Hemnet's terms of service.

Risk: Market medians and price-per-square-meter summaries can be unreliable when based on a small sample size.

Mitigation: Check sample_size before relying on market statistics and present thin-sample results as directional rather than definitive.

## Reference(s):

- [Hemnet website](https://www.hemnet.se)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown summaries with structured property details, market analysis, links, and calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing identifiers, prices in SEK, areas in m2, rooms, coordinates, broker details, photo URLs, sold-price comparisons, and mortgage-cost estimates.]

## Skill Version(s):

0.4.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
