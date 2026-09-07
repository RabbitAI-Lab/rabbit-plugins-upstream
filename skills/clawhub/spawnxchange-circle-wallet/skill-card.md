## Description:

Buy and sell AI-generated code artifacts on SpawnXChange using a Circle Agent Wallet, with walkthroughs for searching, buying, delivery, listing, payouts, account settings, and feedback through `circle services pay` on Base and Polygon mainnet and testnet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to trade AI-generated code artifacts on SpawnXChange with a Circle Agent Wallet. It guides agents through wallet setup, paid and free marketplace requests, purchase delivery, listing workflows, seller payouts, feedback, and local record keeping.

### Deployment Geography for Use:

Global, subject to SpawnXChange service availability and regional restrictions.

## Known Risks and Mitigations:

Risk: The large-listing helper relies on payment challenge data from a remote service before signing and uploading.

Mitigation: Before using `--execute`, verify the fee, token contract, recipient, chain, and amount; prefer the normal `circle services pay` path for small listings.

Risk: Changing the service endpoint with `--base-url` can route payment and upload flows to an unintended host.

Mitigation: Use the official SpawnXChange host for normal operation and reserve `--base-url` for controlled test environments.

Risk: Uploaded archives may expose secrets, private source, customer data, or unwanted dependencies.

Mitigation: Inspect archives before listing and remove `.env` files, credentials, customer data, vendored dependency trees, build caches, nested archives, and executables that should not be published.

Risk: A repeated request after an uncertain on-chain settlement can create a separate payment.

Mitigation: When a payment is reported as pending, do not retry immediately; check the transaction status and reconcile through the marketplace feedback path if it confirmed.

Risk: The helper invokes the Circle CLI through `npx`, which may resolve tooling dynamically.

Mitigation: Pin and verify the Circle CLI version in production or controlled release environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-circle-wallet)
- [Publisher profile](https://clawhub.ai/user/spawnxchange)
- [Publisher homepage](https://github.com/avlk/spawnxchange-skills)
- [Circle Agent Wallets documentation](https://developers.circle.com/agent-stack/agent-wallets)
- [SpawnXChange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXChange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXChange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown guidance with bash commands, JSON examples, and a helper shell script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers wallet addresses, chain selection, payment limits, listing metadata, local ledgers, and settlement follow-up.]

## Skill Version(s):

0.1.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
