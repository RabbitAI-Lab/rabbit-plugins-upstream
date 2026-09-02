## Description:

SentiSense provides read-only US stock market data for AI agents, including sentiment, smart-money disclosures, institutional flows, options positioning, analyst ratings, earnings, AI insights, and delayed stock prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and financial research agents use this skill to query SentiSense market data for dashboards, watchlists, screeners, and research summaries without trading, purchase, wallet, or write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can be exposed or stored locally when using optional persistent CLI authentication.

Mitigation: Prefer environment variables or REST header examples; use persistent CLI auth only when local storage is acceptable, and rotate or revoke keys from account settings when needed.

Risk: Optional npx or SDK package execution may introduce supply-chain risk in sensitive agent environments.

Mitigation: Prefer direct REST calls where possible, and review the optional package source before running it in sensitive environments.

Risk: Returned market data or AI summaries may be mistaken for trading advice.

Mitigation: Treat all outputs as informational only and do not present them as investment advice, personalized recommendations, or trade instructions.

Risk: Delayed, preview, quota-gated, or tier-limited data may be incomplete or stale.

Mitigation: Check freshness, preview, and count fields before presenting results; do not label delayed prices as live.

## Reference(s):

- [SentiSense API Documentation](https://sentisense.ai/docs/api/)
- [SentiSense Website](https://sentisense.ai)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/sentisense)
- [SentiSense Python SDK](https://github.com/SentiSenseApp/sentisense)
- [SentiSense Node.js SDK](https://github.com/SentiSenseApp/sentisense-node)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with REST examples, shell commands, SDK snippets, and optional JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; market data is read-only and informational]

## Skill Version(s):

2.12.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
