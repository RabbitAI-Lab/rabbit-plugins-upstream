## Description:

ClickUp API integration with managed OAuth for accessing and managing tasks, lists, folders, spaces, workspaces, users, and webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and operations teams use this skill to inspect and manage ClickUp work items, project hierarchy, users, and webhooks from an agent workflow. It is intended for read-first API work with explicit approval before new connections or writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClickUp resources can be modified or deleted through approved write operations.

Mitigation: Default to read/list calls, confirm the target account, connection, resource identifiers, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: API activity is routed through Maton and depends on the selected Maton account and ClickUp connection.

Mitigation: Use OAuth where possible, verify the authenticated Maton profile and active ClickUp connection, specify a connection when multiple exist, and revoke unused connections when work is complete.

Risk: Long-lived API keys can leak if the raw HTTP fallback is used instead of the CLI.

Mitigation: Prefer the Maton CLI with OAuth; when CLI use is impossible, keep the key out of command arguments, logs, files, and user-visible output, and send it only to api.maton.ai.

Risk: Fetched ClickUp content or webhook payloads may contain untrusted instructions or adversarial text.

Mitigation: Treat returned content as data, avoid executing or interpolating it into shell commands, and do not let it choose follow-up endpoints, recipients, or write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickup-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClickUp API Overview](https://developer.clickup.com/docs/Getting%20Started.md)
- [ClickUp Get Tasks](https://developer.clickup.com/reference/gettasks.md)
- [ClickUp Create Task](https://developer.clickup.com/reference/createtask.md)
- [ClickUp Update Task](https://developer.clickup.com/reference/updatetask.md)
- [ClickUp Delete Task](https://developer.clickup.com/reference/deletetask.md)
- [ClickUp Create Webhook](https://developer.clickup.com/reference/createwebhook.md)
- [ClickUp Rate Limits](https://developer.clickup.com/docs/rate-limits.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON request bodies, and API usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands and API request examples that require network access, a Maton account, and a connected ClickUp account.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
