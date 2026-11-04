## Description:

Analyzes a stock's overhead resistance using trapped-share distribution, moving-average confluence, and estimated rebound volume, producing a reviewable pressure-line report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[panting09266-ai](https://clawhub.ai/user/panting09266-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individual investors use this skill to review likely resistance levels for a single stock they hold, understand how trapped-share concentrations and moving averages may affect a rebound, and examine estimated volume needs. It provides analysis for consideration rather than a guaranteed recovery date or a buy/sell instruction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to share a Cue API key in chat.

Mitigation: Configure the key outside chat, restrict access to its credential file, and rotate any key already shared in conversation.

Risk: The external runner can update without review, and its behavior was not available in this artifact.

Mitigation: Review and pin the runner before executing it.

Risk: Stock queries and optional cost-basis details are sent to Cue; recurring runs consume credits.

Mitigation: Share only the details needed, and check recurring-run costs and removal instructions before enabling them.

## Reference(s):

- [Cue platform](https://cuecue.cn)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Structured Markdown report with trend context, resistance levels, rebound scenarios, risk notes, and source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-stock analysis; results depend on Cue and its external data sources.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
