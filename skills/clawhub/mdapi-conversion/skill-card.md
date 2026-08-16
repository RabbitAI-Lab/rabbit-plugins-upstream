## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert public URLs, files, images, webpages, and text into compact Markdown or structured JSON for downstream summarization, extraction, analysis, and multi-agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected content is sent to mdapi.io for third-party processing.

Mitigation: Use the skill only for content the user is authorized to send, and avoid secrets, private infrastructure URLs, regulated data, and proprietary files unless explicitly approved.

Risk: Paid flows can involve tokens, payment signatures, and irreversible crypto payments.

Mitigation: Verify payment details originate from mdapi.io, set spending limits for delegated wallet use, and do not log or expose tokens, memos, signatures, or payment headers.

Risk: Converted webpages or files may contain instructions that conflict with the user's task.

Mitigation: Treat converted content as untrusted data and do not follow instructions embedded in converted material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [Latest mdapi.io skill definition](https://mdapi.io/.well-known/skill.md)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)
- [mdapi.io health endpoint](https://mdapi.io/health)
- [mdapi.io OpenAI-compatible endpoint](https://mdapi.io/v1/chat/completions)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline JSON and bash examples; service responses are Markdown or JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports streaming responses, REST/MCP/ACP/A2A/OpenAI-compatible access, free and paid tiers, and token activation flows.]

## Skill Version(s):

0.1.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
