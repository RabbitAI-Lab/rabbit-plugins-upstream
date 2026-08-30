## Description:

Podio API integration with managed OAuth for managing workspaces, apps, items, tasks, and comments through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect and manage Podio organizations, workspaces, apps, items, tasks, comments, and files through a managed OAuth gateway. It is suited for Podio account workflows where read operations are preferred by default and writes require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can authorize Maton to access a user's Podio account.

Mitigation: Use OAuth when possible, review the selected Maton account and Podio connection, and create new connections only after explicit user approval.

Risk: Podio writes can create, update, delete, comment, share, or trigger workflows in connected workspaces.

Mitigation: Default to read and list calls, then confirm the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: API-key fallback exposes a long-lived Maton credential to the local environment.

Mitigation: Prefer OAuth and use the raw HTTP fallback only when the CLI cannot be installed; never print, persist, or pass the key on a command line.

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

**Output Type(s):** [Guidance, Shell commands, API Calls, Code, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton OAuth or API-key authentication and may return Podio API JSON responses.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
