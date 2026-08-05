## Description: <br>
Guides agents in calling the Kronos Crypto Data API for real-time crypto prices, derivatives signals, market alerts, forecasts, candles, volatility, and related market snapshots using free endpoints or paid x402 USDC micropayments. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vizionik25](https://clawhub.ai/user/vizionik25) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and market-analysis agents use this skill to select Kronos Crypto Data API endpoints, understand request costs, and retrieve informational crypto market data. It is intended for data access and analysis workflows, not financial advice or autonomous trading decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Paid endpoint calls can spend real USDC through a wallet-enabled x402 payment flow. <br>
Mitigation: Require explicit user approval before paid calls and configure a hard daily or per-task USDC spend limit. <br>
Risk: Repeated agent loops could accumulate charges across multiple API cycles. <br>
Mitigation: Prefer free health and stats endpoints before paid calls, batch requests where supported, and stop cycles once the configured spend cap is reached. <br>
Risk: Crypto forecasts and market signals could be mistaken for financial advice. <br>
Mitigation: Keep outputs framed as informational market data and preserve the artifact's disclaimer that forecasts are probabilistic and not financial advice. <br>


## Reference(s): <br>
- [Kronos Crypto Data API](https://kronossignals.com) <br>
- [Kronos OpenAPI specification](https://kronossignals.com/api/openapi.json) <br>
- [Kronos API health endpoint](https://kronossignals.com/api/health) <br>
- [Kronos API stats endpoint](https://kronossignals.com/api/stats) <br>
- [ClawHub skill page](https://clawhub.ai/vizionik25/skills/kronos-signals-api) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, API Calls, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with endpoint examples, JSON response shapes, and request command patterns] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include paid API call instructions and should preserve API disclaimers that forecasts and signals are informational only.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact overview) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
