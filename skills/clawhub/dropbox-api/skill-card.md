## Description:

Dropbox API integration with managed OAuth for files, folders, search, metadata, and cloud storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Dropbox through Maton-managed OAuth, list and search files, retrieve metadata, upload or download content, and manage folders or revisions with user confirmation for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Dropbox files and metadata through an authorized Maton connection.

Mitigation: Authorize only the Dropbox account needed for the task, prefer OAuth and read-only scopes where possible, and revoke unused connections when finished.

Risk: Write, delete, upload, sharing, or connection changes can modify or expose Dropbox data.

Mitigation: Confirm the exact account, connection, resource identifiers, payload, and intended effect before any data-changing operation.

Risk: Long-lived Maton API keys can leak through logs, shell history, files, or child processes when raw HTTP is used.

Mitigation: Use the CLI-managed OAuth flow when available; if raw HTTP is required, keep the key in the process environment only, never print or persist it, and send it only to api.maton.ai.

## Reference(s):

- [Dropbox HTTP API Overview](https://www.dropbox.com/developers/documentation/http/overview)
- [Dropbox Developer Portal](https://www.dropbox.com/developers)
- [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/)
- [DBX File Access Guide](https://developers.dropbox.com/dbx-file-access-guide)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API calls, JSON, Guidance]

**Output Format:** [Markdown with inline bash, Python, JavaScript, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and an authorized Dropbox connection.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
