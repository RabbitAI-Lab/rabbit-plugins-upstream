## Description: <br>
Access Finnhub API for real-time stock quotes, company news, market data, financial statements, and trading signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[matthewxfz3](https://clawhub.ai/user/matthewxfz3) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and market-data users use this skill to configure Finnhub access and request quotes, company news, financial statements, earnings data, technical indicators, and SEC filing search results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Finnhub API key for market-data requests. <br>
Mitigation: Use a limited key where possible and avoid exposing the token in logs, shell history, URLs, or shared transcripts. <br>
Risk: Finnhub requests can consume quota or paid-tier usage. <br>
Mitigation: Monitor API usage and rate limits before running repeated quote, news, filings, or technical-indicator requests. <br>


## Reference(s): <br>
- [Finnhub](https://finnhub.io) <br>
- [Finnhub API base URL](https://finnhub.io/api/v1) <br>
- [ClawHub skill page](https://clawhub.ai/matthewxfz3/skills/finnhub) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON configuration examples and bash curl commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires FINNHUB_API_KEY; output depends on Finnhub plan limits, queried symbols, date ranges, and endpoint availability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
