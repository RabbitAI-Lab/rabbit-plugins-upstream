## Description:

Sunsama MCP helps an agent read, create, update, and delete Sunsama planning data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to operate Sunsama MCP from an OOMOL-connected account, including task, calendar, channel, objective, help-center, tool-discovery, and resource workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include remote installer commands that execute downloaded scripts without verification.

Mitigation: Use a signed package, pinned release, or installer with a published checksum or signature before installing the oo CLI.

Risk: Write and destructive actions can change or delete Sunsama tasks, calendar events, channels, and related planning data.

Mitigation: Confirm the exact target, payload, and effect with the user before running any write or destructive action.

## Reference(s):

- [Sunsama MCP homepage](https://help.sunsama.com/docs/integrations/mcp/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sunsama-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include JSON data and execution metadata from the oo CLI.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
