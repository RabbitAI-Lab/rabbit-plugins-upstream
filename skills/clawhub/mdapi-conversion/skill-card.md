## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert webpages, files, and text into Markdown or structured data, and to request prompt-driven extraction or summarization through REST and supported agent protocols. It also supports streaming and payment flows when a conversion requires payment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted content may be processed by an external conversion service, and provider retention claims were not independently audited.

Mitigation: Submit only content you are authorized to process; use POST for sensitive inputs and ttl=0 to disable conversion caching.

Risk: A2A task records are retained temporarily, and task and context IDs provide access to task data.

Mitigation: Keep task and context IDs private.

Risk: Payment credentials and payment actions can expose secrets or cause irreversible charges.

Mitigation: Protect service credentials, approve irreversible payments, or configure a wallet spending limit.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)
- [mdapi.io AI discovery manifest](https://mdapi.io/.well-known/ai-discovery.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Structured data]

**Output Format:** [Markdown or JSON, depending on the requested response mode]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Prompt-driven transformations can return converted content, extracted results, or both; streaming is available for long responses.]

## Skill Version(s):

0.1.22 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
