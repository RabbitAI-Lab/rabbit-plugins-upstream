## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet, covering search, purchase, delivery, listing, payouts, account settings, and feedback through AgentCash requests that settle USDC on Base or Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to buy and sell code artifacts through SpawnXchange with an AgentCash wallet. It guides marketplace search, paid acquisition, artifact delivery, listing creation, payout checks, account settings, and feedback workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses AgentCash for financial operations through a mutable npm package reference.

Mitigation: Use a pinned and verified AgentCash package version before funding or spending from the wallet.

Risk: User-scoped MCP registration backed by `@latest` can change behavior outside a single session.

Mitigation: Prefer a pinned package version and review the MCP configuration before enabling user-scoped access.

Risk: Marketplace actions can spend USDC on Base or Polygon.

Mitigation: Keep limited funds in the wallet and confirm the item price, maximum spend, and payment network before each paid request.

Risk: Uploaded sale archives may expose secrets, private data, dependencies, or unintended files.

Mitigation: Inspect archives before uploading and remove credentials, customer data, vendored dependency trees, build caches, and other private content.

## Reference(s):

- [SpawnXchange AgentCash on ClawHub](https://clawhub.ai/spawnxchange/skills/spawnxchange-agentcash)
- [SpawnXchange skills homepage](https://github.com/avlk/spawnxchange-skills)
- [AgentCash documentation](https://agentcash.dev/docs)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange machine-readable endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI document](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with bash commands, JSON examples, and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance includes payment limits, network selection, short-lived download links, listing checks, and local ledger practices.]

## Skill Version(s):

0.1.0 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
