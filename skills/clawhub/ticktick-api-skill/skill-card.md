## Description:

TickTick API integration with managed OAuth for creating, updating, completing, and organizing tasks, projects, and task lists through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent manage TickTick tasks and projects through an authenticated Maton connection while keeping write operations and automation steps subject to explicit approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires granting Maton access to a user's TickTick account.

Mitigation: Use OAuth when possible, connect only the account needed for the task, and confirm the user is comfortable authorizing TickTick access before installation or connection creation.

Risk: Write operations can create, update, complete, or delete TickTick projects and tasks.

Mitigation: Default to read and list calls, then obtain explicit approval for the target resource, payload, and intended effect before any modifying operation.

Risk: Automation through hosted functions, triggers, or destinations can create ongoing data flows.

Mitigation: Require separate approval for automation setup, especially trigger destinations, and keep functions scoped to reviewed code, approved connections, and least-privilege network settings.

Risk: Using a Maton API key instead of OAuth can expose a long-lived credential.

Mitigation: Prefer OAuth; when an API key is unavoidable, keep it out of logs, command lines, files, and output, and rotate it if exposure occurs.

## Reference(s):

- [TickTick skill on ClawHub](https://clawhub.ai/byungkyu/skills/ticktick-api-skill)
- [Maton homepage](https://maton.ai)
- [TickTick Developer Portal](https://developer.ticktick.com/)
- [TickTick Help Center](https://help.ticktick.com/)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated Maton CLI or API calls, TickTick request and response examples, and approval-oriented guidance for writes and automation.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
