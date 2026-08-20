## Description:

How the Risk Manager writes the desk's risk limits with the user, sizes every proposed trade from live account state and Hyperliquid's real constraints, checks the book, and issues a PASS or REJECT with exact ticket fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and trading-desk operators use this skill to define risk limits, size proposed Hyperliquid trades from live account state, and produce PASS or REJECT risk decisions with exact ticket fields. It also supports written book checks that summarize positions, margin, protection, open risk, and daily loss status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses live Hyperliquid account data and can create persistent desk records containing sensitive account, position, and operational details.

Mitigation: Install only when this access is intended, and review generated risk-limit files, saved book checks, and proposal records before sharing or retaining them outside the approved workspace.

Risk: Missing or stale account, market, or stop inputs can lead to an incorrect sizing decision.

Mitigation: Require the agent to reject missing or stale inputs and verify the displayed sizing arithmetic, leverage tier, margin, open-risk, and protection checks before trade execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/galleonlabs/skills/hypergrok-desk-risk-limits)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown risk-limit files, PASS or REJECT risk blocks, and book-check briefs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use live Hyperliquid account data and persist trading-desk records when the agent follows the workflow.]

## Skill Version(s):

1.0.0 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
