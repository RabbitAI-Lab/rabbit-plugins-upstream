## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns current Hyperliquid perpetual funding rates across tracked coins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Traders and agents use this skill to retrieve current Hyperliquid perpetual funding rates before opening or holding positions, to evaluate funding arbitrage, or to avoid unusually high funding costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Each request authorizes a paid call using an EVM wallet private key, so repeated calls can incur charges and exposed credentials could put wallet funds at risk.

Mitigation: Keep EVM_PRIVATE_KEY in a secret store, use a wallet funded only for intended requests, and monitor request frequency and spending.

## Reference(s):

- [Funding Rate HL endpoint](https://apexrunner.ai/signals/funding-rate-hl)
- [Related funding-rate signal](https://apexrunner.ai/signals/funding-rate)
- [Related arbitrage-spread signal](https://apexrunner.ai/signals/arb-spread)
- [ClawHub skill release](https://clawhub.ai/kynto2001-ctrl/skills/funding-rate-hl)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Market data]

**Output Format:** [JSON object containing funding rates and a timestamp]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Current values vary by asset and time.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
