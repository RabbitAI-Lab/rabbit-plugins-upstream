## Description:

Guides agents through fresh, fee-aware quotes for supported non-custodial cross-chain routes and agent-wallet funding without signing or submitting transactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odaiin](https://clawhub.ai/user/odaiin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compare supported bridge routes or fund an agent payment wallet from a known source asset, then review a fresh quote before separately approving any unsigned action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stale quotes or incomplete fee comparisons can mislead route selection.

Mitigation: Confirm a fresh quote, check its full fees and minimum output, and verify route details before acting.

Risk: Cross-chain actions are sequential and non-atomic, so a later step may fail after a prior step succeeds.

Mitigation: Require explicit caller approval, verify each unsigned action, and advance only after confirmed receipts and actual output.

Risk: Route details and public wallet addresses are shared with AssetFare; exposing credentials or session tokens can compromise wallet security.

Mitigation: Share only necessary public details; never provide private keys, seed phrases, signed transactions, or raw session tokens in chat or logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/odaiin/skills/assetfare-route)
- [AssetFare REST/OpenAPI v2](https://api.assetfare.dev/v2/openapi.json)
- [AssetFare route economics](https://assetfare.dev/route-economics.json)
- [AssetFare MCP endpoint](https://api.assetfare.dev/mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with quote details and verification steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quote-based recommendations only; unsigned action preparation requires separate caller approval.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
