## Description:

Guides agents through fresh AssetFare quotes for non-custodial cross-chain routes and wallet funding, with execution requiring separate caller approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odaiin](https://clawhub.ai/user/odaiin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compare fresh, fee-inclusive cross-chain quotes and identify a candidate route for bridging or funding a native-USDC payment wallet. The caller separately approves any action and signs and submits with their own wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Quotes and unsigned actions can expose users to financial loss if costs, route details, or changing conditions are overlooked.

Mitigation: Review a fresh quote and independently verify each unsigned action, including fees, outputs, wallet details, and timing, before the caller signs or submits.

Risk: Session or access-token disclosure could expose route-preparation workflows.

Mitigation: Keep session and access tokens private; never provide private keys, seed phrases, signed transactions, or blanket approval for financial actions.

## Reference(s):

- [AssetFare OpenAPI v2](https://api.assetfare.dev/v2/openapi.json)
- [AssetFare route economics](https://assetfare.dev/route-economics.json)
- [AssetFare Route Quote on ClawHub](https://clawhub.ai/odaiin/skills/assetfare-route)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quote-based route guidance; does not sign or submit transactions.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
