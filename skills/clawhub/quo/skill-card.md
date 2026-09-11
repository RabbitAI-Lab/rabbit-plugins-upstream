## Description:

Quo API integration with managed OAuth for managing calls, messages, contacts, and conversations in a business phone system.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to work with Quo business-phone data through Maton, including listing calls and messages, sending SMS, managing contacts, and retrieving call recordings or transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access sensitive business-phone calls, messages, contacts, conversations, recordings, and transcripts.

Mitigation: Use OAuth with the least Quo scopes needed, verify that Maton is trusted as the gateway provider, and prefer reviewed or pinned CLI and SDK versions.

Risk: Write operations can send SMS, create or update contacts, delete records, or act on the wrong account or connection.

Mitigation: Confirm exact connection IDs, recipients, contact IDs, payloads, and intended effects before any POST, PUT, PATCH, DELETE, or connection deletion.

Risk: Using raw API keys or direct HTTP fallback can expose long-lived credentials through the environment, logs, command history, or pasted output.

Mitigation: Prefer the Maton CLI OAuth flow; when fallback API-key use is unavoidable, keep keys out of command lines and output, avoid persistence, and send them only to api.maton.ai.

## Reference(s):

- [Quo API Introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Quo API Authentication](https://www.quo.com/docs/mdx/api-reference/authentication)
- [Quo Support Center API Integrations](https://support.quo.com/core-concepts/integrations/api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON examples, and SDK code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Quo API requests through the Maton CLI or SDKs; write operations require explicit user confirmation.]

## Skill Version(s):

1.2.0 (source: server release evidence; artifact frontmatter reports 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
