## Description:

Use folkctl to inspect and update folk.app CRM data through its REST API. Covers people, companies, groups, members, custom fields, deals, custom objects, users, notes, tasks, interactions, legacy reminders, webhooks, and official MCP setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[j-edel](https://clawhub.ai/user/j-edel)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect, create, and update folk.app CRM records through the folkctl CLI and Folk REST API. It is suited for CRM automation, data review, task management, webhook setup, and MCP configuration workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a Folk API key that can expose or modify CRM data if mishandled.

Mitigation: Use a least-privilege key, keep it in environment variables or approved secret storage, and never paste or print it in chat or logs.

Risk: Create, update, delete, webhook, and field-option operations can change CRM state or remove associated contact data.

Mitigation: Run dry-run previews first, review the exact resource and request body, and require explicit user confirmation before deletes or webhook changes.

Risk: The skill installs and delegates work to a pinned external folkctl source.

Mitigation: Confirm trust in the pinned source before installation, install with lifecycle scripts disabled as documented, and verify the CLI version before providing credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/j-edel/skills/folk-cli)
- [folkctl repository](https://github.com/j-edel/folkctl)
- [Folk reminders-to-tasks migration guide](https://developer.folk.app/migrations/reminders-to-tasks)
- [Folk MCP tools reference](https://developer.folk.app/mcp/tools)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for agent-mediated CLI use with dry-run previews before mutations.]

## Skill Version(s):

0.2.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
