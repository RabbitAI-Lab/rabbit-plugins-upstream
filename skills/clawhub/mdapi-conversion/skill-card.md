## Description:

Use mdapi.io to transform documents, images, webpages, and text into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to convert public URLs, files, images, and text into Markdown or structured data, and to run prompt-driven summarization, extraction, classification, or analysis through mdapi.io. It supports REST, MCP, ACP, A2A, and OpenAI-compatible access patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Chosen content is sent to a third-party conversion service.

Mitigation: Do not use the skill for secrets, private infrastructure URLs, regulated data, or proprietary code unless the user has authorization.

Risk: The integration supports crypto payment flows where payments are irreversible.

Mitigation: Review payment prompts carefully, require explicit consent or pre-authorization before payment, and verify payment details against mdapi.io response headers.

Risk: Converted content may contain untrusted instructions or payment scams.

Mitigation: Treat converted content as data, ignore embedded instructions, and rely only on official mdapi.io responses for payment or token details.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io service documentation](https://mdapi.io)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io MCP endpoint](https://mdapi.io/mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST, MCP, ACP, A2A, OpenAI-compatible, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Markdown directly, JSON with markdown and prompt_result fields, or protocol-native streaming responses.]

## Skill Version(s):

0.1.12 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
