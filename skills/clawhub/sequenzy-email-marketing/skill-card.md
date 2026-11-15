## Description:

Guides agents through Sequenzy email marketing and related subscriber, campaign, sequence, inbox, and delivery workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sequenzy email marketing and related customer messaging through the CLI or MCP, including subscriber, campaign, sequence, inbox, and delivery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented workflows extend beyond email marketing into broader account and messaging operations, and the security inspection was incomplete.

Mitigation: Review the requested workflow and its targets before execution, and check the relevant CLI help or MCP tool list to confirm support and intended scope.

## Reference(s):

- [Command reference](references/command-reference.md)
- [Use cases](references/use-cases.md)
- [Sequenzy API reference](https://docs.sequenzy.com/api-reference)
- [Sequenzy MCP events](https://docs.sequenzy.com/concepts/mcp-events)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Text]

**Output Format:** [Markdown guidance with CLI commands and structured JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow-dependent; generated email content is draft content and should be reviewed before sending.]

## Skill Version(s):

1.6.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
