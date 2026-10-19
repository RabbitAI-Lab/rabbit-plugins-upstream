## Description:

Provides sourced, read-only stock research views and, when explicitly requested, guidance for building a local financial terminal.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Investors, analysts, and developers use this skill to review dated market data, compare stocks, and explore news, filings, earnings, and options analytics. Developers can also request guidance for building a local chat-and-canvas terminal.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An API key is used to authenticate market-data requests.

Mitigation: Keep the key in the configured environment variable; do not expose it in URLs, responses, or generated files.

Risk: Short ticker-like inputs in a built terminal may trigger market-data requests.

Mitigation: Make this navigation behavior clear to users and keep data access read-only.

Risk: An explicitly requested local build may install dependencies and save thread history.

Mitigation: Review dependencies and local history storage before running or using the built application.

## Reference(s):

- [Stock Terminal on ClawHub](https://clawhub.ai/thesentitrader/skills/stock-terminal)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [Build in an afternoon](references/build-in-an-afternoon.md)
- [Commands and data](references/commands-and-data.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions]

**Output Format:** [Sourced Markdown market summaries; optional code and build guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dates and coverage gaps identified; no trading or account changes.]

## Skill Version(s):

2.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
