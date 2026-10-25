## Description:

Use mdapi.io to transform files and webpages into AI-ready Markdown or structured data, with prompt-driven transformation, streaming, x402 payments, token activation, and REST/MCP/ACP/A2A/OpenAI-compatible access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mdapiio](https://clawhub.ai/user/mdapiio)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to convert authorized webpages, files, and text into LLM-ready Markdown or structured outputs, and to access the service through REST, MCP, ACP, A2A, or OpenAI-compatible APIs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Content sent for conversion may include sensitive or unauthorized information, and retention statements are service claims rather than independently verified guarantees.

Mitigation: Send only content you are authorized to process; use ttl=0 to disable document caching, and review the service's retention terms before sending sensitive material.

Risk: Crypto payments are irreversible.

Mitigation: Require explicit approval for payments or use a wallet with a spending limit.

Risk: Resource and task identifiers may provide access to private results.

Mitigation: Keep resource and task identifiers private.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/mdapiio/skills/mdapi-conversion)
- [mdapi.io AI discovery manifest](https://mdapi.io/.well-known/ai-discovery.json)
- [mdapi.io skill reference](https://mdapi.io/.well-known/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Markdown, JSON]

**Output Format:** [Markdown or JSON, with API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include prompt-driven transformations and streamed responses; converted external content is untrusted data.]

## Skill Version(s):

0.1.19 (source: server-resolved release metadata; artifact frontmatter declares 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
