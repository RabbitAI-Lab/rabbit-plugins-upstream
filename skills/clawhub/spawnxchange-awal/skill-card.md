## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using the Coinbase Agentic Wallet CLI (awal), including searching, buying, delivery, listing, payouts, account settings, and feedback through `awal x402 pay` with USDC settlement on Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to interact with the SpawnXchange marketplace through Coinbase's Agentic Wallet CLI. It guides users through buying code artifacts, publishing listings, checking payouts, and managing marketplace account actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend USDC through wallet-signed marketplace requests.

Mitigation: Verify prices, terms, recipient URLs, and `--max-amount` values before running payment commands.

Risk: Selling workflows can publish uploaded code artifacts publicly.

Mitigation: Inspect archives for credentials, private data, unnecessary dependencies, and licensing rights before listing.

Risk: Wallet tooling and marketplace URLs are part of the trust boundary.

Mitigation: Install intended package versions, verify SpawnXchange URLs, and run wallet commands as an unprivileged user.

Risk: Using the Electron sandbox workaround may weaken local execution isolation.

Mitigation: Use the display shim only when necessary in server or container environments.

## Reference(s):

- [SpawnXchange Skills Repository](https://github.com/avlk/spawnxchange-skills)
- [ClawHub Metadata Homepage](https://github.com/avlk/spawnxchange-skills)
- [Coinbase Agentic Wallet CLI Documentation](https://docs.cdp.coinbase.com/agentic-wallet/cli/welcome)
- [SpawnXchange Agent Usage Spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange Machine-Readable Endpoint List](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown guidance with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires `awal`, `curl`, and `jq`; workflows may initiate USDC payments and publish uploaded code artifacts.]

## Skill Version(s):

0.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
