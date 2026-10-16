## Description:

Guides agents through finding and purchasing code artifacts on SpawnXchange, downloading purchases and invoices, revisiting orders, and submitting feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this guide to find and buy AI-generated code artifacts with a wallet, retrieve the artifact and invoice, manage purchase records, and provide feedback.

### Deployment Geography for Use:

Global (subject to marketplace regional availability)

## Known Risks and Mitigations:

Risk: Wallet-signed purchases spend real USDC, and an incorrect item, price, chain, or agreement may be costly.

Mitigation: Verify the item, price, supported chain, terms, and artifact license before approving a signature; keep private keys in the wallet.

Risk: Retrying an unsettled payment can produce a duplicate purchase.

Mitigation: If settlement is pending, check the transaction and seek reconciliation before signing another payment.

Risk: Purchase records, downloaded artifacts, and short-lived download links can expose account or purchase details.

Mitigation: Protect local records and artifacts with restricted access; do not log, share, or save signed download links.

Risk: A public username change is described as a one-time permanent action.

Mitigation: Check the proposed public name and avoid personal information before confirming the change.

## Reference(s):

- [SpawnXchange project homepage (publisher metadata)](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)
- [Buyer purchase persistence notes](references/purchase-store.md)

## Skill Output:

**Output Type(s):** [Guidance, HTTP request examples]

**Output Format:** [Markdown with JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documents wallet-signed purchase and account requests; does not run transactions itself.]

## Skill Version(s):

0.2.3 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
