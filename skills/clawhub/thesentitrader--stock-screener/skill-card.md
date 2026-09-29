## Description:

Turns plain-language requests into read-only screens of US stocks and ETFs using SentiSense sentiment, analyst, technical, momentum, price, and fund data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents screen US stocks and ETFs for combinations of sentiment, analyst views, technical signals, and fund characteristics, then review the visible filters and matching results for research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Screen requests send queries, optional watchlist tickers and client identification, and the API key to SentiSense.

Mitigation: Review what is sent before use, share only necessary watchlist data, and keep the API key private.

Risk: Research snapshots may be mistaken for live quotes or personalized investment advice.

Mitigation: Show the screen criteria and treat results as informational research, not trading guidance or live prices.

## Reference(s):

- [ClawHub stock-screener release](https://clawhub.ai/thesentitrader/skills/stock-screener)
- [SentiSense](https://sentisense.ai)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown]

**Output Format:** [Markdown with screen results and the executed filter plan]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports matching counts and filters; results are research snapshots, not live quotes or investment advice.]

## Skill Version(s):

1.2.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
