## Description:

Check an AI agent's repayment record before you pay or trust it, pay x402 APIs in USDG on Robinhood Chain within caps, borrow the shortfall from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use Priors to check repayment histories before interacting with other agents and, with a dedicated wallet, pay for x402 services, borrow USDG, and manage repayments on Robinhood Chain.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured wallet can authorize real-money payments, borrowing, and repayments on Robinhood Chain.

Mitigation: Use the read-only service for reputation checks; for wallet actions, use a dedicated, minimally funded wallet with tight spending and borrowing caps, and confirm each mainnet action.

Risk: Exposing the wallet private key can compromise funds.

Mitigation: Keep PRIORS_KEY out of chat and configuration files; provide it only through the wallet service's environment.

Risk: Missed repayments or unattended autopilot can create financial and reputation consequences.

Mitigation: Review loan fees and due dates, plan repayment before borrowing, and review any long-running autopilot setup before enabling it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/priors-agents/skills/priors)
- [Skill homepage listed in release metadata](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Priors record-check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Agent001 wallet and credit-line setup](https://github.com/priors-agents/agent001)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Repayment-record interpretation and steps for payments, borrowing, and repayment; wallet actions require user approval.]

## Skill Version(s):

0.2.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
