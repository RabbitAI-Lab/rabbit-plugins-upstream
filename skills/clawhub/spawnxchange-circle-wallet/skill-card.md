## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using a Circle Agent Wallet, including searching, buying, delivery, listing, payouts, account settings, feedback, and large-artifact listing through a bundled signing script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate a wallet-based marketplace workflow for buying and selling AI-generated code artifacts with USDC. It provides command guidance for searches, purchases, downloads, listings, payouts, account updates, and feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace payments, listings, username changes, feedback, and deletion commands can have real account or financial effects.

Mitigation: Review wallet setup, spending limits, and each command before execution; use the documented max-amount and fee-cap controls.

Risk: Publishing an archive may expose files the seller did not intend to share.

Mitigation: Package from a separate review copy, exclude secrets and generated dependency folders, and run the documented precheck before listing.

Risk: Large-artifact listing signs payment data returned by the marketplace.

Mitigation: Use the helper script's preflight mode first and keep its host, chain, USDC contract, and fee-cap checks enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-circle-wallet)
- [Project homepage](https://github.com/avlk/spawnxchange-skills)
- [Circle Agent Wallets documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes user-directed wallet, payment, listing, and account-management commands; does not handle private keys directly.]

## Skill Version(s):

0.3.1 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
