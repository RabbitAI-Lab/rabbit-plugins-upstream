## Description:

Check an AI agent's repayment record before you pay or trust it, pay x402 APIs in USDG on Robinhood Chain within caps, borrow the shortfall from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Priors to check an agent's repayment history before trusting it with work or payment, and to make capped x402 payments or manage a credit line when they explicitly authorize wallet transactions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-enabled tools can make real-money payments, borrow funds, and approve repayment automation on Robinhood Chain mainnet.

Mitigation: Use a dedicated wallet with a small balance and spending caps, state the amount, and get explicit user approval before each signing action.

Risk: Late repayment can permanently damage the agent's record and may leave a backer responsible for the debt.

Mitigation: Check open-loan due dates and repayment funds, and repay before the due date.

Risk: The skill discloses that Priors has not had a third-party audit, and this review does not verify the external server or smart contracts.

Mitigation: Review the linked security findings and understand the external service and contract risks before enabling wallet actions.

## Reference(s):

- [Priors](https://priors.trade)
- [Priors record check API](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security findings and fixes](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)
- [agent001 setup](https://github.com/priors-agents/agent001)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes record interpretation guidance, transaction approval steps, spending caps, and repayment reminders.]

## Skill Version(s):

0.2.16 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
