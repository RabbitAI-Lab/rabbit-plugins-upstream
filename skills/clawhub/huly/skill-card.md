## Description:

Drive a self-hosted Huly workspace through the `huly` CLI - issues, projects, cards, documents, calendars, channels, DMs, actions/todos, time tracking, notifications, and approvals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamcoder18](https://clawhub.ai/user/iamcoder18)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to manage a self-hosted Huly workspace from the command line. It helps select and run the right Huly CLI commands for project tracking, cards, documents, collaboration, calendars, notifications, approvals, time tracking, and workspace administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use existing Huly credentials to make broad changes in a real workspace, including destructive actions.

Mitigation: Use a limited service account, prefer a test workspace first, verify the target with read commands, and require confirmation for deletes.

Risk: Raw `huly ws` and `huly api` commands can perform mutations outside the normal high-level command flow.

Mitigation: Reserve raw commands for gaps in the CLI, review payloads before execution, and require confirmation before raw mutation calls.

Risk: Ambiguous productivity or save requests may affect the wrong workspace, project, or Huly object.

Mitigation: Ask for the target workspace and object when context is missing, and avoid acting on ambiguous requests that do not explicitly name Huly and the target.

## Reference(s):

- [Auth & setup](references/auth-and-setup.md)
- [Issues & actions (todos)](references/issues-and-todos.md)
- [Projects, components, milestones, issue templates](references/tracker-projects.md)
- [Cards](references/cards.md)
- [Documents](references/documents.md)
- [Channels, DMs, threads, activity](references/chat-and-collaboration.md)
- [Calendar, schedule, time](references/calendar-and-schedule.md)
- [Notifications & approvals](references/notifications-and-approvals.md)
- [Workspace & user](references/workspace-and-user.md)
- [Spaces, relations, type configuration](references/spaces-types-and-relations.md)
- [Escape hatches & internals](references/escape-hatches-and-internals.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline Huly CLI commands and JSON-oriented command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read-before-write checks, dry-run guidance, and confirmation steps before destructive workspace changes.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
