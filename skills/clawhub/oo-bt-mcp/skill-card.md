## Description:

BT Panel MCP helps agents inspect and operate BT Panel server-management tools through OOMOL's bt_mcp connector and oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to list current BT Panel MCP tools, inspect live schemas, and call BT Panel actions through OOMOL-connected accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes an unsafe remote installer pattern for the oo CLI.

Mitigation: Review the oo CLI installation method before installing and prefer a verified or package-manager install path.

Risk: BT Panel MCP actions can include broad server-management capabilities such as command execution, firewall changes, file writes, or data deletion.

Mitigation: Check the exact target, payload, and expected effect before tool calls, and require explicit confirmation for write or destructive actions.

## Reference(s):

- [BT Panel MCP homepage](https://www.bt.cn/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bt-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live schema inspection before action calls.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
