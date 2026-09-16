## Description:

Mattermost (mattermost.com). Use this skill for ANY Mattermost request: reading, creating, and updating data through the OOMOL-connected Mattermost account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Mattermost through OOMOL's connected account flow, including retrieving users, teams, channels, and posts, and creating channel posts after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup uses remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a verified oo CLI installation method and review the installer source before running it.

Risk: The create_post action can write new content to a Mattermost channel.

Mitigation: Confirm the exact target channel, payload, and expected effect with the user before executing write actions.

## Reference(s):

- [Mattermost homepage](https://mattermost.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mattermost)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and SKILL.md metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
