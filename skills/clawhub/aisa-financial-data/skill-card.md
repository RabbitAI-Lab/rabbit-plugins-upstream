## Description: <br>
Query real-time and historical financial data across equities and crypto - prices, market moves, metrics, and trends for analysis, alerts, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aisapay](https://clawhub.ai/user/aisapay) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External developers and agents use this skill to retrieve equities and cryptocurrency market data from AIsa for portfolio monitoring, investment research, screening, alerts, and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends an AIsa API key and market query details to a third-party financial data API. <br>
Mitigation: Treat AISA_API_KEY as a secret, install only when the AIsa service is trusted, and avoid submitting confidential trading strategies, client identifiers, or private portfolio details unless that sharing is acceptable. <br>
Risk: API calls may consume paid credits or incur usage costs. <br>
Mitigation: Monitor API usage, review returned usage cost and credits remaining, and use constrained ticker lists, filters, and date ranges. <br>


## Reference(s): <br>
- [AIsa Financial Data on ClawHub](https://clawhub.ai/aisapay/skills/aisa-financial-data) <br>
- [AIsa API Reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa signup](https://aisa.one) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with shell commands, Python client examples, and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl or python3 and an AISA_API_KEY environment variable; API responses may include usage cost and remaining credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
