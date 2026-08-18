## Description:

Use for Sendbird Chat Platform API v3 server-side integration - users, group channels, open channels, messages, metadata, moderation, bots, announcements, and statistics - with caller-owned application credentials and preview-first mutation confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pontjs](https://clawhub.ai/user/pontjs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to discover and call Sendbird Chat Platform API v3 endpoints with their own Sendbird application credentials. It supports read workflows and chat-management mutations by previewing requests first and requiring explicit confirmation before state-changing actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide powerful Sendbird chat-management actions such as sending messages, moderating users, scheduling announcements, and deleting channels.

Mitigation: Review dry-run request previews carefully and require explicit confirmation before executing any mutation.

Risk: Sendbird application tokens could be exposed through logs, commits, or copied request examples.

Mitigation: Keep SENDBIRD_API_TOKEN in the local environment, use a scoped token where possible, and do not print or commit credentials.

Risk: Callers may need to satisfy Sendbird terms and their own data-compliance requirements when using application data.

Mitigation: Confirm the caller's Sendbird terms and data-compliance posture before using the skill on production application data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pontjs/skills/pontx-sendbird-chat-platform)
- [Sendbird Chat Platform API base URL](https://api-{app_id}.sendbird.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API request previews, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses caller-owned Sendbird application credentials and preview-first confirmation for mutations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
