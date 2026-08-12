## Description:

Drive a self-hosted Huly workspace through the `huly` CLI for issues, projects, cards, documents, calendars, channels, DMs, actions, todos, time tracking, notifications, and approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamcoder18](https://clawhub.ai/user/iamcoder18)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect and manage a self-hosted Huly workspace from the command line. It supports common project tracking, collaboration, scheduling, document, card, notification, approval, and workspace administration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to make broad changes in a Huly workspace using the configured account's permissions.

Mitigation: Use a least-privilege service account and verify the active workspace, target project, and target object with JSON reads before any mutation.

Risk: Raw `huly ws` and `huly api` commands can bypass normal CLI guardrails and mutate production data directly.

Mitigation: Reserve raw API/RPC escape hatches for cases where the standard CLI cannot perform the task, and require explicit review of the exact method, payload, and target workspace before execution.

Risk: Delete and bulk-change workflows can remove or alter issues, workspaces, notifications, documents, cards, channels, calendars, and related records.

Mitigation: Require explicit user confirmation for deletes and bulk operations, use preview or dry-run commands where available, and inspect target records before proceeding.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamcoder18/skills/huly)
- [Auth and setup](references/auth-and-setup.md)
- [Issues and todos](references/issues-and-todos.md)
- [Tracker projects](references/tracker-projects.md)
- [Cards](references/cards.md)
- [Documents](references/documents.md)
- [Chat and collaboration](references/chat-and-collaboration.md)
- [Calendar and schedule](references/calendar-and-schedule.md)
- [Notifications and approvals](references/notifications-and-approvals.md)
- [Workspace and user](references/workspace-and-user.md)
- [Spaces, types, and relations](references/spaces-types-and-relations.md)
- [Escape hatches and internals](references/escape-hatches-and-internals.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Huly CLI commands, JSON-read guidance, and confirmation prompts before destructive or bulk changes.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
