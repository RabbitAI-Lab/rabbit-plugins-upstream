## Description:

Enables agents to operate Discord Bot through the OOMOL oo CLI for reading, creating, updating, and deleting Discord data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Discord bot resources such as guilds, channels, messages, members, roles, events, moderation settings, and commands through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete Discord data, including messages, channels, roles, bans, invites, guild settings, and related resources.

Mitigation: Use a Discord bot account limited to the intended servers and permissions, fetch the live action schema before constructing payloads, and confirm every write or destructive action with the user.

Risk: Setup guidance includes remote installer snippets for the oo CLI.

Mitigation: Do not run installer snippets automatically; independently verify the oo CLI installer source and integrity before installation.

Risk: Some action labeling may not fully reflect the impact of a Discord operation.

Mitigation: Treat all mutating actions as requiring explicit confirmation, even when a specific action is not tagged as write or destructive.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-discordbot)
- [Publisher profile](https://clawhub.ai/user/oomol)
- [Discord Developer Applications](https://discord.com/developers/applications)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run Discord connector actions that return JSON data and execution metadata.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
