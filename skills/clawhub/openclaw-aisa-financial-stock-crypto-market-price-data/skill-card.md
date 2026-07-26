## Description: <br>
Query real-time and historical financial data across equities and crypto, including prices, market moves, metrics, news, filings, and trends for analysis, alerts, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to retrieve stock and cryptocurrency market data, company financials, news, filings, analyst estimates, insider trades, and screening results from AIsa for analysis, alerts, and reporting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Market-data queries and symbol lists are sent to AIsa and may be logged by the provider or consume paid credits. <br>
Mitigation: Use a limited or dedicated AISA_API_KEY, review queries before execution, and monitor provider usage and remaining credits. <br>
Risk: Returned stock and crypto data may be time-sensitive or unsuitable as the sole basis for investment decisions. <br>
Mitigation: Verify important results against authoritative sources and apply human review before trading, reporting, or alerting decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-financial-stock-crypto-market-price-data) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown documentation, curl and Python command examples, and JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires AISA_API_KEY and sends requested tickers, dates, filters, and symbol lists to AIsa.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
