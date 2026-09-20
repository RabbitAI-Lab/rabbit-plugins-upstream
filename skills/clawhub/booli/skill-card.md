## Description:

Search and analyse Swedish real estate on booli.se - active for-sale listings, sold prices (slutpriser), area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare Swedish real estate listings, sold prices, area identifiers, and market statistics from Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may route queries through a local Booli browser tab using the Transporter bridge when direct requests are blocked.

Mitigation: Keep the bridge limited to a trusted browser tab and extension, run booli_healthcheck before use, or set direct mode when avoiding the bridge is preferred.

Risk: Market statistics can be misleading when based on a thin sample.

Mitigation: Check the reported sample_size before relying on medians, averages, or over-under asking percentages.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text responses with property summaries, sold-price comparables, market statistics, and diagnostic guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; monetary values are in SEK, areas are in square meters, and sold-date filters use YYYYMMDD.]

## Skill Version(s):

2.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
