## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns real-time BTC price tick from live exchange feeds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this endpoint to retrieve low-latency BTC price ticks for polling, spread checks, and momentum calculations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The endpoint charges USDC for each request, so frequent polling can increase wallet spend.

Mitigation: Set a request rate that fits your budget, use a wallet funded only for the intended spend, and monitor transactions.

Risk: Requests use an EVM private key, which could expose wallet funds if it is disclosed.

Mitigation: Store the key in a secret manager or protected environment variable and keep it out of prompts, source code, and logs.

## Reference(s):

- [BTC price tick endpoint](https://apexrunner.ai/signals/btc-price-tick)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/btc-price-tick)
- [Related market tick signal](https://apexrunner.ai/signals/market-tick)
- [Related apex pulse signal](https://apexrunner.ai/signals/apex-pulse)
- [Related BTC dominance signal](https://apexrunner.ai/signals/btc-dominance)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON BTC price tick response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A paid x402 request returns a real-time BTC price tick and associated market fields.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
