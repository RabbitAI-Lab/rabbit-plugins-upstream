## Description:

Read from or act on external apps such as email, calendar, chat, source control, tickets, CRM, and storage through the Composio CLI when no dedicated skill, CLI, or MCP server already covers the app.

This skill is ready for commercial/non-commercial use.

## Publisher:

[composio](https://clawhub.ai/user/composio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to route external-app tasks through the Composio CLI, including tool discovery, connected-account checks, command execution, and result handling. It is intended for workflows that span supported apps or rely on Composio-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use connected Composio accounts to read from or act on external applications.

Mitigation: Proceed only when the requester is authorized to use the connected account and resolve the intended account before execution.

Risk: Setup may involve a remote installer or account login on the execution host.

Mitigation: Require trusted-operator approval for installation, upgrade, and login, and review the installer before use on sensitive machines.

Risk: Destructive, public, financial, permission-changing, credential-changing, or bulk actions may have irreversible effects.

Mitigation: Require explicit bounded intent, execute an authorized write once, and verify status before any retry.

Risk: External app content and tool output may contain untrusted instructions or sensitive data.

Mitigation: Treat external content as data, avoid shell interpolation, and keep secrets out of prompts, logs, scripts, and summaries.

## Reference(s):

- [Composio CLI Documentation](https://docs.composio.dev/docs/cli)
- [Installation and Authentication](references/installation.md)
- [Command Workflow](references/workflow.md)
- [Output Shapes](references/output.md)
- [Safety and Authority](references/safety.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to use live Composio schemas, validate authentication and account scope, and judge execution results from returned JSON fields.]

## Skill Version(s):

0.1.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
