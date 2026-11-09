## Description:

Manage DeFi liquidity on Uniswap and Aero across Base, Optimism, Unichain, and Robinhood by preparing concentrated liquidity, lending, rebalancing, compounding, and yield optimization actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomas-smets](https://clawhub.ai/user/thomas-smets)

### License/Terms of Use:

MIT-0

## Use Case:

DeFi users use this skill to review Arcadia accounts, strategies, and lending pools, then prepare liquidity, lending, and automation transactions across supported networks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses shell access and makes external service calls, and its tool scope is not declared.

Mitigation: Use it only where shell access and external calls are acceptable; review the requested actions and data sent to Arcadia before use.

Risk: Write operations can prepare transactions that affect on-chain positions or lending balances.

Mitigation: Review transaction details and account health, obtain explicit user confirmation before signing, and keep private keys out of skill arguments.

## Reference(s):

- [Arcadia Finance](https://arcadia.finance)
- [Arcadia documentation](https://docs.arcadia.finance)
- [Arcadia MCP tool documentation](https://mcp.arcadia.finance/llms-full.txt)

## Skill Output:

**Output Type(s):** [API responses, JSON, Shell commands, Guidance]

**Output Format:** [Text and JSON, with shell commands and unsigned transaction data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Write operations produce unsigned transaction proposals; a separate wallet is required to sign and broadcast.]

## Skill Version(s):

1.5.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
