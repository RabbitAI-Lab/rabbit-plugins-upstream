## Description:

Yingmi MCP helps agents discover Yingmi financial data, research, and advisory tools and call them through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect Yingmi MCP tool schemas, discover available financial data, research, and advisory tools, and run read-oriented Yingmi MCP actions through an authenticated OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote CLI installer commands that can execute downloaded scripts.

Mitigation: Prefer a signed or package-manager install path, verify the oo CLI source, and avoid running remote installer commands blindly.

Risk: The generic call_tool action may invoke downstream Yingmi MCP tools whose behavior is only known after schema and annotation checks.

Mitigation: Fetch the live schema before building a payload and require explicit user confirmation unless the downstream tool is clearly read-only.

Risk: The connector depends on OOMOL and Yingmi account state, credentials, connection scopes, and billing status.

Mitigation: Run setup or reconnection steps only after matching authentication, connection, scope, or billing errors occur.

## Reference(s):

- [Yingmi MCP homepage](https://qieman.com/mcp/mcp-market)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-yingmi-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include live Yingmi MCP schemas, command outputs, setup guidance, and user-confirmation prompts for actions with write or destructive behavior.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
