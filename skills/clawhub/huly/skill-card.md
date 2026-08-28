## Description:

Drive a self-hosted Huly workspace through the `huly` CLI for tracker issues, projects, chat, calendar events, todos, time entries, notifications, approvals, and workspace automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamcoder18](https://clawhub.ai/user/iamcoder18)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to automate a self-hosted Huly workspace through the `huly` CLI. It supports project tracking, scheduling, collaboration, approvals, notifications, and workspace administration when the user has confirmed any write or persistent action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change a Huly workspace, including persistent records, notifications, approvals, and destructive actions.

Mitigation: Require explicit user confirmation before write, send, log, delete, raw SDK, or other persistent actions, and verify the target workspace, project, person, and object before mutating.

Risk: Using the third-party `huly` CLI requires trusting the CLI and protecting credentials for the target Huly workspace.

Mitigation: Install only when the third-party CLI is trusted, prefer least-privilege service accounts or short-lived tokens, and avoid inventing or exposing credentials.

Risk: Public, notification-sending, scheduling, and recipient-targeted actions can affect other users or create visible side effects.

Mitigation: Clarify workspace, recipient, visibility, and timezone before execution, and confirm public or notification-sending actions explicitly.

## Reference(s):

- [huly skill instructions](SKILL.md)
- [Auth & setup](references/auth-and-setup.md)
- [Issues & actions](references/issues-and-todos.md)
- [Projects, components, milestones, issue templates](references/tracker-projects.md)
- [Channels, DMs, threads, activity](references/chat-and-collaboration.md)
- [Cards](references/cards.md)
- [Documents](references/documents.md)
- [Calendar, schedule, time](references/calendar-and-schedule.md)
- [Workspace & user](references/workspace-and-user.md)
- [Spaces, relations, type configuration](references/spaces-types-and-relations.md)
- [Notifications & approvals](references/notifications-and-approvals.md)
- [Direct SDK and HTTP access](references/direct-sdk-access.md)
- [huly CLI repository](https://github.com/IamCoder18/huly-cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-oriented command output recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Directs agents to use `--json` for programmatic reads, confirm write and destructive actions, and ask for missing workspace, recipient, or timezone context.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
