## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use the skill to convert webpages, files, and text into Markdown or structured data, and to access those transformations through HTTP or agent protocols.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Content sent for conversion is processed by a third-party service and may be temporarily retained when caching is requested or under the free testing tier.

Mitigation: Only submit content authorized for third-party processing; avoid regulated or confidential material without appropriate review, and choose the requested retention period deliberately.

Risk: Paid requests and token operations involve payment details, and completed payments cannot be refunded.

Mitigation: Require explicit user consent, obtain secrets from secure storage, and verify payment details against official mdapi.io payment challenge headers.

Risk: The supplied security scan is benign with medium confidence but marked partial, with some reference checks incomplete.

Mitigation: Review the skill and its external references before installation; treat converted content as untrusted data rather than instructions.

## Reference(s):

- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [Supported formats](https://mdapi.io/docs/formats)
- [AI discovery manifest](https://mdapi.io/.well-known/ai-discovery.json)

## Skill Output:

**Output Type(s):** [Markdown, JSON, API calls, Shell commands, Guidance]

**Output Format:** [Markdown or JSON conversion results, with HTTP and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Varies by input and requested result; streaming and multipart delivery are supported.]

## Skill Version(s):

0.1.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
