## Description:

Creates a self-contained options payoff chart for a selected stock or ETF using SentiSense market data and modeled Black-Scholes premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate educational, offline payoff diagrams for common options strategies on stocks and ETFs. It helps compare breakevens, modeled max profit and loss, and the expected move band without placing trades or making personalized recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Modeled premiums and payoff figures may be mistaken for live tradable quotes, financial advice, or forecasted outcomes.

Mitigation: Present outputs as modeled educational estimates, state that premiums use end-of-day implied volatility and Black-Scholes rather than a live options chain, and avoid personalized buy or sell recommendations.

Risk: The workflow requires a SentiSense API key and build-time market-data requests.

Mitigation: Provide SENTISENSE_API_KEY through the host's secret handling, expect only read-only requests at build time, and use the bundled script path to avoid extra local dependencies.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [text, code, shell commands, configuration, guidance, files]

**Output Format:** [Self-contained HTML file plus concise Markdown guidance and optional JSON data snapshot]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and build-time network access to SentiSense; the rendered HTML artifact works offline.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
