## Description:

Airtable API integration with managed OAuth for reading, creating, updating, and deleting Airtable bases, tables, and records through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to connect Airtable through Maton OAuth, inspect bases and schemas, query records, and perform reviewed record changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent could use the wrong Airtable connection or account.

Mitigation: Confirm the intended Airtable connection before use and specify the connection when more than one is available.

Risk: The connected Airtable account could grant broader access than the task requires.

Mitigation: Prefer least-privilege OAuth scopes and use read/list calls first to verify context.

Risk: Record creation, update, or deletion could change user data unexpectedly.

Mitigation: Review every proposed write or deletion with the target resource, payload, and intended effect before approval.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Airtable API Overview](https://airtable.com/developers/web/api/introduction)
- [Airtable List Records](https://airtable.com/developers/web/api/list-records)
- [Airtable Create Records](https://airtable.com/developers/web/api/create-records)
- [Airtable Update Record](https://airtable.com/developers/web/api/update-record)
- [Airtable Delete Record](https://airtable.com/developers/web/api/delete-record)
- [ClawHub Airtable Skill](https://clawhub.ai/byungkyu/skills/airtable)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user confirmation before connection creation or write operations.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
