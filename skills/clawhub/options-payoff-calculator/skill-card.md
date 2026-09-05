## Description:

Options Payoff Calculator generates a self-contained offline HTML payoff diagram for common stock and ETF options strategies using SentiSense market data and modeled Black-Scholes premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch read-only SentiSense market data for a ticker and produce an interactive options payoff chart for common strategies. It helps compare modeled breakevens, max profit, max loss, and expected move context without placing trades or making recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends SENTISENSE_API_KEY to SentiSense to fetch market data.

Mitigation: Use a read-only SentiSense API key, supply it through the host secret mechanism, and avoid optional local CLI auth unless local credential storage is acceptable.

Risk: The generated payoff chart can be mistaken for live quotes or trading advice.

Mitigation: Present premiums as modeled from end-of-day implied volatility and state that the output is educational context, not a recommendation or order instruction.

Risk: The skill writes a local HTML chart file.

Mitigation: Review the output path before running with --out and treat the generated file as a local artifact for inspection or sharing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [Self-contained HTML file plus concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY at build time; rendered output is offline and uses modeled premiums rather than live option-chain quotes.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
