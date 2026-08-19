## Description:

AI-native lending on Base MAINNET for autonomous agents. Check credit, request USDC loans (EIP-712 signed via Coinbase CDP), and repay autonomously. Real money.

This skill is ready for commercial/non-commercial use.

## Publisher:

[rsoft-latam](https://clawhub.ai/user/rsoft-latam)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and autonomous-agent operators use this skill to configure a Coinbase CDP wallet, check agent credit, request Base mainnet USDC loans, and repay them through REST commands or MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can move real USDC on Base mainnet through high-impact wallet actions.

Mitigation: Install it only with a dedicated low-balance CDP project and wallet, and manually confirm recipient, amount, chain, and token before broadcasting transactions.

Risk: CDP credentials used by the skill can control every wallet in the configured CDP project.

Mitigation: Use credentials dedicated to this agent, keep the wallet config outside synced folders, restrict file permissions, and avoid connecting broader funds to the same project.

Risk: Unpinned runtime dependencies could change before the skill is used with real funds.

Mitigation: Review the repayment scripts and pin dependencies before operating with real USDC.

## Reference(s):

- [RSoft Agentic Bank website](https://rsoft-agentic-bank.com/)
- [RSoft Agentic Bank documentation](https://rsoft-agentic-bank.com/docs)
- [ClawHub skill page](https://clawhub.ai/rsoft-latam/skills/rsoft-agentic-bank)
- [ClawHub publisher profile](https://clawhub.ai/user/rsoft-latam)
- [BaseScan](https://basescan.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration instructions, API calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include wallet addresses, EIP-712 signatures, request IDs, transaction hashes, and API responses.]

## Skill Version(s):

2.2.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
