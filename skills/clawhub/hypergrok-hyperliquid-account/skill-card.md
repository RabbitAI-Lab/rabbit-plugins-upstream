## Description:

Provides read-only Hyperliquid account checks for positions, balances, orders, fills, funding, and account history using an account address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[galleonlabs](https://clawhub.ai/user/galleonlabs)

### License/Terms of Use:

MIT

## Use Case:

Traders, risk reviewers, and developers use this skill to inspect Hyperliquid account state, check open-order protection and margin, and reconcile trading activity without placing orders.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account queries may expose sensitive positions, balances, orders, fills, funding, and ledger activity.

Mitigation: Share account results only with intended recipients and avoid exposing them in public logs or reports.

Risk: A request for wallet private keys or API secrets exceeds this read-only skill's documented scope.

Mitigation: Provide only the account address for documented reads; do not supply signing credentials.

## Reference(s):

- [HyperGrok Hyperliquid Account on ClawHub](https://clawhub.ai/galleonlabs/skills/hypergrok-hyperliquid-account)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown account summaries with curl and Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only account queries; results may contain sensitive trading and account information.]

## Skill Version(s):

1.5.0 (source: ClawHub release; bundled frontmatter says 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
