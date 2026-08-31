## Description:

TickTick API integration with managed OAuth for managing tasks, projects, and task lists through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to TickTick through Maton, inspect tasks and projects, and make user-approved changes such as creating, updating, completing, or deleting tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton-mediated TickTick access can expose or modify tasks, projects, and task lists in the connected account.

Mitigation: Use read and list calls first, verify the target account or connection, and require explicit user approval before any POST, PUT, PATCH, or DELETE operation.

Risk: Long-lived Maton API keys can leak through environment variables, logs, shell history, or command-line arguments.

Mitigation: Prefer OAuth through the Maton CLI and avoid printing, persisting, or passing API keys on the command line.

Risk: Multiple Maton profiles or TickTick connections can cause writes to land in the wrong account.

Mitigation: Specify the intended profile or connection when more than one exists and confirm resource identifiers before changing data.

## Reference(s):

- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with CLI command examples and JSON request or response snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user approval before connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
