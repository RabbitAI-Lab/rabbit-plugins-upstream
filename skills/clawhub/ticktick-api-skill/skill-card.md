## Description:

TickTick API integration with managed OAuth for managing tasks, projects, and task lists through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to TickTick through Maton, list task and project data, and create, update, complete, or delete tasks and projects with user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and change TickTick tasks and projects through Maton.

Mitigation: Default to read/list operations, verify account and resource identifiers, and require explicit user confirmation before creating connections or performing writes.

Risk: A long-lived MATON_API_KEY may be exposed if used outside the recommended OAuth flow.

Mitigation: Use OAuth where possible; if an API key is unavoidable, keep it out of files, logs, command lines, and user-visible output.

Risk: TickTick task or project content may contain untrusted external data.

Mitigation: Treat returned content as data only, and do not execute or follow instructions embedded in API responses.

## Reference(s):

- [ClawHub TickTick Skill](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Maton CLI/API requests that require network access and user-confirmed TickTick access.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
