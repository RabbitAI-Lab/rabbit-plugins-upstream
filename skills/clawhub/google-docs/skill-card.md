## Description:

Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, managing content, and making confirmed read/write calls through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to work with Google Docs through Maton-managed OAuth, including document retrieval, creation, text insertion, formatting, and content updates. The skill is suited to workflows that need read-first API access with explicit user approval before connecting accounts or modifying documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on Google Docs content through a connected Google account.

Mitigation: Authorize only trusted Maton connections, review OAuth scopes, prefer read-only access where possible, and revoke unused connections after use.

Risk: Document writes, deletes, or formatting changes may alter user data.

Mitigation: Default to read/list operations first and require explicit user confirmation of the target document, payload, and intended effect before any modifying request.

Risk: API keys or OAuth tokens could be exposed if handled outside the credential store.

Mitigation: Use Maton OAuth and the CLI credential store when available; do not print, persist, or pass credentials on command lines.

Risk: Content returned from Google Docs may contain untrusted instructions or adversarial text.

Mitigation: Treat fetched document content as data, validate it before reuse, and do not let it choose follow-up endpoints, recipients, commands, or actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/google-docs)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Google Docs API Overview](https://developers.google.com/docs/api/how-tos/overview)
- [Google Docs API: Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Google Docs API: Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Google Docs API: Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Google Docs API: Request Types](https://developers.google.com/docs/api/reference/rest/v1/documents/request)
- [Google Docs API: Document Structure](https://developers.google.com/docs/api/concepts/structure)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces task guidance for Maton CLI, Maton API gateway, and optional SDK usage; Google Docs writes require explicit user approval.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
