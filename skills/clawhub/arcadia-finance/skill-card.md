## Description:

DeFi liquidity management on Uniswap and Aerodrome, live on Base, Unichain, and Optimism. Deploy concentrated liquidity positions with automated rebalancing, compounding, yield optimization, and leverage, or provide single-sided liquidity to lending pools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thomas-smets](https://clawhub.ai/user/thomas-smets)

### License/Terms of Use:

MIT-0

## Use Case:

External DeFi users and developers use this skill to inspect Arcadia accounts, pools, strategies, and automations, then prepare unsigned transaction payloads for liquidity management on Base, Unichain, and Optimism.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill calls a broad remote MCP tool interface for financial workflows.

Mitigation: Install only if you trust Arcadia's MCP endpoint and review the requested tool, arguments, and returned result before acting.

Risk: Write operations return transaction parameters that could affect wallet assets if signed.

Mitigation: Review every returned unsigned transaction in a trusted wallet before signing or broadcasting.

Risk: Wallet and account details plus transaction parameters are sent to the Arcadia endpoint.

Mitigation: Use only public addresses and amounts, and do not provide private keys, seed phrases, or secrets as tool arguments.

## Reference(s):

- [Arcadia website](https://arcadia.finance)
- [Arcadia documentation](https://docs.arcadia.finance)
- [Arcadia MCP full tool documentation](https://mcp.arcadia.finance/llms-full.txt)
- [Contract addresses](artifact/contracts.md)
- [Signing unsigned transactions](artifact/wallet-signing.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with bash examples and JSON arguments; write tools return unsigned transaction JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl and jq; connects to the Arcadia MCP endpoint and returns unsigned transactions for separate wallet review and signing.]

## Skill Version(s):

1.2.0 (source: frontmatter, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
