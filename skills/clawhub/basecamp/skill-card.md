## Description:

Basecamp API integration with managed OAuth for managing projects, to-dos, messages, schedules, documents, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to work with Basecamp through Maton-managed authentication, including project, to-do, message, schedule, document, and team collaboration tasks. It is intended for Basecamp API actions that the user has requested, with read/list operations preferred and explicit approval required for writes, new connections, hosted functions, or persistent automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Basecamp write operations, connection creation, and connection deletion can modify data or change account access.

Mitigation: Default to read and list operations; require explicit user approval for connection creation and every POST, PUT, PATCH, or DELETE action.

Risk: Hosted functions and triggers can create persistent automation that continues after the immediate chat turn.

Mitigation: Use hosted functions or triggers only when requested by name, summarize the handler, connection scope, destination, and network policy before approval, and revoke unused connections or automations.

Risk: Raw HTTP fallback requires a long-lived Maton API key that can be exposed through logs, command lines, files, or child processes.

Mitigation: Prefer OAuth through the Maton CLI; when raw HTTP is unavoidable, read the key from the environment only, never print or persist it, and send it only to api.maton.ai.

Risk: Basecamp responses and trigger payloads can contain personal, business, or third-party data.

Mitigation: Extract only the fields needed for the task, avoid dumping raw responses or payloads into logs or shared surfaces, and prefer Maton-controlled destinations unless the user approves another host.

## Reference(s):

- [Basecamp 4 API Documentation](https://github.com/basecamp/bc3-api)
- [Basecamp Authentication Guide](https://github.com/basecamp/bc3-api/blob/master/sections/authentication.md)
- [Basecamp API Reference](https://github.com/basecamp/bc3-api#endpoints)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce authenticated Basecamp API call plans, Maton CLI commands, raw HTTP examples, hosted function snippets, and trigger configuration guidance.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
