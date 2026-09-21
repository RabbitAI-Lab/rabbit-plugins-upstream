## Description:

Discord Bot helps agents read, create, update, and delete Discord resources through OOMOL's `oo` CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, employees, and external agents use this skill to operate Discord bot workflows through OOMOL-connected credentials, including reading guild data, managing channels and messages, and performing moderated write or cleanup actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connected Discord bot permissions can allow posting, moderation, deletion, bans, and guild setting changes.

Mitigation: Install only when the user trusts OOMOL and the connected Discord bot permissions; confirm the exact action, payload, target, and expected effect before any write or destructive action.

Risk: The first-time setup path includes a pipe-to-shell installer for the oo CLI.

Mitigation: Review the OOMOL CLI installer before running it and use the documented platform-specific install path when setup is required.

## Reference(s):

- [ClawHub Discord Bot skill page](https://clawhub.ai/oomol/skills/oo-discordbot)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Discord Developer Applications](https://discord.com/developers/applications)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include `oo connector schema` and `oo connector run` commands plus action-specific JSON payload guidance.]

## Skill Version(s):

1.0.5 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
