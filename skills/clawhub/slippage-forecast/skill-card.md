## Description:

Provides a paid x402 endpoint that forecasts expected slippage for an order size and market condition; each call costs $0.007 USDC on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers placing cryptocurrency orders can request an expected-slippage forecast to estimate execution costs and compare venues before trading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Forecast requests incur a USDC charge, so repeated calls can add up.

Mitigation: Set a request budget and confirm the current per-call price before use.

Risk: The x402 client uses EVM_PRIVATE_KEY to authorize wallet payments.

Mitigation: Store the key in a secret manager and use a dedicated wallet funded only for intended spending.

## Reference(s):

- [Slippage forecast endpoint](https://apexrunner.ai/signals/slippage-forecast)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/slippage-forecast)
- [Related signal: optimal order routing](https://apexrunner.ai/signals/optimal-order-routing)
- [Related signal: execution window optimizer](https://apexrunner.ai/signals/execution-window-optimizer)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON slippage forecast with timestamp; Markdown instructions with a Python example]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Each request costs $0.007 USDC on Base through 2027-01-01; the documented standard price is $0.01 per call. Requires EVM_PRIVATE_KEY and a Base wallet funded with USDC.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
