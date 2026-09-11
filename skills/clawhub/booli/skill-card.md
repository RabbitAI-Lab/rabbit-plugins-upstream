## Description:

Search and analyze Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Booli real-estate data for Swedish property searches, sold-price comparables, area lookup, and market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may use the user's local browser context through the Transporter browser bridge.

Mitigation: Use the skill only with an intentional open www.booli.se tab, approve pairing prompts deliberately, and run booli_healthcheck before relying on results.

Risk: Market statistics can be misleading when based on a small sample.

Mitigation: Check sample_size before trusting medians, averages, or over-under asking statistics.

## Reference(s):

- [Booli Skill Page](https://clawhub.ai/chrischall/skills/booli)
- [Booli](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text summarizing Booli query results and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only outputs; prices are in SEK, areas are in square meters, and sold-date filters use YYYYMMDD.]

## Skill Version(s):

1.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
