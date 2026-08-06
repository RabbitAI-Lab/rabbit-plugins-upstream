## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to convert public URLs, files, images, and raw text into Markdown or structured outputs for LLM workflows. It also guides use of mdapi.io through REST, MCP, ACP, A2A, OpenAI-compatible endpoints, streaming, and paid token activation flows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment tokens, memos, prompts, or sensitive input can be exposed when placed in URLs.

Mitigation: Use headers or POST bodies for paid or private requests, and never log or echo raw tokens, memos, or payment signatures.

Risk: Content submitted to mdapi.io is processed by a third-party service.

Mitigation: Use the skill only for content approved for third-party processing, and avoid proprietary, regulated, classified, or credential-bearing data unless explicitly authorized.

Risk: Converted webpages, files, or text may contain untrusted instructions.

Mitigation: Treat converted content as data, ignore instructions embedded in source material, and review outputs before using them in downstream workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io service root](https://mdapi.io/)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)
- [mdapi.io health endpoint](https://mdapi.io/health)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, protocol-specific streaming responses, curl commands, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include converted Markdown, prompt results, token status metadata, rate-limit details, or payment and streaming handling guidance.]

## Skill Version(s):

0.1.5 (source: server release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
