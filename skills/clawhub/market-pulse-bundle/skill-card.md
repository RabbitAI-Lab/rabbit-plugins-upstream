## Description:

Paid x402 endpoint: $0.007 USDC per call on Base. Returns price tick + Fear & Greed + regime in one call.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents can request a quick market snapshot containing a price tick, Fear & Greed reading, and market regime in one call. Each request is paid, so activation should match a clear market-data need and be authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation guidance may cause unnecessary paid market-data requests during unrelated agent loops.

Mitigation: Require a clear market-data need and authorization for paid use before activating the skill.

## Reference(s):

- [Market Pulse Bundle endpoint](https://apexrunner.ai/signals/market-pulse-bundle)
- [Trading Intelligence Bundle](https://apexrunner.ai/signals/trading-intelligence-bundle)
- [Regime signal](https://apexrunner.ai/signals/regime)
- [Fear & Greed signal](https://apexrunner.ai/signals/fear-greed)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Market data]

**Output Format:** [JSON market snapshot]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One response bundles a price tick, Fear & Greed reading, and market regime.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
