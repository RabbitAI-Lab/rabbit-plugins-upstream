## Description:

Discord Bot lets an agent operate Discord through the OOMOL-connected oo CLI for reading, creating, updating, and deleting Discord resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage Discord bot resources such as guilds, channels, messages, members, roles, events, moderation settings, and commands through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unsafe setup guidance around a remote installer.

Mitigation: Review installation steps before use and avoid running remote installer commands blindly.

Risk: The security scan reports that some Discord-changing actions are mislabeled as safe reads.

Mitigation: Require explicit confirmation for any action that changes content, pins, bans, guild membership, roles, channels, or server settings, even when the skill does not tag the action as write or destructive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-discordbot)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Discord Developer Applications](https://discord.com/developers/applications)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; results are returned as JSON from the oo CLI.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
