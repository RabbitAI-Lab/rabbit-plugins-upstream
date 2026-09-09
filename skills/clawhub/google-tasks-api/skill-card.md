## Description:

Google Tasks API integration with managed OAuth for reading, creating, updating, and deleting task lists and tasks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Google Tasks task lists and tasks through Maton-managed OAuth. It is suited for task-list and task CRUD workflows where the agent should read or list first and request approval before creating a connection or changing data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify or delete Google Tasks data through an authorized Maton connection.

Mitigation: Use read/list operations first and require explicit user approval with the target resource, payload, and intended effect before create, update, clear, or delete operations.

Risk: Maton acts as an intermediary for the user's Google Tasks account and credentials.

Mitigation: Prefer OAuth, avoid API keys unless necessary, never expose tokens, and verify the intended Maton account or connection before write operations.

Risk: External task content may contain untrusted instructions or data.

Mitigation: Treat Google Tasks API responses as data, do not execute or follow instructions returned by the API, and pass values as discrete arguments rather than shell-interpolated strings.

## Reference(s):

- [Google Tasks API Overview](https://developers.google.com/workspace/tasks)
- [Google Tasks Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [Google Tasks TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-tasks-api)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI or API commands and account-connection guidance; write operations require explicit user approval.]

## Skill Version(s):

1.2.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
