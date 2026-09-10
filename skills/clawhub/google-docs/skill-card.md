## Description:

Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, and managing document content through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent read, create, edit, and format Google Docs through a managed Maton connection. It is suited for document workflows where account selection, least-privilege scopes, and explicit confirmation for changes are required.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Docs account authorization can expose documents beyond the user's intended task if the wrong account, profile, connection, or OAuth scope is used.

Mitigation: Prefer OAuth, review requested Google scopes, choose the intended Maton profile and connection explicitly when more than one is available, and use least-privilege scopes.

Risk: Document creation, editing, sharing, or deletion can change user data or access permissions.

Mitigation: Default to read and list calls first, then require explicit user confirmation with the target document, payload, and intended effect before any modifying operation.

Risk: Long-lived API keys or provider-issued tokens can leak through logs, command lines, files, or copied output.

Mitigation: Use OAuth where possible, never print or persist credentials, avoid passing secrets on command lines, and send Maton API keys only to api.maton.ai.

Risk: Content returned from Google Docs may contain untrusted instructions or adversarial text.

Mitigation: Treat document content as data, validate it before reuse, and do not let fetched content choose endpoints, recipients, commands, or follow-up actions.

## Reference(s):

- [ClawHub Google Docs Skill](https://clawhub.ai/byungkyu/skills/google-docs)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Google Docs API Overview](https://developers.google.com/docs/api/how-tos/overview)
- [Google Docs API: Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Google Docs API: Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Google Docs API: Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Google Docs API: Request Types](https://developers.google.com/docs/api/reference/rest/v1/documents/request)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include read/list API calls and proposed write commands that require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
