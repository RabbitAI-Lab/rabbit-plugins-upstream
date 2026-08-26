## Description:

Google Docs API integration with managed OAuth for creating documents, inserting text, applying formatting, and managing content through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Google Docs through a managed OAuth gateway, list or view documents, and perform approved document creation or content updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses Maton as an OAuth gateway for Google Docs account access.

Mitigation: Install only if Maton is trusted for the account, authorize the narrowest available Google scopes, and revoke unused Google Docs connections.

Risk: Google Docs write or delete operations can modify user documents.

Mitigation: Default to read and list operations, then confirm the target document, payload, and intended effect before any write or delete operation.

Risk: Fallback API-key use can expose a long-lived Maton credential.

Mitigation: Prefer OAuth through the Maton CLI; when a key is unavoidable, avoid printing, logging, persisting, or passing it on the command line.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-docs)
- [Maton homepage](https://maton.ai)
- [Maton docs](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Docs API overview](https://developers.google.com/docs/api/how-tos/overview)
- [Google Docs API: Get Document](https://developers.google.com/docs/api/reference/rest/v1/documents/get)
- [Google Docs API: Create Document](https://developers.google.com/docs/api/reference/rest/v1/documents/create)
- [Google Docs API: Batch Update](https://developers.google.com/docs/api/reference/rest/v1/documents/batchUpdate)
- [Google Docs API request types](https://developers.google.com/docs/api/reference/rest/v1/documents/request)
- [Google Docs document structure](https://developers.google.com/docs/api/concepts/structure)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval for Google Docs connection creation or write operations.]

## Skill Version(s):

1.1.0 (source: ClawHub release evidence, released 2026-08-26; artifact frontmatter version 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
