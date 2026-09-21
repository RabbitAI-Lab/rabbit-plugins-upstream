## Description:

Enables agents to operate Sunsama through the OOMOL oo CLI and sunsama_mcp connector for reading, creating, updating, scheduling, and deleting Sunsama tasks, calendar events, channels, objectives, and related resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage Sunsama planning workflows through the OOMOL-connected Sunsama MCP connector, including task, calendar, channel, objective, help-center, and resource-discovery operations. It is appropriate when users want an agent to read or modify Sunsama data with explicit confirmation for write and destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include running remote oo CLI installer scripts directly in a shell.

Mitigation: Prefer a verified package or download and inspect the installer before execution.

Risk: The skill operates Sunsama through OOMOL with server-side credential handling.

Mitigation: Install only when the user is comfortable trusting OOMOL with Sunsama access.

Risk: Write and destructive actions can alter or remove Sunsama tasks, calendar events, channels, objectives, and related data.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sunsama-mcp)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Sunsama MCP documentation](https://help.sunsama.com/docs/integrations/mcp/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
