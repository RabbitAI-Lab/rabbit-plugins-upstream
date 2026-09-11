## Description:

Airtable API integration with managed OAuth for managing bases, tables, and records through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Airtable bases, query records, and perform approved create, update, or delete operations through Maton-managed OAuth.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Airtable access is mediated through Maton, so the user must trust Maton as the gateway for the connected Airtable account.

Mitigation: Prefer OAuth, grant only scopes needed for the task, and confirm that Maton is acceptable before installation or connection.

Risk: Create, update, and delete operations can change or remove Airtable data.

Mitigation: Default to read and list calls first, then require explicit confirmation of the target resource, payload, and intended effect before any write or delete.

Risk: The installation examples use unpinned third-party CLI and SDK package commands.

Mitigation: Pin or otherwise verify Maton CLI and SDK versions in controlled environments before use.

Risk: API-key fallback mode can expose a long-lived Maton credential through environment variables, logs, shell history, or process output.

Mitigation: Use the CLI OAuth flow when possible; if a key is unavoidable, do not print, persist, or pass it on a command line, and send it only to api.maton.ai.

## Reference(s):

- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Airtable API Overview](https://airtable.com/developers/web/api/introduction)
- [Airtable List Records](https://airtable.com/developers/web/api/list-records)
- [Airtable Create Records](https://airtable.com/developers/web/api/create-records)
- [Airtable Update Record](https://airtable.com/developers/web/api/update-record)
- [Airtable Delete Record](https://airtable.com/developers/web/api/delete-record)
- [Airtable Formula Reference](https://support.airtable.com/docs/formula-field-reference)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Airtable API paths, request payloads, and CLI or SDK examples; write and delete actions require explicit user confirmation.]

## Skill Version(s):

1.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
