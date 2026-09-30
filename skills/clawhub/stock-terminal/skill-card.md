## Description:

Answers stock research questions with compact, sourced market views and provides a guide for building a local financial terminal on explicit request.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors and researchers use the skill to explore sourced prices, sentiment, news, filings, earnings, and options data without placing trades. Developers can use its reference contracts and guide to build a local chat-and-canvas research terminal when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A SentiSense API key is required for market-data calls.

Mitigation: Keep the key in the environment and out of chat, URLs, and generated app interfaces.

Risk: Short ticker-like inputs or broad market questions may trigger data requests.

Mitigation: Confirm ambiguous intent before fetching data and keep requests scoped to the question.

Risk: An optional local app build can expose credentials or introduce dependency risks.

Mitigation: Keep credentials in the main process, review pinned dependencies, and never place keys in renderer configuration.

## Reference(s):

- [Stock Terminal release on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [Commands and data](artifact/references/commands-and-data.md)
- [Local terminal build guide](artifact/references/build-in-an-afternoon.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Configuration guidance]

**Output Format:** [Sourced text or Markdown; optional canvas XML and local app code for explicit build requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market data; delayed prices and dated observations should be labeled.]

## Skill Version(s):

2.0.1 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
