## Description:

BT Panel MCP helps agents operate BT Panel MCP through an OOMOL-connected account for searching, reading data, and invoking current server-management tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover BT Panel MCP tools, inspect live action schemas, and run connector actions through the oo CLI. It is suited to BT Panel MCP workflows that need structured results and explicit confirmation before state-changing or destructive server-management operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A BT Panel connection with production or administrative privileges may expose broad server-management tools with high-impact effects.

Mitigation: Review the skill before installing, prefer least-privilege or read-only connections for discovery tasks, and use this skill only when explicit confirmation for state-changing or destructive actions is acceptable.

Risk: The call_tool action may expose command execution, firewall changes, file writes, or irreversible deletion operations depending on the current BT Panel MCP server tools.

Mitigation: Run list_tools and fetch the live action schema before constructing a payload, then confirm the exact target, payload, and effect with the user before any write or destructive operation.

## Reference(s):

- [BT Panel MCP ClawHub release](https://clawhub.ai/oomol/skills/oo-bt-mcp)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [BT Panel MCP homepage](https://www.bt.cn/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute oo connector commands that return structured JSON with data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
