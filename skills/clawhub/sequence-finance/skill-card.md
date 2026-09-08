## Description:

Read Sequence business bank accounts, cash balances, transfers, and cards; create and run money-moving automations with human approval before funds move.

This skill is ready for commercial/non-commercial use.

## Publisher:

[getsequence](https://clawhub.ai/user/getsequence)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and business operators use this skill to connect an agent to Sequence for business cash visibility, transfers, cards, pods, and money-moving automation workflows. It is not intended for personal-finance advice, tax filing, bookkeeping, or unapproved movement of funds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting the skill gives an agent access to Sequence business banking information and available role-scoped tools.

Mitigation: Confirm trust in Sequence before installation, review enabled capabilities, and prefer read-only tools for balance and reporting workflows.

Risk: Transfer or automation requests can affect real business funds if approved without review.

Mitigation: Treat money movement as a proposal, verify amount, source, and destination, and approve transfers or automation runs only in the Sequence app.

Risk: Using unattended capability acceptance can broaden access without an interactive review.

Mitigation: Use unattended capability acceptance only for CI or scripts, and rely on normal human capability review for ordinary installs.

## Reference(s):

- [Sequence ClawHub skill page](https://clawhub.ai/getsequence/skills/sequence-finance)
- [Sequence publisher profile](https://clawhub.ai/user/getsequence)
- [Sequence website](https://getsequence.io)
- [Sequence agent setup](https://app.getsequence.io/agents)
- [Sequence agent signup](https://app.getsequence.io/agentic/signup)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and connection guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Sequence account and an OAuth-connected Sequence MCP server; money movement remains pending until approved by a human in Sequence.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
