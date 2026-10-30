## Description:

Check an AI agent's repayment record before you pay or trust it, pay x402 APIs in USDG on Robinhood Chain within caps, borrow the shortfall from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

External agent operators and developers use Priors to check repayment records before paying or relying on another agent. They can also configure a wallet to pay x402 services, borrow within limits, and repay loans on time.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payments, borrowing, repayments, and automated repayment approvals can move real funds or create repayment obligations.

Mitigation: Start with key-free record checks; use a dedicated wallet with limited funds, keep spending and borrowing caps low, approve amounts carefully, and track loan due dates.

Risk: Savings and trading features involve investment risk, and the project states that it has not had a third-party audit.

Mitigation: Treat these features as financial risk and do not take the skill's guidance as independent verification of external software or contracts.

## Reference(s):

- [Priors service](https://priors.trade)
- [Priors skill homepage (metadata)](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Agent setup repository](https://github.com/priors-agents/agent001)
- [Security findings and fixes](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)
- [ClawHub release page](https://clawhub.ai/priors-agents/skills/priors)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Text and structured tool results, with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include repayment-record details and transaction results; financial actions require user approval as described by the skill.]

## Skill Version(s):

0.2.14 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
