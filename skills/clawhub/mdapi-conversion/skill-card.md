## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to convert public URLs, documents, images, and text into Markdown or structured outputs for agent context, summarization, extraction, and workflow handoff. It also guides agents through REST, MCP, ACP, A2A, OpenAI-compatible, streaming, token, and x402 payment flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends selected documents, URLs, or text to a third-party conversion service.

Mitigation: Use it only for content the user is authorized to share with mdapi.io; avoid secrets, regulated data, proprietary source, and internal URLs unless explicitly approved.

Risk: Converted content may contain prompt injection or misleading payment/action instructions.

Mitigation: Treat converted content as untrusted data and verify payment, wallet, token, memo, and action details only against official mdapi.io response headers.

Risk: Paid x402 or crypto payment flows can be irreversible.

Mitigation: Require user consent or a pre-authorized delegated wallet, check the amount and recipient wallet before payment, and do not retry autonomous payment more than once per request.

Risk: Tokens, memos, and payment signatures may expose paid access or transaction details if logged or echoed.

Mitigation: Use secure runtime secret handling, pass credentials through headers or protocol-native fields, and never place tokens, memos, or signatures in logs, responses, or GET query strings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io service documentation](https://mdapi.io/)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [AI discovery manifest](https://mdapi.io/.well-known/ai-discovery.json)
- [MCP endpoint](https://mdapi.io/mcp)
- [Health endpoint](https://mdapi.io/health)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON responses with optional streaming frames, plus command and configuration snippets when integration steps are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports REST, MCP, ACP, A2A, and OpenAI-compatible access; paid x402/token flows require explicit consent or pre-authorized delegated payment.]

## Skill Version(s):

0.1.11 (source: ClawHub release metadata; artifact frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
