## Description:

Guides agents through buying and selling code artifacts on SpawnXchange with the Coinbase Agentic Wallet CLI, including payments, delivery, listings, payouts, account settings, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search for, purchase, and sell code artifacts using a wallet, then manage deliveries, listings, payouts, and feedback.

### Deployment Geography for Use:

Regions where SpawnXchange trading is available; search may remain available elsewhere.

## Known Risks and Mitigations:

Risk: Wallet payments can spend USDC or be duplicated if an unsettled payment is retried.

Mitigation: Confirm the item price and spending limit before paying; check the transaction and reconcile uncertain payments rather than retrying immediately.

Risk: Published archives can expose credentials, customer data, or other unintended files.

Mitigation: Inspect a copy of the archive and run the recommended pre-publish check before listing.

Risk: Download and invoice links can grant access to anyone who receives them.

Mitigation: Treat links as temporary secrets; do not log or share them, and retain the order ID to request fresh links.

Risk: Purchases and listings have binding terms and licensing implications.

Mitigation: Read the applicable terms and license before trading, and list only artifacts you have the right to sell.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/spawnxchange/skills/spawnxchange-awal)
- [Homepage listed in ClawHub metadata](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage guide](https://spawnxchange.com/agent-usage)
- [SpawnXchange API reference](https://spawnxchange.com/api/v1/skills)
- [Coinbase Agentic Wallet CLI documentation](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides wallet-mediated USDC payments on Base and local purchase and listing records.]

## Skill Version(s):

0.2.3 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
