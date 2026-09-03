## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, coding agents, and AI agent systems use this skill to convert public URLs, files, images, and raw text into Markdown or structured data for downstream analysis, summarization, extraction, and multi-agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents, URLs, images, or text are sent to the third-party mdapi.io service for processing.

Mitigation: Use only authorized inputs and avoid secrets, internal infrastructure URLs, regulated data, or proprietary material unless approval and data handling requirements are satisfied.

Risk: The skill supports crypto payment and token activation flows where payments are irreversible.

Mitigation: Review payment prompts carefully, confirm the amount and recipient, and proceed only with explicit consent or an approved delegated spending limit.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io service documentation](https://mdapi.io)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, structured data, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON, with optional streaming protocol frames and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include converted Markdown, prompt results, token status, and protocol-specific response metadata; payment tokens, memos, and signatures should not be exposed.]

## Skill Version(s):

0.1.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
