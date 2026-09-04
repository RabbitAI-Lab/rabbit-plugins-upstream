## Description:

Baserow API integration with managed API key authentication for managing database rows, fields, and tables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to read, create, update, delete, filter, sort, and batch-manage Baserow database rows through Maton-managed API access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad API passthrough can read or modify Baserow resources beyond simple row and table operations.

Mitigation: Default to read and list requests, verify the target account and resource identifiers first, and require explicit user approval before every write or upload.

Risk: Local file uploads can transfer file contents into Baserow.

Mitigation: Confirm the exact file, destination field, and intended effect before uploading, and avoid uploading files unless the user has approved the transfer.

Risk: Maton or provider credentials can be exposed if printed, logged, persisted, or passed through shell commands.

Mitigation: Prefer OAuth login through the Maton CLI, keep credentials in the operating system credential store, and never print, export, persist, or transmit credential values outside the documented Maton flow.

Risk: API responses may contain untrusted content that could try to influence subsequent agent behavior.

Mitigation: Treat Baserow response content as data, validate it before reuse, and do not let fetched content choose follow-up endpoints, recipients, commands, or prompts.

## Reference(s):

- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Baserow API Spec (OpenAPI)](https://api.baserow.io/api/redoc/)
- [Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces Maton CLI and SDK guidance for Baserow API calls; writes and connection creation require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
