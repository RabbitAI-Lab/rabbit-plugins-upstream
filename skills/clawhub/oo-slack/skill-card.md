## Description:

Slack enables agents to read, search, create, update, schedule, upload, react to, and delete Slack workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and automation agents use this skill to operate Slack conversations, messages, users, reactions, and files from a connected OOMOL account. It supports Slack read workflows plus user-confirmed write and destructive workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change Slack state by posting, replying, updating, scheduling, uploading, reacting, or opening conversations.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

Risk: The skill can remove or overwrite Slack data through delete and remove-reaction actions.

Mitigation: Require explicit approval for the specific target before running destructive actions.

Risk: Slack read and search results may include sensitive workspace data.

Mitigation: Treat returned messages, users, files, and conversation data as sensitive and share only what is needed for the task.

## Reference(s):

- [Slack homepage](https://slack.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed and authenticated oo CLI plus an OOMOL-connected Slack account]

## Skill Version(s):

1.0.4 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
