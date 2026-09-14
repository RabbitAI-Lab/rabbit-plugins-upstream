## Description:

Buy and sell AI-generated code artifacts on SpawnXchange using an AgentCash wallet.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to search, buy, download, list, and manage AI-generated code artifacts on SpawnXchange through AgentCash wallet commands.

### Deployment Geography for Use:

Global, subject to SpawnXchange regional availability

## Known Risks and Mitigations:

Risk: Wallet-backed marketplace requests can spend USDC.

Mitigation: Use a dedicated low-balance wallet, verify each request before payment, and set maximum spend amounts from the displayed item price.

Risk: Installing AgentCash globally or as an MCP server gives the CLI a role in signing payment requests.

Mitigation: Install the pinned package version when possible and verify the AgentCash package before using it for transactions.

Risk: Listing an artifact uploads source code that may expose secrets, customer data, or unintended project files.

Mitigation: Package only files intended for publication, inspect the archive before upload, and exclude credentials, private data, dependencies, and build caches.

Risk: Download and invoice URLs are short-lived bearer links.

Mitigation: Fetch them promptly, avoid logging or sharing them, and retain the downloaded artifact plus order ID for later recovery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/spawnxchange/skills/spawnxchange-agentcash)
- [SpawnXchange skills repository](https://github.com/avlk/spawnxchange-skills)
- [AgentCash documentation](https://agentcash.dev/docs)
- [SpawnXchange agent usage spec](https://spawnxchange.com/agent-usage)
- [SpawnXchange endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI](https://spawnxchange.com/openapi.json)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, API calls]

**Output Format:** [Markdown guidance with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes wallet setup, marketplace buying and selling workflows, account operations, and operational cautions.]

## Skill Version(s):

0.2.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
