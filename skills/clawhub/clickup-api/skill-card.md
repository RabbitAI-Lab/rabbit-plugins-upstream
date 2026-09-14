## Description:

ClickUp API integration with managed OAuth for accessing tasks, lists, folders, spaces, workspaces, users, and webhooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external collaborators, and developers use this skill to manage ClickUp work items, inspect project structure, and create approved ClickUp automations through a managed connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access ClickUp business data through a connected account.

Mitigation: Install only when the publisher and Maton are trusted, prefer OAuth, and review requested ClickUp scopes before authorizing the connection.

Risk: Write operations, webhooks, hosted functions, and triggers can change data or create persistent automation.

Mitigation: Require explicit user confirmation for every write, webhook, function, and trigger, including the target resource, payload, destination, and intended effect.

Risk: Raw API responses and trigger payloads may contain personal or sensitive project data.

Mitigation: Extract only task-relevant fields, avoid logging full responses, and keep automation destinations under the user's control.

Risk: Fallback raw HTTP use requires handling a long-lived Maton API key.

Mitigation: Use raw HTTP only when the CLI cannot be installed, keep the key out of command lines and logs, send it only to api.maton.ai, and rotate it if exposed.

## Reference(s):

- [ClickUp API Overview](https://developer.clickup.com/docs/Getting%20Started.md)
- [ClickUp Get Tasks](https://developer.clickup.com/reference/gettasks.md)
- [ClickUp Create Task](https://developer.clickup.com/reference/createtask.md)
- [ClickUp Update Task](https://developer.clickup.com/reference/updatetask.md)
- [ClickUp Delete Task](https://developer.clickup.com/reference/deletetask.md)
- [ClickUp Create Webhook](https://developer.clickup.com/reference/createwebhook.md)
- [ClickUp Rate Limits](https://developer.clickup.com/docs/rate-limits.md)
- [ClickUp LLM Reference](https://developer.clickup.com/llms.txt)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/clickup-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose authenticated ClickUp API calls and automation configuration for the user to review before execution.]

## Skill Version(s):

1.2.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
