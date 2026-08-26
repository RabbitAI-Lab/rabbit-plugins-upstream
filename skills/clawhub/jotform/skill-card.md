## Description:

JotForm API integration with managed OAuth for creating forms, managing submissions, accessing form data, and managing webhooks through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with a connected JotForm account: listing account data, retrieving forms and submissions, creating or deleting forms, and managing webhooks after user approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read or modify forms, submissions, metadata, and webhooks in the connected JotForm account.

Mitigation: Use read/list calls first, confirm target resources and payloads before write or delete operations, and approve only recognized changes.

Risk: A new JotForm connection grants account access through Maton.

Mitigation: Create connections only after explicit user approval, prefer least-privilege scopes when available, and specify the intended connection when multiple accounts are connected.

Risk: Raw API-key fallback can expose a long-lived credential if the CLI cannot be used.

Mitigation: Prefer Maton OAuth and use the raw API-key path only when CLI installation is unavailable; never print, persist, or pass the key on a command line.

## Reference(s):

- [JotForm API Overview](https://api.jotform.com/docs/)
- [JotForm User Forms API](https://api.jotform.com/docs/#user-forms)
- [JotForm Form Submissions API](https://api.jotform.com/docs/#form-id-submissions)
- [JotForm Webhooks API](https://api.jotform.com/docs/#form-id-webhooks)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [ClawHub JotForm Skill](https://clawhub.ai/byungkyu/skills/jotform)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected JotForm account; defaults to read/list operations and requires user approval for writes or new connections.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
