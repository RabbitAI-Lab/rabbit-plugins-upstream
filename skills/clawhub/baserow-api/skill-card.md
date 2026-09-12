## Description:

Baserow API integration with managed API key authentication for managing database rows, fields, tables, filtering, sorting, batch operations, and file uploads through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to read, create, update, delete, filter, sort, and upload data in Baserow workspaces through Maton-managed API access. It is intended for Baserow database operations where reads are preferred first and writes, deletes, uploads, or new connections require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Database writes, deletes, uploads, and connection changes can alter or expose Baserow workspace data.

Mitigation: Default to read and list operations first, verify target identifiers and payloads, and obtain explicit user confirmation before any write, delete, upload, or connection creation action.

Risk: Long-lived API keys and provider credentials can leak through environment variables, logs, files, command history, or broad process inheritance.

Mitigation: Prefer OAuth and the Maton CLI credential store, avoid printing or persisting credentials, send raw API keys only to api.maton.ai when CLI use is impossible, and rotate any key that was exposed.

Risk: Overbroad Baserow authorization can allow access beyond the immediate task, including endpoints reachable through the Maton API passthrough.

Mitigation: Grant only needed Baserow scopes, use a specific connection when multiple accounts exist, prefer read-only scopes where possible, and revoke unused connections.

Risk: Upload-via-url asks Baserow to fetch external content into the workspace.

Mitigation: Confirm the source URL and intended destination with the user before upload, and treat externally sourced content as untrusted.

Risk: Multipart upload bodies can temporarily contain copies of user files.

Mitigation: Use owner-only temporary files created with umask 077 and mktemp, and remove them with a trap on exit.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/baserow-api)
- [Maton Homepage](https://maton.ai)
- [Baserow API Documentation](https://baserow.io/api-docs)
- [Baserow Database API](https://baserow.io/user-docs/database-api)
- [Database Tokens](https://baserow.io/user-docs/personal-api-tokens)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI commands, raw HTTP examples, API request payloads, and Baserow response interpretation guidance.]

## Skill Version(s):

1.2.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
