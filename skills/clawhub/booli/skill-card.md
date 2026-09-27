## Description:

Search and analyse Swedish real estate on booli.se — active for-sale listings, sold prices (slutpriser), area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer Swedish real estate questions by searching Booli listings, sold prices, area IDs, and market statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Searches may run through the user's local Booli browser tab via the Transporter bridge.

Mitigation: Keep use limited to Booli/property queries and approve the pairing prompt only when intentionally using the skill.

Risk: Market statistics can be misleading when based on a thin sample.

Mitigation: Check sample_size before relying on medians, averages, or over/under-asking percentages.

## Reference(s):

- [Booli](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or structured text summaries with property data and tool-use guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Booli property queries; monetary values are in SEK, areas are in m², and sold-search dates use YYYYMMDD.]

## Skill Version(s):

2.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
