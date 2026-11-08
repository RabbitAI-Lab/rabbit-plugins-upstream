## Description:

Check an AI agent's repayment record before you pay or trust it, pay x402 APIs in USDG on Robinhood Chain within caps, borrow the shortfall from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use Priors to check an ERC-8004 agent's repayment record before paying or relying on it. With explicit user approval, they can also make capped USDG payments, borrow, and repay through a wallet on Robinhood Chain.

### Deployment Geography for Use:

Global; optional stock token features may be geographically restricted.

## Known Risks and Mitigations:

Risk: Payment, borrowing, repayment, and automated repayment actions can move real funds or approve future repayment.

Mitigation: State the amount and get user approval before each signing action; use a dedicated wallet with limited funds and low caps, and understand how to stop automation and revoke approvals.

Risk: The external financial software is unverified and has no third-party audit.

Mitigation: Start with keyless record checks and review the external wallet software and its published security findings before enabling transactions.

## Reference(s):

- [Priors](https://priors.trade)
- [Priors Check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security findings and fixes](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)
- [Priors MCP server](https://mcp.priors.trade/mcp)
- [agent001 setup guide](https://github.com/priors-agents/agent001)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance, JSON service responses, and inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May initiate real-money on-chain transactions only after user approval; the skill describes wallet setup, spending caps, and repayment steps.]

## Skill Version(s):

0.2.17 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
