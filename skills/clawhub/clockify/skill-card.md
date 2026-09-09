## Description:

Clockify API integration with managed OAuth for tracking time and managing projects, clients, tasks, workspaces, members, and related timekeeping resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to inspect and manage Clockify time tracking data through Maton-managed OAuth. It supports read-first workflows for users, workspaces, projects, clients, tags, tasks, time entries, and workspace members, with confirmation before connection creation or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can act on Clockify account data through Maton-mediated access.

Mitigation: Install only when comfortable granting this access, use OAuth where possible, and connect only the account needed for the task.

Risk: Writes or deletes could affect the wrong Clockify workspace, project, task, client, tag, or time entry.

Mitigation: Confirm the exact account, workspace, resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE operation.

Risk: The raw API-key fallback may expose a long-lived credential if handled carelessly.

Mitigation: Prefer OAuth through the Maton CLI and use the API-key fallback only when the CLI cannot be used.

## Reference(s):

- [ClawHub Clockify Skill](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton](https://maton.ai)
- [Clockify API Documentation](https://docs.clockify.me/)
- [Clockify Time Entry API Reference](https://docs.clockify.me/#tag/Time-entry)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and explicit user confirmation before creating connections or performing writes.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
