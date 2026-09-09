## Description:

Answer stock-terminal commands and market research questions with compact, sourced views of price, sentiment, SentiSense Score, news, filings, analyst ratings, earnings, and end-of-day options analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and market-research agents use this skill to answer stock and market questions with sourced, read-only SentiSense data. For explicit build requests, developers use the bundled references, contracts, fixtures, and runtime modules to create a local chat-and-canvas financial terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market-data calls.

Mitigation: Install only when the user is comfortable granting that credential, and never print the key or place it in URLs, artifacts, or renderer code.

Risk: Ticker-like shorthand or broad market questions may trigger API calls and consume quota.

Mitigation: Use explicit wording when a data fetch is not intended, and stop fan-out when authentication or rate-limit errors occur.

Risk: Market data may be delayed, preview-limited, missing, or outside coverage.

Mitigation: Display source dates and preview labels, distinguish missing data from zero values, and avoid turning returned observations into investment recommendations.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [Build a local chat-and-canvas terminal](references/build-in-an-afternoon.md)
- [Commands and data recipes](references/commands-and-data.md)
- [Canvas grammar and validation](references/canvas-grammar.md)
- [App shell and trust boundary](references/app-shell.md)
- [Runtime and stream contract](references/runtime-and-stream.md)
- [Verification and the fresh-builder exercise](references/verification.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown market-research answers with optional code, shell commands, JSON contracts, XML canvas examples, and JavaScript runtime modules for explicit app-building requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only market-data workflow using SENTISENSE_API_KEY; app or artifact creation only when explicitly requested]

## Skill Version(s):

2.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
