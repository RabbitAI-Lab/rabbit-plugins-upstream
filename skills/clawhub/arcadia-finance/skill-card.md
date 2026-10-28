## Description:

DeFi liquidity management on Uniswap and Aero, live on Base, Optimism, Unichain and Robinhood. Deploy concentrated liquidity positions with automated rebalancing, compounding, yield optimization, and leverage, or provide single-sided liquidity to lending pools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomas-smets](https://clawhub.ai/user/thomas-smets)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Arcadia accounts and manage concentrated or single-sided liquidity, lending, and liquidity automations across supported blockchain networks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incorrect networks, token or recipient addresses, amounts, approval limits, or automation permissions can expose funds or lead to unintended DeFi transactions.

Mitigation: Verify each transaction detail and automation permission before signing; keep signing in a separate wallet under user control and never provide private keys. Independently verify the newly listed AERO address and review how to revoke continuing approvals.

## Reference(s):

- [Arcadia Finance](https://arcadia.finance)
- [Arcadia documentation](https://docs.arcadia.finance)
- [Arcadia MCP tool documentation](https://mcp.arcadia.finance/llms-full.txt)
- [ClawHub release](https://clawhub.ai/thomas-smets/skills/arcadia-finance)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [JSON tool results and unsigned transaction parameters, with Markdown guidance and inline bash examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations return unsigned transactions; signing and broadcasting remain under the user's separate wallet control.]

## Skill Version(s):

1.4.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
