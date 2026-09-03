## Description:

Search and analyse Swedish real estate on hemnet.se, including active listings, sold prices, listing details, photos, market statistics, address resolution, and Swedish mortgage calculations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to research Swedish residential real estate, compare for-sale and sold listings, inspect property details, review local market statistics, and estimate Swedish monthly housing costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Property searches, address lookups, and location queries may send user-provided real-estate interests or addresses to Hemnet's public API.

Mitigation: Avoid entering private addresses or personal financial details unless the user is comfortable using them for Hemnet lookups.

Risk: Market statistics and sold-price medians can be misleading when based on thin samples.

Mitigation: Check sample_size before relying on medians or averages and present thin samples as directional rather than definitive.

Risk: Use of Hemnet data may be subject to hemnet.se's terms of service.

Mitigation: Use the skill within hemnet.se's terms of service.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/hemnet)
- [Hemnet](https://hemnet.se)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text property research summaries with structured real-estate values]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing URLs, photo URLs, prices, property attributes, market statistics, and mortgage calculations in SEK.]

## Skill Version(s):

0.5.0 (source: target metadata and server release metadata, released 2026-09-02)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
