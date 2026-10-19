## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert webpages, files, and text into Markdown or structured results for downstream analysis and automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content is sent to a third-party conversion service.

Mitigation: Do not submit secrets, regulated data, internal URLs, or proprietary files without authorization.

Risk: Converted content may be cached beyond the request.

Mitigation: Use ttl=0 or avoid ttl for sensitive conversions.

Risk: Tokens and payment memos may be exposed if copied into requests or logs.

Mitigation: Keep credentials in secure storage and omit them from URLs, logs, and output.

Risk: Cryptocurrency payments cannot be reversed.

Mitigation: Get authorization and verify payment details before paying.

## Reference(s):

- [mdapi-conversion on ClawHub](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON conversion results; request examples and integration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional prompt-based transformation and streaming responses.]

## Skill Version(s):

0.1.17 (source: ClawHub release; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
