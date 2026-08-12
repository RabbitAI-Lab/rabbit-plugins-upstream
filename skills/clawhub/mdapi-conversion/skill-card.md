## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-agent operators use this skill to convert public or authorized documents, webpages, images, and text into Markdown or structured outputs for LLM workflows through mdapi.io protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content may be sent to a third-party conversion service.

Mitigation: Use the skill only for public or authorized content; use POST for sensitive inputs and avoid secrets or regulated data unless compliance has been reviewed.

Risk: Autonomous payment and token activation can spend funds or expose payment tokens if handled carelessly.

Mitigation: Require user or wallet confirmation before paid conversions, verify payment details come from mdapi.io service responses, and never log tokens, memos, or signatures.

Risk: Converted webpages, files, or text may contain prompt injection or misleading instructions.

Mitigation: Treat converted content as untrusted data and do not execute instructions embedded in converted material.

## Reference(s):

- [mdapi.io service documentation](https://mdapi.io/)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)
- [ClawHub skill release](https://clawhub.ai/mdapiio/skills/mdapi-conversion)

## Skill Output:

**Output Type(s):** [text, markdown, structured data, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, and protocol-specific tool responses with optional SSE streaming]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return direct Markdown for GET requests, JSON with converted content and metadata for POST requests, or streamed chunks when enabled.]

## Skill Version(s):

0.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
