## Description:

Slack (slack.com). Use this skill for ANY Slack request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read Slack workspace context and perform common Slack actions through an OOMOL-connected account. It supports schema-driven Slack connector calls for messages, conversations, users, files, reactions, search, and thread workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include internet installer commands executed directly in a shell.

Mitigation: Use a verified or pinned installer source, or inspect and validate the downloaded installer before execution.

Risk: Slack write and destructive actions can change, remove, or overwrite workspace content.

Mitigation: Confirm the exact Slack target, payload, and expected effect before approving write or destructive actions.

Risk: The connector relies on OOMOL-managed Slack access for the connected account.

Mitigation: Install and use the skill only where OOMOL handling connector access is acceptable for the workspace and account.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-slack)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Slack homepage](https://slack.com)
- [Slack icon](https://static.oomol.com/logo/third-party/Slack.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Slack connector calls that return JSON data and execution metadata.]

## Skill Version(s):

1.0.7 (source: server evidence release.version and skill frontmatter metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
