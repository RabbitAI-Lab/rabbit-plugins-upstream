## Description:

Mattermost enables agents to read Mattermost users, teams, channels, and posts, and to create channel posts through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate Mattermost through an OOMOL-connected account, including retrieving user, team, channel, and post data and creating channel posts after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use a verified installation path, inspect the installer before execution, and do not allow an agent to run the installer automatically.

Risk: Mattermost write actions can create posts in channels through the connected account.

Mitigation: Confirm the exact channel, payload, and expected effect with the user before running any action tagged as write.

Risk: Actions are brokered through OOMOL and depend on the oo CLI and an OOMOL-connected Mattermost account.

Mitigation: Install only when that trust model and prerequisite are acceptable for the deployment environment.

## Reference(s):

- [ClawHub Mattermost skill page](https://clawhub.ai/oomol/skills/oo-mattermost)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Mattermost connection page](https://console.oomol.com/app-connections?provider=mattermost)
- [Mattermost homepage](https://mattermost.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mattermost write actions require explicit payload confirmation; oo CLI command responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
