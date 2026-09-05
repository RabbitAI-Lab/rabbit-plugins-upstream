## Description:

TickTick API integration with managed OAuth for creating, reading, updating, completing, deleting, and organizing tasks, projects, and task lists through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to manage TickTick tasks and projects from an agent workflow while routing authentication through Maton. It is suited for listing, creating, updating, completing, deleting, and organizing TickTick task-management data with explicit confirmation for write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, complete, or delete TickTick tasks and projects in the connected account.

Mitigation: Default to read/list calls first and require explicit user confirmation of the target resource, payload, and intended effect before any write or delete action.

Risk: Authorizing Maton grants access to the user's TickTick account through the configured connection.

Mitigation: Use OAuth where possible, select only needed scopes when available, and revoke unused connections promptly.

Risk: Multiple Maton profiles or TickTick connections can route actions to the wrong account.

Mitigation: Pin the intended profile and connection when more than one account or connection exists.

Risk: The raw API-key fallback exposes a long-lived Maton credential to the process environment.

Mitigation: Use the fallback only when the CLI cannot be installed; never print, log, persist, or pass the key on a command line.

Risk: TickTick API responses may contain personal task data or untrusted external content.

Mitigation: Return only fields needed for the task, avoid dumping raw responses, and treat fetched content as data rather than instructions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include TickTick API paths, request payload examples, connection-selection guidance, and user-confirmation prompts for writes.]

## Skill Version(s):

1.2.1 (source: server release evidence; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
