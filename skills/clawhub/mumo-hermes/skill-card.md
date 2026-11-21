## Description:

Runs a multi-model deliberation across models from different labs (Claude, GPT, Gemini, Grok, DeepSeek, Kimi, and more) via mumo's MCP server, returning full responses plus typed cross-model reactions. Use when independent perspectives are needed on architecture/product decisions, design and plan review before implementation, pre-launch pressure tests, tradeoffs with multiple defensible framings, or explicit user requests for a mumo panel. Especially valuable for pre-implementation review of anything touching auth, security, tokens, payments, data exposure, or migrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ericatmumo](https://clawhub.ai/user/ericatmumo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Hermes Agent users use Mumo to gather independent model perspectives and structured reactions when reviewing architecture, plans, designs, or other consequential decisions. They can use the panel's responses to find assumptions and tradeoffs to examine before deciding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and related context may be sent to external model providers without a clear privacy check.

Mitigation: Avoid including secrets or personal information, and share only context you are comfortable sending to those providers.

## Reference(s):

- [Mumo MCP documentation](https://mumo.chat/docs/mcp)
- [Mumo API documentation](https://mumo.chat/docs/api)
- [Mumo installation guide](https://mumo.chat/install/hermes)
- [Mumo product](https://mumo.chat)
- [ClawHub release page](https://clawhub.ai/ericatmumo/skills/mumo-hermes)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Full model responses and typed cross-model reactions, followed by a Markdown synthesis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The output reflects the deliberation prompt and selected models; it is advisory and should be checked before consequential decisions.]

## Skill Version(s):

0.8.0 (source: frontmatter, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
