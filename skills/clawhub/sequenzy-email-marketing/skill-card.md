## Description:

Guides agents through Sequenzy email marketing workflows, including subscriber and campaign management, message creation, delivery reporting, and supported CLI or MCP operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Sequenzy subscriber data, create and operate email campaigns and sequences, handle inbox workflows, and review delivery performance through supported CLI or MCP paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags a mismatch between the broad documented capabilities and the email-marketing scope, as well as campaign lifecycle guidance that could prompt consequential actions; some referenced files received only partial analysis.

Mitigation: Review the skill's scope and campaign cancellation guidance before installation. Before acting, inspect the target and confirm the workflow against installed CLI help or the MCP tool schema.

## Reference(s):

- [Use cases](references/use-cases.md)
- [Command reference](references/command-reference.md)
- [Sequenzy API reference](https://docs.sequenzy.com/api-reference)
- [Sequenzy MCP Events](https://docs.sequenzy.com/concepts/mcp-events)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown guidance, shell commands, and structured API or MCP requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated email content and operational requests; resulting actions depend on the selected workflow and account permissions.]

## Skill Version(s):

1.6.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
