## Description:

Gives AI agents bounded CryptoSLIP pocket funds on Base for merchant payments, human payouts, receipt checks, recovery of unclaimed funds, and referral withdrawals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[naraprotocol](https://clawhub.ai/user/naraprotocol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this MCP skill to let AI agents make bounded crypto payments on Base, distribute payouts, and verify receipts using a provisioned CryptoSLIP pocket-funds URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is incomplete, and ClawScan flagged a possible spending-limit bypass and unpinned install commands that could run a changed package.

Mitigation: Follow the server guidance: defer installation until the payout-limit concern is reviewed and launch instructions specify a reviewed package version.

## Reference(s):

- [Server-resolved source (NARAProtocol/cryptoslip-sdk, packages/mcp)](https://github.com/NARAProtocol/cryptoslip-sdk/tree/main/packages/mcp)
- [CryptoSLIP PocketSlip release on ClawHub](https://clawhub.ai/naraprotocol/skills/mcp)
- [CryptoSLIP](https://slip.naraprotocol.io)

## Skill Output:

**Output Type(s):** [JSON, CSV, HTML, Text]

**Output Format:** [Structured payment results and receipts in JSON or CSV, printable HTML receipts, and human payout links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Payment and receipt results depend on the configured pocket funds and spending policy.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
