## Description:

Stock terminal for AI agents that returns synthesized stock research reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news while remaining read-only with no trading, purchases, write operations, or wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research workflows use this skill to turn ticker commands or natural-language market questions into concise, data-grounded stock terminal screens. It is intended for informational research and education, not personalized investment advice or trade execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data calls.

Mitigation: Use the SENTISENSE_API_KEY environment variable so the key stays in host process state and is not placed in prompts, tool arguments, emitted events, or conversation history.

Risk: The optional npx CLI authentication flow can persist the API key locally.

Mitigation: Prefer environment-variable authentication when local credential caching is not acceptable, or remove stored CLI credentials after use.

Risk: Financial outputs could be mistaken for investment recommendations.

Mitigation: Frame responses as informational and educational market research, preserve the no-advice posture, and do not present outputs as personalized buy, sell, or hold recommendations.

Risk: Market data and generated summaries can be stale, delayed, incomplete, or unavailable.

Mitigation: Require tool-grounded data before quoting prices, percentages, ratings, headlines, or dates, and disclose missing or delayed readings instead of filling gaps from memory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with terminal-style reports, inline code examples, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data responses require SENTISENSE_API_KEY; optional CLI authentication can store the API key locally.]

## Skill Version(s):

1.8.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
