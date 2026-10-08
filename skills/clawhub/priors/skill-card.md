## Description:

Check an AI agent's repayment record, pay x402 APIs in USDG on Robinhood Chain within spending caps, and borrow and repay from a Priors credit line.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use Priors to review a counterparty's repayment history before transacting and, with an authorized wallet, pay for APIs or manage short-term USDG credit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payments, borrowing, and repayment move real funds and may create debt.

Mitigation: Require approval for each transaction, use a dedicated low-balance wallet, and set conservative spend and borrow caps.

Risk: Exposing the wallet private key could allow unauthorized transactions.

Mitigation: Keep PRIORS_KEY out of chats, command history, and shared configuration.

Risk: Missed loan due dates can result in default.

Mitigation: Check open-loan due dates and arrange repayment before borrowing.

Risk: Installing and running cloned software may execute unreviewed code.

Mitigation: Review the cloned repository before running npm install or autopilot commands.

## Reference(s):

- [Priors skill on ClawHub](https://clawhub.ai/priors-agents/skills/priors)
- [Priors skill homepage](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Priors check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security notes](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with repayment summaries, setup commands, and transaction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports repayment status and amounts; wallet transactions require user approval and spending caps.]

## Skill Version(s):

0.2.1 (source: frontmatter, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
