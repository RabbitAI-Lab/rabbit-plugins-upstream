## Description:

Helps agents compare non-custodial cross-chain routes and payment-wallet funding quotes, with unsigned action plans only after caller approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odaiin](https://clawhub.ai/user/odaiin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compare fresh AssetFare bridge or native-USDC wallet-funding quotes against other routes and, with explicit caller approval, prepare unsigned actions for independent wallet review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A stale or misleading quote could result in an unfavorable route or incorrect transaction.

Mitigation: Compare fresh fee-inclusive quotes and independently verify the chain, asset, amount, total fees, minimum output, address, deadline, and payload before wallet signing.

Risk: Unsigned cross-chain actions can involve non-atomic steps or exposure of wallet credentials.

Mitigation: Require explicit caller approval for each plan, verify live receipts before continuing, sign and submit only in the caller's own wallet, and never share private keys or seed phrases.

## Reference(s):

- [AssetFare Route Quote on ClawHub](https://clawhub.ai/odaiin/skills/assetfare-route)
- [AssetFare REST/OpenAPI v2](https://api.assetfare.dev/v2/openapi.json)
- [AssetFare MCP endpoint](https://api.assetfare.dev/mcp)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Unsigned action plans]

**Output Format:** [Text guidance and structured route quotes or unsigned action plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quotes remain unranked candidates until separately selected; the skill does not check balances, sign, or submit transactions.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
