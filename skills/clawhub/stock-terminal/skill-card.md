## Description:

Provides compact, sourced stock research views and, when requested, guidance for building a local chat-and-canvas financial terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, researchers, and developers use the skill to answer market-data questions with dated price, sentiment, news, filing, analyst, earnings, and options context. On explicit request, developers can use its references to build a local financial terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SentiSense API key is required for market-data requests.

Mitigation: Provide the key only if comfortable using the read-only service; keep it out of responses and generated files.

Risk: Delayed or partial market data may be mistaken for current, complete coverage or investment advice.

Mitigation: Show source dates and preview limits, distinguish missing data, and treat results as informational context rather than financial advice.

Risk: Natural-language finance requests may trigger an unwanted stock-data lookup.

Mitigation: State explicitly when a stock-data lookup is or is not wanted.

## Reference(s):

- [ClawHub stock-terminal release](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [Local terminal build guide](artifact/references/build-in-an-afternoon.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries and tables, with optional build instructions and code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dated, read-only market context; local app artifacts only on explicit request.]

## Skill Version(s):

2.1.0 (source: ClawHub server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
