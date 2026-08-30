## Description:

Fathom API integration with managed OAuth for retrieving meeting recordings, transcripts, summaries, and action items, plus managing webhook notifications through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to access Fathom meeting data, search recordings, retrieve summaries and transcripts, and manage webhooks through Maton OAuth. It is intended for read-first API work with explicit user confirmation for connection creation and write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access meeting recordings, transcripts, summaries, and webhook management in the connected Fathom account.

Mitigation: Prefer OAuth, connect only the intended Fathom account, use least-privilege scope choices when available, and revoke unused connections.

Risk: Write operations and webhook changes can modify account state or trigger downstream effects.

Mitigation: Default to read and list calls first, then confirm the target resource, payload, and intended effect before connection creation or any POST, PUT, PATCH, or DELETE call.

Risk: Meeting content and webhook payloads may include sensitive or untrusted third-party data.

Mitigation: Treat API responses as data, avoid executing or interpolating returned content into commands, and avoid printing, logging, or persisting credentials or provider-issued tokens.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/fathom-api)
- [Maton Homepage](https://maton.ai)
- [Fathom API Documentation](https://developers.fathom.ai)
- [Fathom LLM Reference](https://developers.fathom.ai/llms.txt)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, API paths, JSON examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a connected Fathom account; raw HTTP fallback should be used only when the CLI cannot be installed.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
