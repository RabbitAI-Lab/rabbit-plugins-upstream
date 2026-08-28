## Description:

Generates a self-contained options payoff HTML artifact for a stock or ETF using SentiSense market data, with modeled profit-and-loss-at-expiry diagrams for nine common strategies and offline rendering after build time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch read-only SentiSense market data for a ticker and produce an interactive options payoff diagram for common strategies. The output is educational modeled context, not a live options quote, trading instruction, or personalized investment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key for read-only market data access.

Mitigation: Install and run it only when sharing that key with the local agent workflow is acceptable, and avoid optional CLI credential storage unless local persistence is intended.

Risk: The payoff artifact uses modeled premiums from end-of-day implied volatility rather than live options-chain quotes.

Mitigation: Present outputs as educational modeled data, not trading advice, live quotes, recommendations, or forecasts.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated JSON or self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a SENTISENSE_API_KEY at build time; the generated HTML artifact renders offline after data is bound.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
