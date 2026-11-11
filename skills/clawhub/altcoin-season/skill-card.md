## Description:

This skill calls a paid x402 endpoint on Base for $0.007 USDC per call and returns an altcoin season index measuring capital rotation from Bitcoin to altcoins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and trading agents use the returned index as context when assessing Bitcoin versus altcoin exposure and rotation timing. Treat it as one signal alongside other market information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests authorize a paid USDC call using an EVM wallet private key.

Mitigation: Keep EVM_PRIVATE_KEY in secure secret storage and use a wallet funded only with the amount intended for these calls.

Risk: The index may be used to inform trading decisions, but it is only one market signal.

Mitigation: Corroborate it with other market data and apply independent position and loss limits.

Risk: The security review did not assess the destinations of linked URLs.

Mitigation: Verify the endpoint and related service destinations before sending requests or payment.

## Reference(s):

- [Altcoin Season API](https://apexrunner.ai/signals/altcoin-season)
- [BTC Dominance signal](https://apexrunner.ai/signals/btc-dominance)
- [Capital Rotation signal](https://apexrunner.ai/signals/capital-rotation-signal)
- [Market Regime signal](https://apexrunner.ai/signals/regime)

## Skill Output:

**Output Type(s):** [API Calls, JSON]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A single response provides an index, season label, and threshold; each request is paid in USDC on Base.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
