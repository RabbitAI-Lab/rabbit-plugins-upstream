## Description:

Crypto market signals for agents, paid per call in USDC on Base via x402 (from $0.001, no account, no API key): funding rates and predictions, liquidation zones, sentiment, stablecoin peg health, DEX-vs-CEX and cross-exchange spreads, ETF flows, memecoin risk checks, recorded history anchored on Base. Every predictive signal has a public track record against a naive baseline. Use when the user asks about crypto market conditions, funding, liquidations, depeg risk or a memecoin's risk, or wants crypto data an agent can pay for itself.

This skill is ready for commercial/non-commercial use.

## Publisher:

[speteai](https://clawhub.ai/user/speteai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents can retrieve current crypto market readings, risk indicators, and recorded signal history, then use the calibration data to judge predictive signals before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid requests can spend USDC from the configured buyer wallet.

Mitigation: Use a dedicated wallet with limited funds, confirm the request and price with the user, and keep per-call and session spending caps in place.

Risk: A buyer wallet key or unsuitable wallet configuration could expose funds or cause payments to fail.

Mitigation: Keep the private key in the process environment and out of chat, use a plain account rather than an EIP-7702 delegated wallet, and fund it only with a small amount of USDC.

## Reference(s):

- [AgentData API documentation](https://agentdata-api.com/llms.txt)
- [Signal calibration and track records](https://agentdata-api.com/calibration)
- [Live API catalogue and prices](https://agentdata-api.com/info)
- [AgentData homepage](https://agentdata-api.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured market signal data with concise agent-facing summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Predictive signals should be interpreted alongside their public calibration and known weaknesses.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
