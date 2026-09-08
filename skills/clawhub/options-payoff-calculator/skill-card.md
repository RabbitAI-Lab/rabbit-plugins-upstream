## Description:

Options Payoff Calculator creates a self-contained HTML payoff diagram for common stock and ETF options strategies using delayed SentiSense market data and modeled Black-Scholes premiums.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate educational options payoff diagrams for calls, puts, covered calls, cash-secured puts, vertical spreads, straddles, strangles, and iron condors. It is used to compare modeled breakevens, max profit, max loss, and expected move bands against a delayed market-data snapshot.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manual JSON binding into the HTML template can be unsafe or invalid if untrusted data is inserted without escaping.

Mitigation: Use the bundled command with --out to generate the HTML; if binding manually, use trusted data and escape '<' as a JSON Unicode escape before opening or sharing the file.

Risk: Modeled options premiums can be mistaken for live option-chain quotes or personalized trading advice.

Mitigation: Describe premiums as modeled from end-of-day implied volatility and present the output as educational market context only.

Risk: The skill requires an API key for read-only market data access.

Mitigation: Provide SENTISENSE_API_KEY through the environment and send it only to the documented SentiSense API origin over HTTPS.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/thesentitrader/skills/options-payoff-calculator)
- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [SentiSense API Origin](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Files]

**Output Format:** [Self-contained HTML file with brief text guidance and optional JSON data snapshot.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; generated payoff values are educational market context, not trading advice.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
