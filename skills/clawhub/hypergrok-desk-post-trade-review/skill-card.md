## Description:

Guides trading-desk agents through exchange-record-based journaling, post-trade and incident reviews, and weekly desk summaries while grading process separately from results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Trading-desk agents and their users document trades, reconcile outcomes against exchange records, assess execution costs and controls, and prepare incident and weekly desk reviews.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A review may access sensitive trade records outside the intended trade or time window.

Mitigation: Use only in the intended trading-desk workspace; confirm the trade or time window and limit record access to that scope.

Risk: Trade reviews may be sent to unauthorized recipients.

Mitigation: Verify that the Desk Lead and user DM recipients are authorized before sending the review.

## Reference(s):

- [HyperGrok Desk Post Trade Review on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-post-trade-review)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown journal entries, trade and incident reviews, weekly summaries, and direct messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timestamped exchange-record evidence, execution costs, separate process and outcome grades, and one repeatable finding per review.]

## Skill Version(s):

1.5.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
