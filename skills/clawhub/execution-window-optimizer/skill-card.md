## Description:

Paid x402 service that returns real-time execution-window recommendations based on market volatility and liquidity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use the signal to assess execution timing based on current volatility and liquidity, including during high-volatility or latency-sensitive periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request incurs a USDC charge, and the documented price includes an early-adopter period.

Mitigation: Check the current endpoint price and wallet transaction details before calling; account for the standard price after the stated discount period.

Risk: The x402 client uses an EVM private key to authorize payment from a Base wallet.

Mitigation: Keep the key in a secret manager and use a dedicated wallet with only the funds needed for intended calls.

Risk: Execution-window ratings are time-sensitive recommendations and do not guarantee an execution outcome.

Mitigation: Check the response timestamp and current market conditions before acting on a recommendation.

## Reference(s):

- [Execution Window Optimizer service](https://apexrunner.ai/signals/execution-window-optimizer)
- [Slippage Forecast signal](https://apexrunner.ai/signals/slippage-forecast)
- [Optimal Order Routing signal](https://apexrunner.ai/signals/optimal-order-routing)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON execution-window rating, recommendation, candidate time windows, and timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One paid response per call; the documented early-adopter price is $0.007 USDC on Base through 2027-01-01, with a stated standard price of $0.01 per call.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
