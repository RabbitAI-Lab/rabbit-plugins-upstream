## Description:

Slack Bot lets agents read, create, update, and delete Slack data through an OOMOL-connected Slack account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to let an agent inspect Slack conversations, users, files, threads, reactions, and permalinks, then perform confirmed Slack message, reaction, direct-message, scheduling, and file-upload workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Slack write and destructive actions can post, update, delete, schedule, react to, or upload content in the connected workspace.

Mitigation: Confirm the exact Slack target, action, and payload with the user before writes, and require explicit approval before destructive actions.

Risk: The connected Slack account may expose workspace channels, users, files, messages, threads, reactions, and permalinks within its granted OAuth scopes.

Mitigation: Review Slack OAuth scopes before installation and limit use to workspaces where the connected account is appropriate for agent access.

## Reference(s):

- [Slack Bot on ClawHub](https://clawhub.ai/oomol/skills/oo-slackbot)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Slack](https://slack.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live action schemas before constructing Slack action payloads.]

## Skill Version(s):

1.0.1 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
