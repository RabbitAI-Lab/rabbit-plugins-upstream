## Description:

Dropbox API integration with managed OAuth for files, folders, search, metadata, and cloud storage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to Dropbox through Maton-managed OAuth, list and search files, inspect metadata, and perform approved file operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill routes Dropbox access through Maton as an OAuth/API gateway, so Dropbox account access depends on trusting that gateway.

Mitigation: Install only if the user trusts Maton for Dropbox access, prefer the CLI OAuth flow, and approve each new connection explicitly.

Risk: Dropbox write actions such as upload, delete, move, share, or other modifications can change or expose user data.

Mitigation: Default to read and list operations, verify the target account and resource identifiers, and require explicit user approval before every write action.

Risk: The MATON_API_KEY/raw HTTP fallback can expose a long-lived credential and the server security guidance identifies a read-only Dropbox API v2 protocol mistake in the appendix.

Mitigation: Avoid the raw HTTP fallback unless the CLI cannot be used; when raw HTTP is unavoidable, keep the key out of logs and commands and use POST with the required request body, such as JSON null, for Dropbox API v2 calls.

## Reference(s):

- [Dropbox HTTP API Overview](https://www.dropbox.com/developers/documentation/http/overview)
- [Dropbox Developer Portal](https://www.dropbox.com/developers)
- [Dropbox API Explorer](https://dropbox.github.io/dropbox-api-v2-explorer/)
- [DBX File Access Guide](https://developers.dropbox.com/dbx-file-access-guide)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related ClawHub API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, API calls, markdown]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Dropbox authorization.]

## Skill Version(s):

1.2.0 (source: server release metadata; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
