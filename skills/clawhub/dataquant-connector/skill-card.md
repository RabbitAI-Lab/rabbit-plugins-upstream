## Description:

Dataquant Connector connects agents to the DataQuant quantitative data platform for REST API access to market data, K-line/OHLCV series, valuation snapshots, screening, macro data, and quota queries across A-shares, Hong Kong stocks, U.S. stocks, crypto, indices, and ETFs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-ip](https://clawhub.ai/user/ai-ip)

### License/Terms of Use:

MIT

## Use Case:

Developers, AI-assisted quantitative researchers, and individual traders use this skill to retrieve structured market data and support backtesting, screening, and macro-data workflows through the DataQuant REST API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credential exposure from pasting a DataQuant API key into chat or shell history.

Mitigation: Prefer DATAQUANT_API_KEY through a local environment variable or secure secret manager, and avoid sharing real API keys in chat.

Risk: The skill can query market data using the user's DataQuant account.

Mitigation: Install only when that account access is acceptable for the intended market-data workflow.

## Reference(s):

- [DataQuant Connector API Reference](references/api-reference.md)
- [DataQuant API Docs](https://app.dataquant.trade/api-docs)
- [DataQuant Platform](https://app.dataquant.trade/)
- [Server-resolved GitHub source](https://github.com/ai-ip/dataquant-connector)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Code, Markdown, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses from the bundled CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a DataQuant API key; the CLI reads DATAQUANT_API_KEY or an explicit --api-key value and writes JSON to stdout.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
