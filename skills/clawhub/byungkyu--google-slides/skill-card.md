## Description:

Google Slides API integration with managed OAuth for creating presentations, adding slides, inserting content, and managing slide formatting through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to read, create, and update Google Slides presentations through a managed Maton OAuth connection. It supports presentation retrieval, slide creation, text and image insertion, formatting updates, and batch updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify Google Slides content through an authorized Maton connection.

Mitigation: Use OAuth where possible, select the narrowest available Google scopes, verify the target presentation, and require explicit user confirmation before any write operation.

Risk: Using the API-key fallback can expose a long-lived credential through environment variables, logs, shell history, or copied output.

Mitigation: Prefer the Maton CLI OAuth flow; when an API key is unavoidable, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Ambiguous Maton accounts or Google Slides connections can cause reads or writes against the wrong account.

Mitigation: List active connections first and specify the intended connection or profile before acting.

## Reference(s):

- [Google Slides API Overview](https://developers.google.com/slides/api/reference/rest)
- [Google Slides Presentations](https://developers.google.com/slides/api/reference/rest/v1/presentations)
- [Google Slides Pages](https://developers.google.com/slides/api/reference/rest/v1/presentations.pages)
- [Google Slides BatchUpdate](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can propose Maton CLI calls, SDK snippets, and Google Slides API request payloads; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
