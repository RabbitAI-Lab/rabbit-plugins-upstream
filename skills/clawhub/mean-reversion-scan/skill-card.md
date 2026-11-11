## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns mean-reversion opportunity scan across RANGING and CHOPPY regimes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this paid APEX Runner signal to review potential oversold or overbought opportunities before mean-reversion entries in RANGING or CHOPPY market regimes. It returns market-signal data and does not itself place trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The x402 endpoint charges for each request, and repeated calls can accumulate USDC charges.

Mitigation: Confirm the current price and Base network before use, and set a spending limit for repeated calls.

Risk: The skill uses EVM_PRIVATE_KEY to authorize paid requests, so mishandling the key could expose wallet funds.

Mitigation: Keep the key in a protected secret store and use a wallet with only the funds needed for expected calls.

Risk: A market signal can be misleading and does not guarantee a profitable trade.

Mitigation: Review the signal against current market conditions and independent risk controls; use it only for the documented RANGING and CHOPPY regimes.

## Reference(s):

- [Mean Reversion Scan endpoint](https://apexrunner.ai/signals/mean-reversion-scan)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/mean-reversion-scan)
- [APEX Runner](https://apexrunner.ai)
- [Related signal: bb-analysis](https://apexrunner.ai/signals/bb-analysis)
- [Related signal: regime](https://apexrunner.ai/signals/regime)
- [Related signal: liquidation-magnet](https://apexrunner.ai/signals/liquidation-magnet)

## Skill Output:

**Output Type(s):** [Analysis, API Calls, JSON]

**Output Format:** [JSON opportunity-scan response]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Market-signal data for RANGING and CHOPPY regimes. Each call costs $0.007 USDC on Base through 2027-01-01 under the stated early-adopter discount; the skill lists $0.01 per call as the standard price.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
