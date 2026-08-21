## Description:

Read a Hyperliquid account from the desk computer - positions and margin, spot balances, open orders including trigger details, fills, funding paid, ledger updates, order status by oid or cloid, historical orders, portfolio history, fee tier and rate-limit budget - with curl and Python SDK examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT-0

## Use Case:

Traders, reviewers, and agent operators use this skill to query read-only Hyperliquid account state for sizing inputs, book checks, reconciliation, and trading reviews. It helps inspect positions, margin, balances, orders, fills, funding, ledger updates, portfolio history, fees, and rate-limit budget for a supplied account address.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hyperliquid account positions, balances, fills, and approved agent listings can be financially sensitive even when access is read-only.

Mitigation: Install and use the skill only where agents are permitted to query the supplied account address, and avoid sharing outputs outside authorized trading or review workflows.

Risk: Using the wrong wallet or network can produce empty or misleading account reads.

Mitigation: Query the main trading account address, not an API wallet address, and set the Hyperliquid network explicitly before relying on results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-account)
- [Hyperliquid Mainnet API](https://api.hyperliquid.xyz)
- [Hyperliquid Testnet API](https://api.hyperliquid-testnet.xyz)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with inline bash and Python code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Hyperliquid account lookup guidance using a supplied account address and selected network.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
