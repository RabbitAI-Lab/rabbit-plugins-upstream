## Description:

Sunsama MCP helps agents read, create, update, and delete Sunsama tasks, calendar events, channels, objectives, and help-center information through the OOMOL connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent manage Sunsama planning workflows, including task search, scheduling, backlog movement, priorities, notes, timers, meeting invites, channels, weekly objectives, and product help lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review the installer risk before installing; prefer an official, version-pinned, signed, or checksum-verified installation path, and do not let an agent run curl-to-bash or irm-to-iex commands automatically.

Risk: The skill can perform write and destructive Sunsama actions, including deleting tasks, calendar events, and channels.

Mitigation: Confirm write payloads and effects with the user, and require explicit approval before destructive actions.

## Reference(s):

- [Sunsama MCP integration documentation](https://help.sunsama.com/docs/integrations/mcp/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Sunsama MCP release page](https://clawhub.ai/oomol/skills/oo-sunsama-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Sunsama connector results as JSON when actions are executed with the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
