## Description:

Expected Move Visualizer helps agents fetch read-only SentiSense market data and produce a self-contained offline HTML chart showing modeled 30, 60, and 90 day expected-move cones for stocks and ETFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create an informational expected-move chart for a stock or ETF from SentiSense options, quote, chart, and earnings data. The result supports market research by visualizing modeled implied-volatility ranges, IV rank context, and earnings timing without making trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send the SentiSense API key to an environment-selected server.

Mitigation: Remove or strictly validate SENTISENSE_BASE_URL before execution, and send credentials only to the expected SentiSense endpoint.

Risk: Generated HTML can execute injected script content if untrusted JSON is embedded verbatim in script elements.

Mitigation: Safely serialize and escape bound JSON for script-element embedding, then review generated HTML before sharing or opening it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/expected-move-visualizer)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense API base](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated HTML file instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a self-contained offline HTML chart from a bound market-data snapshot; requires SENTISENSE_API_KEY at build time.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
