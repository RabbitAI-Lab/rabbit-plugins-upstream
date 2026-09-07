## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, comments, and related Podio resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation agents use this skill to connect to a user-approved Podio account, inspect Podio organizations and workspaces, and read or modify apps, items, tasks, and comments with confirmation for write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton brokers access to the connected Podio account.

Mitigation: Install only when Podio access through Maton is intended, use OAuth where possible, and select the narrowest Podio scopes available.

Risk: Write and delete operations can modify or remove Podio data.

Mitigation: Default to read and list calls, verify the target resource and connection, and require explicit user confirmation before POST, PUT, PATCH, DELETE, or connection deletion.

Risk: The raw API-key fallback uses a long-lived credential.

Mitigation: Avoid the API-key path unless the CLI cannot be used, keep the key out of command lines, logs, files, and pasted output, and prefer OAuth-backed CLI access.

Risk: Podio responses may include personal or business-sensitive content.

Mitigation: Extract only the fields needed for the task and avoid dumping or storing full response bodies unless the user explicitly requests it.

Risk: Fetched Podio content may contain untrusted instructions or data.

Mitigation: Treat API responses as data, validate identifiers and payloads, and do not let returned content choose endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub Podio skill](https://clawhub.ai/byungkyu/skills/podio)
- [ClawHub publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Podio API Documentation](https://developers.podio.com/doc)
- [Podio API Authentication](https://developers.podio.com/authentication)
- [Podio Items API](https://developers.podio.com/doc/items)
- [Podio Tasks API](https://developers.podio.com/doc/tasks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should minimize response data, prefer read and list operations first, and request explicit user confirmation before writes, deletes, or new connections.]

## Skill Version(s):

1.2.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
