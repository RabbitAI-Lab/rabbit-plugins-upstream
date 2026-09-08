## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet, including searching, purchasing, delivery, listing, payouts, account settings, and feedback across Base and Polygon mainnet and testnet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to transact on SpawnXchange with a Circle Agent Wallet: finding, buying, downloading, listing, managing, and receiving payouts for AI-generated code artifacts.

### Deployment Geography for Use:

Regions where SpawnXchange and Circle Agent Wallet services are available

## Known Risks and Mitigations:

Risk: The skill can be used with real funds and includes a financial signing path with an automatic npm fallback.

Mitigation: Install and verify the pinned Circle CLI yourself, ensure the reviewed `circle` binary is on PATH, avoid the script's `npx` fallback, use testnet first, and keep `--max-amount` and fee caps low.

Risk: Listed archives become public to buyers and may expose unintended files or sensitive data.

Mitigation: Inspect archives before listing, remove secrets, customer data, dependency trees, build caches, nested archives, and files you do not have the right to sell.

Risk: Retrying after an uncertain settlement can create a separate payment.

Mitigation: Do not resend payment after `409 payment_settlement_pending`; reconcile the transaction and order state before taking another paid action.

Risk: Purchase and invoice links are short-lived bearer URLs.

Mitigation: Download artifacts and invoices immediately, avoid logging or sharing the URLs, and retain the order ID for fresh links.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-circle-wallet)
- [Project homepage](https://github.com/avlk/spawnxchange-skills)
- [Hermes raw skill source](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange-circle-wallet/SKILL.md)
- [Circle Agent Wallets documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and script usage]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational instructions for marketplace and wallet actions; some actions may initiate USDC payments when executed by the user.]

## Skill Version(s):

0.2.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
