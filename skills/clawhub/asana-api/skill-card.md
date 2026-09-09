## Description:

Asana API integration with managed OAuth for accessing tasks, projects, workspaces, users, and webhooks through the Maton CLI and SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, developers, and work-management teams use this skill to inspect and manage Asana tasks, projects, workspaces, users, and webhooks from an agent workflow. It is most appropriate when the user intends to connect an Asana account through Maton and approve any write or new connection before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Asana tasks, projects, workspaces, users, and webhooks through an authorized Maton connection.

Mitigation: Connect only the intended Asana account, prefer least-privilege OAuth scopes, start with read/list calls, and require user confirmation for connection creation or any POST, PUT, PATCH, or DELETE operation.

Risk: Using a long-lived Maton API key can expose credentials through environment variables, logs, shell history, or child processes.

Mitigation: Prefer the Maton CLI OAuth flow and operating-system credential storage; if raw HTTP access is unavoidable, keep the key only in the current process environment, never print or persist it, and rotate it if exposed.

Risk: Webhook creation sends Asana event data to an external target URL and can create downstream automation side effects.

Mitigation: Confirm the resource identifier, webhook target, filters, and intended effect with the user before creating or updating webhooks.

## Reference(s):

- [ClawHub Asana skill page](https://clawhub.ai/byungkyu/skills/asana-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Asana API Documentation](https://developers.asana.com)
- [Asana API Reference](https://developers.asana.com/reference)
- [Asana LLM Reference](https://developers.asana.com/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API call plans and Maton CLI or SDK examples; live API results depend on the user's authorized Asana and Maton connection.]

## Skill Version(s):

1.2.1 (source: server release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
