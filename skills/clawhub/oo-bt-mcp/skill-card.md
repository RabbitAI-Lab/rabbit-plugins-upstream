## Description:

BT Panel MCP (bt.cn) helps an agent inspect and run BT Panel MCP actions through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover BT Panel MCP tools, inspect live action schemas, and run server-management actions through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Do not allow an agent to run curl-to-bash or irm-to-iex installers blindly; prefer an official versioned installer or inspect and verify the downloaded script first.

Risk: The connected BT Panel MCP server may expose powerful administrative actions through call_tool, including command execution, firewall changes, file writes, or irreversible deletions.

Mitigation: Inspect the live schema before building requests and require explicit user confirmation for state-changing, destructive, or otherwise high-impact payloads.

## Reference(s):

- [BT Panel MCP ClawHub listing](https://clawhub.ai/oomol/skills/oo-bt-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [BT Panel homepage](https://www.bt.cn/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
