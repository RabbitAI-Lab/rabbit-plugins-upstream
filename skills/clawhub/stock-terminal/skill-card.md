## Description:

Stock terminal for AI agents that turns chat commands and natural-language stock questions into read-only, synthesized financial terminal reports across price, sentiment, insider trades, congressional disclosures, institutional flows, analyst ratings, AI insights, and embedded news.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn stock research requests into read-only, data-grounded terminal-style market reports. Builders can also use it as guidance for implementing a SentiSense-backed agent terminal with API-key authentication and grounded tool calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-key exposure or excessive credential scope.

Mitigation: Provide only SENTISENSE_API_KEY through the host environment, keep it out of model-visible messages and user-facing output, and use it only for read-only SentiSense API calls.

Risk: Unbounded headline or embed fetching could broaden the skill into general browsing or expose unsafe third-party markup.

Mitigation: Use a narrow, hardened fetcher only for URLs returned by SentiSense document payloads, and sanitize or sandbox any third-party embed HTML.

Risk: Market outputs could be mistaken for personalized investment advice.

Mitigation: Frame outputs as informational market data and educational synthesis, not as buy, sell, or personalized investment recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense website](https://sentisense.ai)
- [SentiSense full API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown terminal-style reports with inline code, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data synthesis; requires SENTISENSE_API_KEY for authenticated SentiSense API calls.]

## Skill Version(s):

1.7.0 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
