## Description:

Discord聊天 helps an agent send, reply to, search, read, react to, edit, and delete Discord channel messages through the message tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and automation teams use this skill to coordinate Discord workflows such as support replies, announcements, channel searches, reactions, and message maintenance. It is best suited to explicit Discord tasks where the target channel, message, and permission scope are clear.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad local read, write, and exec capabilities even though its main workflow is Discord messaging.

Mitigation: Grant only the minimum agent permissions needed for the exact workflow, and avoid enabling exec or write unless they are required.

Risk: Discord edit, delete, bulk cleanup, and MANAGE_MESSAGES workflows can modify or remove channel content.

Mitigation: Require manual confirmation before edits, deletions, bulk cleanup, or any action using elevated Discord permissions.

Risk: Messages may disclose sensitive information to Discord channels if prompts or retrieved history are not reviewed.

Mitigation: Review destination channels and message content before sending, and redact secrets or private data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/discord-chat)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline message command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Discord message actions that require configured bot access and user confirmation for edits, deletions, or privileged moderation actions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
