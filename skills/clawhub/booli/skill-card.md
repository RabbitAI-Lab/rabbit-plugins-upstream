## Description:

Search and analyze Swedish real estate on booli.se, including active listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to look up Swedish property listings, sold-price comparables, area identifiers, and market statistics from Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Booli searches may be routed through a local browser bridge connected to an open Booli tab.

Mitigation: Approve the Transporter browser bridge only for the intended read-only Booli use and keep the Booli tab under user control.

Risk: Market statistics can be misleading when based on a small sample.

Mitigation: Check the reported sample size before relying on medians, averages, or over-under asking percentages.

## Reference(s):

- [Booli skill page](https://clawhub.ai/chrischall/skills/booli)
- [Publisher profile](https://clawhub.ai/user/chrischall)
- [Booli](https://www.booli.se)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries of property search results, listing details, sold-price comparables, diagnostics, and market statistics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup output; monetary values are in SEK, areas are in square meters, and market statistics should be interpreted with attention to sample size.]

## Skill Version(s):

1.3.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
