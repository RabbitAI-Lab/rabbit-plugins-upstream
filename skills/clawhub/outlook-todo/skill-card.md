## Description:

Read and write Microsoft To Do via its own Microsoft Graph device-code login; enumerate task lists, read and filter tasks, and create, update, complete, or delete tasks with explicit write confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[guoxh](https://clawhub.ai/user/guoxh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect and manage Microsoft To Do or Outlook.com task lists through Microsoft Graph from a command-line agent workflow. It supports setup, token management, task reads, and confirmed task writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores OAuth token material locally and uses Microsoft To Do read/write access.

Mitigation: Install only for accounts where this access is acceptable, protect ~/.outlook-todo/, avoid committing or backing it up, and clear tokens or revoke Microsoft consent when the skill is no longer needed.

Risk: Task write operations can create, update, complete, or delete Microsoft To Do tasks.

Mitigation: Review dry-run previews before execution and use --apply plus typed YES or an explicit --yes flag only when the proposed change is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/guoxh/skills/outlook-todo)
- [Microsoft Graph To Do Notes](references/graph-todo.md)
- [Microsoft Graph API endpoint](https://graph.microsoft.com)
- [Microsoft identity platform endpoint](https://login.microsoftonline.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands; script output can be summary text, JSON, IDs, or raw JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, jq, curl, and python3; writes configuration and OAuth tokens under ~/.outlook-todo/.]

## Skill Version(s):

1.0.8 (source: server release metadata, released 2026-09-07T14:48:17Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
