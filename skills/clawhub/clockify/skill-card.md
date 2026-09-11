## Description:

Clockify API integration with managed OAuth for tracking time and managing projects, clients, tasks, tags, workspaces, and workspace members.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect and manage Clockify data through Maton, including time entries, workspaces, projects, clients, tasks, tags, and workspace members. It defaults to read and list operations and requires explicit user approval before connection creation or data-changing API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, modify, or delete Clockify business records.

Mitigation: Review the target resource, payload, and intended effect before approving any POST, PUT, PATCH, or DELETE operation.

Risk: API key authentication can expose a long-lived Maton credential if mishandled.

Mitigation: Prefer OAuth login and avoid printing, logging, persisting, or passing API keys on command lines.

Risk: Requests can affect the wrong Clockify or Maton account when multiple connections or profiles exist.

Mitigation: Specify the intended connection and profile for account-sensitive operations.

## Reference(s):

- [Clockify Skill on ClawHub](https://clawhub.ai/byungkyu/skills/clockify)
- [Maton Homepage](https://maton.ai)
- [Clockify API Documentation](https://docs.clockify.me/)
- [Clockify Time Entry API Reference](https://docs.clockify.me/#tag/Time-entry)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose Maton CLI, raw HTTPS, Python SDK, or JavaScript SDK calls; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
