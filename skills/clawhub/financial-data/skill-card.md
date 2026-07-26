## Description: <br>
Query real-time and historical financial data across equities and crypto--prices, market moves, metrics, and trends for analysis, alerts, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and agent builders use this skill to retrieve stock and cryptocurrency prices, financial statements, news, filings, metrics, screen results, and related market data through AIsa-backed API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an AISA API key to query a third-party market-data API, which can expose market-data queries and consume quota or paid credits. <br>
Mitigation: Use a dedicated or limited AISA_API_KEY, monitor quota and cost usage, and avoid submitting sensitive proprietary portfolio or strategy filters. <br>
Risk: Agent-generated financial analysis or alerts based on returned data could be incorrect, stale, or unsuitable for a user's financial decisions. <br>
Mitigation: Review outputs before acting, validate important results against authoritative sources, and avoid treating skill output as financial advice. <br>


## Reference(s): <br>
- [ClawHub Financial Data skill page](https://clawhub.ai/aisapay/skills/financial-data) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl or python3 and an AISA_API_KEY environment variable; API responses may include usage cost and remaining credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
