## Description:

A paid x402 endpoint that returns signals about capital rotation among BTC, ETH, altcoins, and stablecoins.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kynto2001-ctrl](https://clawhub.ai/user/kynto2001-ctrl)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to query a paid signal endpoint for indications of capital rotation among BTC, ETH, altcoins, and stablecoins, including a suggested direction and allocation example.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Four external links were outside the scanner's assessment, so their destinations were not assessed.

Mitigation: Review the linked destinations before installing or using the skill.

Risk: The example uses an EVM wallet private key to authorize paid calls, and the endpoint charges $0.007 USDC per call on Base according to the artifact.

Mitigation: Keep EVM_PRIVATE_KEY in a secure secret store and use a wallet funded only for intended calls; check the current price before making requests.

## Reference(s):

- [Capital Rotation Signal endpoint](https://apexrunner.ai/signals/capital-rotation-signal)
- [BTC Dominance signal](https://apexrunner.ai/signals/btc-dominance)
- [Altcoin Season signal](https://apexrunner.ai/signals/altcoin-season)
- [Regime Transition signal](https://apexrunner.ai/signals/regime-transition)
- [ClawHub release page](https://clawhub.ai/kynto2001-ctrl/skills/capital-rotation-signal)
- [Publisher profile](https://clawhub.ai/user/kynto2001-ctrl)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [Markdown instructions with a Python example; endpoint responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid x402 call: $0.007 USDC per call on Base until 2027-01-01, according to the artifact. Requires an EVM wallet private key in EVM_PRIVATE_KEY.]

## Skill Version(s):

1.0.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
