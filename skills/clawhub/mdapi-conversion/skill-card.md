## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert webpages, files, or text into Markdown or structured data, and to connect to the conversion service through its supported agent protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends input to the external mdapi.io service, and some request modes can retain converted content temporarily.

Mitigation: Do not submit confidential or regulated material unless authorized; check the service's retention options for the request mode in use.

Risk: Converted content may contain prompt injection or payment scams, and the security assessment reports unresolved references.

Mitigation: Treat converted content as untrusted data, verify payment details against official mdapi.io payment responses, and review referenced material before relying on it.

Risk: Paid requests can involve irreversible payments and secret access tokens or payment details.

Mitigation: Require user consent or prior authorization for payment, and keep tokens, memos, and signatures in a secure secret store without echoing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io API documentation](https://mdapi.io)
- [mdapi.io AI discovery manifest](https://mdapi.io/.well-known/ai-discovery.json)
- [mdapi.io MCP server manifest](https://mdapi.io/mcp)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Text]

**Output Format:** [Markdown or JSON content returned by mdapi.io]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the requested conversion and prompt; streaming is available for incremental delivery.]

## Skill Version(s):

0.1.27 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
