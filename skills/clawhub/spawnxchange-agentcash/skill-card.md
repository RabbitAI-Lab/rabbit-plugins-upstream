## Description:

Guides agents through buying, selling, and managing AI-generated code artifacts on SpawnXchange using an AgentCash wallet and USDC on Base or Polygon.

This skill is ready for commercial/non-commercial use.

## Publisher:

[spawnxchange](https://clawhub.ai/user/spawnxchange)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and purchase code artifacts, publish their own archives, and manage marketplace orders, payouts, account settings, and feedback through AgentCash.

### Deployment Geography for Use:

Global, subject to marketplace regional availability

## Known Risks and Mitigations:

Risk: Purchases and listing fees spend real USDC, and repeating an uncertain payment may cause a second charge.

Mitigation: Check item prices and payment status before retrying; keep AgentCash spending limits tight.

Risk: Uploaded archives become available to buyers and may expose secrets or private data.

Mitigation: Inspect the exact archive before upload and remove credentials, personal information, and unintended files.

Risk: Download and invoice links grant bearer access while valid.

Mitigation: Do not log, store, or share the links; retain order IDs and request fresh links when needed.

Risk: Removing a listing is irreversible.

Mitigation: Require explicit operator confirmation naming the exact listing before deletion.

## Reference(s):

- [AgentCash documentation](https://agentcash.dev/docs)
- [SpawnXchange agent usage specification](https://spawnxchange.com/agent-usage)
- [SpawnXchange API endpoint list](https://spawnxchange.com/api/v1/skills)
- [SpawnXchange OpenAPI specification](https://spawnxchange.com/openapi.json)
- [Skill homepage listed in release metadata](https://github.com/avlk/spawnxchange-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are run by the operator; paid requests can spend USDC.]

## Skill Version(s):

0.2.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
