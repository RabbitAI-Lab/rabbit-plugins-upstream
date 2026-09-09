## Description:

mumo runs multi-model deliberation across models from different labs through its MCP server, returning full responses and typed cross-model reactions for high-regret decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use mumo to get independent model perspectives on architecture choices, product tradeoffs, design reviews, launch risks, and security-sensitive plans before committing to an implementation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, specs, code excerpts, and security or payment designs may be processed by mumo and multiple model providers.

Mitigation: Redact secrets, tokens, customer data, payment data, private URLs, and unnecessary proprietary details before invoking the skill.

Risk: The mumo bearer API key is stored in local OpenClaw configuration.

Mitigation: Protect ~/.openclaw/openclaw.json as a secret-bearing file, avoid logging or committing it, and rotate the key if it is exposed.

Risk: Multi-model deliberation is advisory and may produce incorrect or misleading guidance.

Mitigation: Validate recommendations against the project context, tests, and human review before making workspace or production changes.

## Reference(s):

- [mumo Product](https://mumo.chat)
- [mumo OpenClaw Install Guide](https://mumo.chat/install/openclaw)
- [mumo MCP Reference](https://mumo.chat/docs/mcp)
- [mumo REST API](https://mumo.chat/docs/api)
- [OpenClaw Documentation](https://docs.openclaw.ai)
- [ClawHub mumo Listing](https://clawhub.ai/ericatmumo/skills/mumo)
- [Claim Maps](references/claim-maps.md)
- [Model Selection](references/model-selection.md)
- [Operating Notes](references/operating-notes.md)
- [Snippets](references/snippets.md)
- [Synthesis](references/synthesis.md)
- [Takeaway](references/takeaway.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured panel summaries, inline shell commands, and configuration JSON where setup is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include model responses, claim-map links, typed reactions, snippets, and follow-up round prompts.]

## Skill Version(s):

0.6.1 (source: evidence release and CHANGELOG, released 2026-09-08)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
