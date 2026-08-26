## Description:

Fetches live cryptocurrency prices, market data, historical trends, and comparative analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrey198224](https://clawhub.ai/user/andrey198224)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to fetch public cryptocurrency prices, market overviews, historical price trends, and side-by-side coin comparisons from CoinGecko. It is suited for market briefings, portfolio tracking support, and structured crypto-data lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on live CoinGecko network calls, so rate limits, API availability, or response changes can affect results.

Mitigation: Batch requests where possible, handle JSON error responses, and retry later when rate limited.

Risk: The dependency policy allows newer requests releases, which can introduce behavior changes or leave vulnerability review to install time.

Mitigation: Review dependencies before installation and pin or constrain requests to a currently patched version in managed environments.

Risk: Coin IDs, currency choices, and market-query parameters are sent to CoinGecko.

Mitigation: Use only the public coin and currency identifiers needed for the lookup, and avoid including sensitive user or portfolio context in command arguments.

## Reference(s):

- [Crypto Market Skill - API Reference](references/REFERENCE.md)
- [Example Workflows](references/EXAMPLES.md)
- [CoinGecko API Documentation](https://www.coingecko.com/en/api/documentation)
- [Crypto Market Skill Page](https://clawhub.ai/andrey198224/skills/crypto-market-data)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Shell commands, Guidance]

**Output Format:** [JSON to stdout, with Markdown usage guidance in the skill documentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs current price data, market overview data, historical price and volume arrays, trend summaries, or comparison summaries depending on the selected script.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
