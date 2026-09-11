## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, comments, and related Podio resources through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations teams, and agents use this skill to inspect and manage Podio organizations, spaces, apps, items, tasks, comments, and files from an authenticated Podio account. It is intended for task-oriented Podio API access where read operations are preferred first and write operations require explicit user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Maton API passthrough can reach Podio endpoints beyond the examples documented in the skill when the connected account is authorized for them.

Mitigation: Use OAuth where possible, grant the narrowest available Podio access, specify the intended connection for each task, and revoke unused connections promptly.

Risk: POST, PUT, PATCH, and DELETE calls can modify or delete Podio data, trigger notifications, run hooks, or cause irreversible connection deletion.

Mitigation: Default to read and list calls first, then require explicit user approval that names the target resource, payload, and intended effect before any write or deletion.

Risk: Podio API responses may contain personal data, business records, comments, or external content that should not be broadly logged or reused.

Mitigation: Extract only the fields needed for the task, avoid dumping full responses into logs or files, and treat returned content as untrusted data rather than instructions.

Risk: Long-lived Maton API keys and provider-issued tokens can be exposed if printed, placed on command lines, or written to files.

Mitigation: Prefer OAuth-backed credential storage, never print or persist credentials, avoid command-line secrets, and send Maton API keys only to api.maton.ai.

## Reference(s):

- [ClawHub Podio Skill](https://clawhub.ai/byungkyu/skills/podio)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Podio API Documentation](https://developers.podio.com/doc)
- [Podio API Authentication](https://developers.podio.com/authentication)
- [Podio Items API](https://developers.podio.com/doc/items)
- [Podio Tasks API](https://developers.podio.com/doc/tasks)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, JSON, markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON request or response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Podio API paths, Maton CLI commands, request bodies, response field summaries, and approval prompts for write operations.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
