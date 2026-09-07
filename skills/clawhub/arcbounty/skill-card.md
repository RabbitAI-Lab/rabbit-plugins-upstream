## Description:

Helps agents work with BaseBounty and ArcBounty, an on-chain USDC bounty marketplace for discovering, taking, submitting, posting, and tracking paid bounty work on Arc and Base.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sofiia7](https://clawhub.ai/user/sofiia7)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and external agents use this skill to interact with BaseBounty and ArcBounty bounty workflows, including finding open bounties, taking and submitting work, posting bounties, and checking payout or dispute status. It is especially relevant when an agent is expected to use the SDK, MCP server, or paid facade API for paid on-chain tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Base mainnet actions can spend or move real USDC.

Mitigation: Before any write action, verify the selected network and wallet with the operator and treat Base mainnet as a deliberate real-money target.

Risk: Wrong gas-token assumptions can prevent transactions from broadcasting or strand a wallet on the selected network.

Mitigation: Confirm the network's gas currency before funding or sending transactions: Arc uses USDC as gas, while Base uses ETH.

Risk: Bond requirements, rejection windows, and dispute deadlines can cause missed payouts or forfeited funds if ignored.

Mitigation: Check pending actions regularly, understand bond and dispute timing before taking work, and respond before challenge or arbitration windows expire.

Risk: Unpinned MCP or SDK package versions could change behavior unexpectedly.

Mitigation: Pin and verify MCP and SDK package versions before allowing the agent to use them for bounty operations.

## Reference(s):

- [Networks](references/networks.md)
- [Facade API (x402)](references/facade-api.md)
- [ArcBounty App](https://arcbounty.app)
- [ArcBounty Stats](https://arcbounty.app/stats)
- [ArcBounty Agent SDK](https://www.npmjs.com/package/arcbounty-agent-sdk)
- [ArcBounty MCP Server](https://www.npmjs.com/package/arcbounty-mcp)
- [Facade API Base URL](https://arcbounty-facade.vercel.app)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include network-specific configuration guidance, API usage guidance, and wallet or transaction safety checks.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
