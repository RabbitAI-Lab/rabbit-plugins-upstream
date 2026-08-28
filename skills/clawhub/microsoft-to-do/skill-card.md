## Description:

Microsoft To Do API integration with managed OAuth for managing task lists, tasks, checklist items, and linked resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to create, read, update, and delete Microsoft To Do task lists, tasks, checklist items, and linked resources through Maton-managed OAuth access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A Maton-connected workflow can read and modify Microsoft To Do data.

Mitigation: Use OAuth, grant only the needed Microsoft To Do access, approve writes only after checking the exact task or list and payload, and revoke unused Maton connections.

Risk: Requests can affect the wrong Microsoft To Do account when multiple Maton connections or profiles exist.

Mitigation: Specify the intended connection or profile before API calls, especially before any create, update, or delete operation.

Risk: Long-lived API keys can leak through environment variables, logs, command history, or pasted output.

Mitigation: Prefer OAuth and the Maton CLI credential store; if an API key is unavoidable, keep it out of command arguments and rotate it if exposed.

Risk: Task content and linked-resource data returned by the Microsoft To Do API may contain untrusted instructions.

Mitigation: Treat returned content as data, validate it before reuse, and do not let fetched content choose follow-up endpoints, recipients, or shell commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/microsoft-to-do)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Microsoft To Do API Overview](https://learn.microsoft.com/en-us/graph/api/resources/todo-overview)
- [todoTaskList Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotasklist)
- [todoTask Resource](https://learn.microsoft.com/en-us/graph/api/resources/todotask)
- [checklistItem Resource](https://learn.microsoft.com/en-us/graph/api/resources/checklistitem)
- [linkedResource Resource](https://learn.microsoft.com/en-us/graph/api/resources/linkedresource)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user confirmation before write operations.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
