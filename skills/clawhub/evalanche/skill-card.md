## Description:

Evalanche provides an autonomous multi-chain wallet SDK and MCP server for EVM transactions, identity, payments, bridging, trading, and DeFi operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ijaack](https://clawhub.ai/user/ijaack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use Evalanche to give autonomous agents wallet access for checking balances and identity, making payments, moving assets across supported chains, trading, and using DeFi services through code or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Autonomous wallet access and transaction tools can cause irreversible asset loss, and the skill may handle private keys or recovery phrases.

Mitigation: Start with address-only access, quotes, or testnets; use a separate minimally funded wallet; configure signer approvals and spending limits before funding autonomous operations; verify amounts, chains, recipients, and approvals; protect keystore and recovery material.

## Reference(s):

- [Evalanche project repository](https://github.com/iJaack/evalanche)
- [Evalanche ClawHub release page](https://clawhub.ai/ijaack/skills/evalanche)

## Skill Output:

**Output Type(s):** [API calls, JSON, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Structured wallet and market data, transaction results, and setup guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On-chain transactions can spend real assets and incur network fees.]

## Skill Version(s):

1.17.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
