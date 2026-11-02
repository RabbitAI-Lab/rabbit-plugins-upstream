## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use mdapi.io to convert files, webpages, or text into AI-ready Markdown or structured data through HTTP and agent protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted content may be processed or cached by a third-party service, and A2A requests retain temporary task records.

Mitigation: Send only authorized content; prefer POST with ttl=0 for private input, and keep passwords and task identifiers private.

Risk: Crypto payments are irreversible.

Mitigation: Require explicit approval or use a capped delegated wallet.

## Reference(s):

- [mdapi.io](https://mdapi.io)
- [mdapi.io skill documentation](https://mdapi.io/.well-known/skill.md)
- [ClawHub skill page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Converted text or structured data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include prompt-driven summaries or extracted data.]

## Skill Version(s):

0.1.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
