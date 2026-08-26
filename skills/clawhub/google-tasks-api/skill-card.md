## Description:

Google Tasks API integration with managed OAuth for reading, creating, updating, and deleting task lists and tasks through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Google Tasks task lists and tasks from an agent session while relying on Maton for OAuth-backed API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Task and task-list write operations can modify, delete, or clear Google Tasks data.

Mitigation: Default to read and list calls, then confirm the target resource, payload, and intended effect before any create, update, move, clear, or delete operation.

Risk: An ambiguous Maton profile or Google Tasks connection can route an action to the wrong account.

Mitigation: Specify the intended Google Tasks account or connection when more than one connection exists, especially before writes.

Risk: Maton API keys and OAuth tokens are sensitive credentials that can be exposed through logs, shell history, or files.

Mitigation: Use OAuth where possible and avoid printing, storing, logging, or passing credentials on command lines.

## Reference(s):

- [Google Tasks API Overview](https://developers.google.com/workspace/tasks)
- [Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may call the Maton CLI or SDK and require network access, a Maton account, and an active Google Tasks connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
