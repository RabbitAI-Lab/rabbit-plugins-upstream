## Description:

Guides an agent through supported Sequenzy email-marketing workflows, including subscriber management, campaign and sequence operations, inbox handling, transactional email, and delivery reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[polnikale](https://clawhub.ai/user/polnikale)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Sequenzy email-marketing workflows through the CLI or MCP, including subscriber, campaign, sequence, inbox, and delivery tasks. It guides agents to check current support and inspect targets before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates this release suspicious with medium confidence, citing broad platform functionality beyond its stated email-marketing purpose; analysis coverage is partial.

Mitigation: Review the instructions for the requested workflow, check current CLI or MCP support, and inspect the target before making changes.

Risk: Campaign cancellation can immediately stop a scheduled or active send and does not prompt for confirmation.

Mitigation: Verify the campaign and its status, and require clear user direction before canceling it.

## Reference(s):

- [Use cases and MCP effect disclosures](references/use-cases.md)
- [Command reference](references/command-reference.md)
- [Sequenzy API reference](https://docs.sequenzy.com/api-reference)
- [Sequenzy MCP events documentation](https://docs.sequenzy.com/concepts/mcp-events)
- [ClawHub release page](https://clawhub.ai/polnikale/skills/sequenzy-email-marketing)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Markdown]

**Output Format:** [Markdown guidance with CLI commands and MCP/API workflow details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Workflow-dependent; no fixed output schema.]

## Skill Version(s):

1.6.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
