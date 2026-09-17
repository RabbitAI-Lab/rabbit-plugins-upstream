## Description:

Search and analyse Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address resolution, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Swedish property through Hemnet data, compare active and sold listings, resolve addresses and locations, review market statistics, and estimate Swedish mortgage costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may be invoked for broad Swedish property questions where the user expects non-Hemnet sources or general housing guidance.

Mitigation: Ask the user whether they want Hemnet-specific research before relying on this skill for broad Swedish real-estate requests.

Risk: Market statistics from small sample sizes can be misleading.

Mitigation: Check and disclose sample size before presenting medians or averages as meaningful market signals.

Risk: Public listing and sold-price data may change or become unavailable.

Mitigation: Treat returned property data as point-in-time research and include source URLs or retrieval context when possible.

## Reference(s):

- [Hemnet](https://www.hemnet.se)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet)

## Skill Output:

**Output Type(s):** [text, markdown, API Calls, guidance]

**Output Format:** [Markdown or structured text with listing data, market statistics, URLs, and calculation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prices in SEK, areas in square meters, listing photo URLs, coordinates, broker details, and mortgage cost estimates.]

## Skill Version(s):

0.6.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
