## Description:

WPS MCP (wps.cn). Use this skill for ANY WPS MCP request: reading, creating, updating, and deleting data through the OOMOL-connected WPS MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live WPS MCP action schemas and run WPS cloud document operations through the oo CLI. It supports reading, listing, searching, inspecting, creating, and folder-management workflows for connected WPS accounts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that may be unsafe if the installer source is not verified.

Mitigation: Review the oo CLI installer source or use an official, verifiable installation method before running setup commands.

Risk: Connected WPS accounts may expose documents to read, write, or destructive connector actions.

Mitigation: Connect only appropriate WPS accounts and require explicit user confirmation for every write or destructive action, including target and expected effect.

## Reference(s):

- [WPS MCP ClawHub release](https://clawhub.ai/oomol/skills/oo-wps-mcp)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [WPS homepage](https://www.wps.cn)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs agents to fetch live connector schemas before sending JSON payloads and to require confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
