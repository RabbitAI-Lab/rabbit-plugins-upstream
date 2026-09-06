## Description:

Options payoff calculator for stocks and ETFs that generates a self-contained, offline profit-and-loss-at-expiry diagram for common options strategies using delayed SentiSense market data and modeled Black-Scholes premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to create an options payoff diagram for a stock or ETF, including breakevens, modeled max profit and loss, and the expected move band. The output is educational market context, not investment advice or a trade recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The SentiSense API key may be sent to an endpoint controlled through SENTISENSE_BASE_URL if that variable is set.

Mitigation: Use the default SentiSense endpoint unless you intentionally trust the alternate endpoint, and review the credential path before installation.

Risk: The optional npx/auth flow stores credentials through an external CLI package.

Mitigation: Prefer the bundled zero-dependency script, or use the optional CLI flow only after reviewing its credential storage behavior.

Risk: Modeled premiums can be mistaken for live executable options quotes.

Mitigation: Present outputs as modeled, delayed, informational market context and avoid using them as trading recommendations or order prices.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [SentiSense app](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Self-contained HTML file, optional JSON payload, and concise Markdown summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The finished HTML artifact renders offline after build-time read-only API calls; premiums are modeled from delayed end-of-day implied volatility and are informational only.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
