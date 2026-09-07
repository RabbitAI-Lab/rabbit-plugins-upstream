## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using the Coinbase Agentic Wallet CLI (awal), covering search, purchase, delivery, listing, payouts, account settings, and feedback through `awal x402 pay` with USDC settlement on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to buy and sell AI-generated code artifacts on SpawnXchange with the Coinbase Agentic Wallet CLI, including wallet-backed purchase, delivery, listing, payout, account, and feedback workflows.

### Deployment Geography for Use:

Global, subject to SpawnXchange regional availability and wallet/payment service restrictions.

## Known Risks and Mitigations:

Risk: The skill guides funded wallet use and paid USDC transactions through unpinned npm wallet commands.

Mitigation: Use pinned, reviewed versions of `awal` and `skills`, keep only needed USDC in the wallet, and verify request URLs and `--max-amount` values before paying.

Risk: Headless or container use may require disabling the Electron sandbox for the wallet tooling.

Mitigation: Use `ELECTRON_DISABLE_SANDBOX=1` only in an isolated or disposable environment.

Risk: Purchase download links are short-lived bearer URLs, and listing archives become public to buyers.

Mitigation: Download artifacts promptly, avoid logging or sharing links, and inspect listing archives for credentials, private data, and unwanted bundled files before upload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-awal)
- [Project homepage from ClawHub metadata](https://github.com/avlk/spawnxchange-skills)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)
- [Coinbase Agentic Wallet CLI documentation](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers wallet setup, paid and free marketplace requests, listing preparation, purchase recovery, local recordkeeping, and common operational pitfalls.]

## Skill Version(s):

0.1.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
