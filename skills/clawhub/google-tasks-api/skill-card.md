## Description:

Google Tasks API integration with managed OAuth for reading and managing task lists and tasks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect, create, update, move, and delete Google Tasks task lists and tasks from an agent session while relying on Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A task or task list could be created, changed, moved, cleared, or deleted in the connected Google Tasks account.

Mitigation: Require explicit user confirmation for every write operation, including the target resource, payload, and intended effect.

Risk: A broad or unintended Google Tasks connection could expose more account data than the current task needs.

Mitigation: Use OAuth, review connection prompts, choose the narrowest available Google Tasks scopes, and specify the intended connection when multiple accounts are connected.

Risk: Long-lived API keys or provider tokens could leak if printed, logged, stored, or passed through shell commands.

Mitigation: Prefer OAuth and keep credentials in the operating system credential store; never print, persist, or pass credential values on a command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-tasks-api)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Google Tasks API Overview](https://developers.google.com/workspace/tasks)
- [Google Tasks Tasks Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasks)
- [Google Tasks TaskLists Reference](https://developers.google.com/workspace/tasks/reference/rest/v1/tasklists)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands, JSON snippets, and API guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands or API-call guidance; write operations require user confirmation.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
