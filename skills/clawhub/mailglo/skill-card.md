## Description:

Inspect and manage a workspace's email authentication (DMARC, SPF, DKIM, MTA-STS) in MailGlo through the mailglo command-line tool or MailGlo's MCP server, within the permissions a person gave you.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mailglo](https://clawhub.ai/user/mailglo)

### License/Terms of Use:

MIT-0

## Use Case:

External MailGlo workspace users can use this agent to inspect email authentication checks, understand recommended fixes, and prepare changes through the CLI or MCP within their granted permissions. A person reviews and approves changes in MailGlo.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MCP sign-in is shared across an OpenClaw Gateway, allowing agents on it and people who can message them to access the signed-in person's workspace.

Mitigation: Use a Gateway dedicated to one person and limit who can message its agents, as the skill recommends.

Risk: A proposed email-authentication change could be incorrect or have unwanted effects.

Mitigation: Prepare changes only when asked, review every plan check and reason, and have a person approve and apply the plan in MailGlo.

Risk: Some referenced material was unavailable during the security review, leaving related behavior unreviewed.

Mitigation: Review the change-plan and approval steps and consult the linked MailGlo guides before installing.

## Reference(s):

- [MailGlo agent documentation](https://mailglo.com/docs/agents/)
- [MailGlo CLI guide](https://mailglo.com/docs/cli/)
- [MailGlo MCP guide](https://mailglo.com/docs/mcp/)
- [OpenClaw MCP transport documentation](https://docs.openclaw.ai/cli/mcp/transports)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
