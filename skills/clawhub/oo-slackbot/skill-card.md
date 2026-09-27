## Description:

Slack Bot (slack.com) helps agents read, create, update, and delete Slack Bot data through OOMOL-connected Slack credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Slack workspaces from an agent, including listing Slack data, posting messages, managing threads and reactions, and handling Slack-hosted files through an OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include web-fetched installer scripts for the oo CLI.

Mitigation: Review the installer path before installing and prefer a verified package-manager or signed installer when available.

Risk: Slack write actions can post, update, schedule, upload, or otherwise change workspace content.

Mitigation: Confirm the exact Slack action payload and expected effect with the user before running write actions.

Risk: Destructive Slack actions can delete messages, files, or reactions.

Mitigation: Require explicit user approval for the target resource before running destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-slackbot)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Slack](https://slack.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or run oo CLI connector commands that return JSON responses from Slack Bot actions.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
