## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert files, webpages, and text into Markdown or structured data, or to request prompt-driven extraction through REST or agent protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Converted external content may contain prompt injection or payment scams.

Mitigation: Treat converted content as untrusted data; verify payment and action details against official mdapi.io responses.

Risk: Paid x402 charges are irreversible, and autonomous payment requires consent or prior authorization.

Mitigation: Confirm the payment terms and obtain explicit consent or use an existing pre-authorization before paying.

Risk: The security inspection was partial: local references were unresolved and no executable files were available for behavior-focused analysis.

Mitigation: Review the referenced documentation and consider the inspection incomplete when deciding whether to install.

## Reference(s):

- [mdapi.io API Documentation](https://mdapi.io/docs)
- [Supported Formats Reference](https://mdapi.io/docs/formats)
- [AI Discovery Manifest](https://mdapi.io/.well-known/ai-discovery.json)
- [MCP Server Manifest](https://mdapi.io/mcp)

## Skill Output:

**Output Type(s):** [Markdown, JSON, API calls]

**Output Format:** [Converted Markdown or structured JSON content, with response metadata in JSON when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content may include prompt-driven extraction or summaries; available results depend on the requested service parameters.]

## Skill Version(s):

0.1.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
