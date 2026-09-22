## Description:

Search and analyse Swedish real estate on booli.se — active for-sale listings, sold prices (slutpriser), area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and analyze Swedish real-estate listings, sold-price comparables, area identifiers, and market statistics from Booli. It is useful when answering questions about Swedish property, housing, listings, or slutpriser.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may route through the user's browser context when Booli blocks direct server-side requests.

Mitigation: Use the browser bridge only when intentionally querying Booli property data, approve the pairing prompt deliberately, and disable the bridge when it is not needed.

Risk: Market statistics and medians can be misleading when based on a thin sample.

Mitigation: Check the reported sample size before relying on market statistics for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown or plain text summaries with structured property data from read-only Booli queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Money values are in SEK, areas are in square meters, rooms are numeric, and sold-date filters use YYYYMMDD.]

## Skill Version(s):

2.1.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
