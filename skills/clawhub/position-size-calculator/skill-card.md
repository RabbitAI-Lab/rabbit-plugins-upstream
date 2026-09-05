## Description:

Position Size Calculator creates a self-contained offline HTML calculator for stocks and ETFs that uses SentiSense market data to show share count, position value, account deployment, dollar risk, and optional R multiple from user-supplied account, risk, entry, stop, and target inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to generate an offline position-size calculator for a single stock or ETF. The skill is for arithmetic on user-supplied risk inputs and market-data context, not for selecting trades or giving investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake position-size arithmetic or displayed market context for trading advice.

Mitigation: Present outputs as calculations from the user's own inputs, state that the skill does not choose securities or trade parameters, and keep investment-advice disclaimers visible.

Risk: A stop price may not be honored in real markets, so actual losses can exceed the calculator's planned risk.

Mitigation: Call out gap, fast-market, slippage, commission, financing, and tax limits when summarizing the generated calculator.

Risk: The skill uses a SentiSense API key and can be pointed at an alternate base URL.

Mitigation: Keep the API key scoped to SentiSense and set SENTISENSE_BASE_URL only for endpoints the installer intentionally trusts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and a generated self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY at build time; the generated HTML calculator is offline at view time.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
