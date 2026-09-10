## Description:

Search and analyse Swedish real estate on booli.se, including active for-sale listings, sold prices, area resolution, and market statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and property researchers use this skill to look up Swedish real estate listings, sold-price comparables, area identifiers, and market statistics from Booli.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use depends on a browser extension and an open booli.se tab, which requires approving a browser bridge pairing.

Mitigation: Approve pairing only for a trusted browser bridge, keep the Booli tab under user control, and use the healthcheck before relying on lookup results.

Risk: Market statistics and medians can be misleading when based on a thin sample.

Mitigation: Check the reported sample size before relying on market statistics or comparable-sale summaries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/booli)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown or plain text summaries with property data and lookup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup results use SEK for money, square meters for area, numeric rooms, and Booli area or residence identifiers when available.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
