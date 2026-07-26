## Description: <br>
Query real-time and historical financial data across equities and crypto, including prices, market moves, metrics, and trends for analysis, alerts, and reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xjordansg-yolo](https://clawhub.ai/user/0xjordansg-yolo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and autonomous agents use this skill to retrieve stock and cryptocurrency market data from AIsa for portfolio analysis, screening, reporting, and market monitoring. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends tickers, screening filters, portfolio symbols, and market-research parameters to the AIsa API. <br>
Mitigation: Avoid sending confidential portfolio details or trading strategies unless sharing that data with AIsa is acceptable. <br>
Risk: The skill requires an AISA_API_KEY and uses pay-as-you-go API calls. <br>
Mitigation: Use a dedicated API key where possible and monitor credit usage in the returned usage fields. <br>
Risk: Real-time and historical market data can be incomplete, stale, or unsuitable for automated trading decisions. <br>
Mitigation: Review outputs before acting on them and validate important financial decisions against authoritative sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xjordansg-yolo/skills/openclaw-aisa-finance-stock-equity-crypto-market-price-data-yahoo-finance-coinhacko) <br>
- [AIsa API reference](https://aisa.mintlify.app/api-reference/introduction) <br>
- [OpenClaw homepage](https://openclaw.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown documentation with curl and Python command examples; the bundled Python client prints JSON API responses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3, curl, and an AISA_API_KEY environment variable; API responses may include usage cost and credits remaining.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
