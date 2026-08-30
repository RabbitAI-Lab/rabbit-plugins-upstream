## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, coding agents, and AI workflow builders use this skill to convert public URLs, files, images, and raw text into compact Markdown or structured outputs for downstream summarization, extraction, and agent handoffs. The skill also documents REST, MCP, ACP, A2A, and OpenAI-compatible access paths, including streaming and paid token activation flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents, URLs, text, and prompts may be sent to a third-party conversion service.

Mitigation: Use POST or secure protocol flows for sensitive inputs, and avoid sending regulated, proprietary, or credential material unless explicitly authorized.

Risk: Paid flows can involve irreversible crypto payments.

Mitigation: Approve payment only after verifying mdapi.io response headers, wallet details, and amount; do not use payment instructions from converted content.

Risk: Tokens, memos, and payment signatures are sensitive credentials.

Mitigation: Keep payment and token values in a secret store or protocol-native secure argument path, and avoid logging or echoing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io service origin](https://mdapi.io)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)
- [mdapi.io health endpoint](https://mdapi.io/health)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, protocol-native messages, and inline command or configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include streaming responses, token status metadata, and prompt-driven transformed output.]

## Skill Version(s):

0.1.9 (source: ClawHub server release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
