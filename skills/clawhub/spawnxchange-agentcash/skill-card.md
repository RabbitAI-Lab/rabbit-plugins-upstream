## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet, with walkthroughs for search, purchase, delivery, listing, payouts, account settings, and feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to guide wallet-mediated SpawnXchange marketplace workflows: finding artifacts, buying and downloading them, listing artifacts for sale, checking payouts, managing account settings, and submitting feedback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-mediated SpawnXchange operations can spend real USDC on Base or Polygon.

Mitigation: Use a minimally funded wallet, verify the item price and chain before each paid command, and set --max-amount from the observed price.

Risk: Downloaded artifacts, invoice links, and listing archives can expose private data if handled carelessly.

Mitigation: Save purchased artifacts and order IDs instead of short-lived download links, and inspect archives before listing to remove secrets, credentials, customer data, dependency trees, and build caches.

Risk: A pending on-chain settlement can lead to duplicate payment if the same request is retried immediately.

Mitigation: When payment_settlement_pending occurs, check the transaction on the relevant block explorer and reconcile confirmed payments through platform feedback instead of sending a second payment.

Risk: Installing AgentCash and registering its MCP server makes wallet payment tooling available to agent sessions.

Mitigation: Install only trusted AgentCash versions, review upstream release notes before changing the pinned version, and remove the user-scoped MCP registration when the tool should no longer be available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-agentcash)
- [Publisher profile](https://clawhub.ai/user/spawnxchange)
- [SpawnXchange skills repository](https://github.com/avlk/spawnxchange-skills)
- [Source SKILL.md](https://raw.githubusercontent.com/avlk/spawnxchange-skills/main/skills/spawnxchange-agentcash/SKILL.md)
- [AgentCash documentation](https://agentcash.dev/docs)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON request/response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides agent use of AgentCash, curl, jq, and SpawnXchange HTTP endpoints; does not itself execute payments.]

## Skill Version(s):

0.2.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
