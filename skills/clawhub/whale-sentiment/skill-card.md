## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns whale leaderboard sentiment derived from Hyperliquid top traders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and trading agents can retrieve a real-time whale sentiment signal derived from Hyperliquid top traders to inform trade research or use as a confirming input for trade entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each endpoint request incurs a USDC charge, and the listed discounted price may change.

Mitigation: Check the current endpoint price and set a spending limit before allowing repeated or automated requests.

Risk: The skill passes an EVM private key to the payment client to authorize requests.

Mitigation: Use a dedicated wallet with only the funds needed for calls, and keep the private key protected from prompts, logs, and shared environments.

Risk: A whale-sentiment signal could be mistaken for a standalone trading recommendation.

Mitigation: Treat the returned signal as one input to a trading decision and assess whether this use fits your needs.

## Reference(s):

- [Whale Sentiment endpoint](https://apexrunner.ai/signals/whale-sentiment)
- [Liquidation Pressure signal](https://apexrunner.ai/signals/liquidation-pressure)
- [Agent Conviction Score signal](https://apexrunner.ai/signals/agent-conviction-score)

## Skill Output:

**Output Type(s):** [Analysis, JSON data]

**Output Format:** [JSON sentiment data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a sentiment label, score, and top-trader long percentage. Each request is paid in USDC on Base.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
