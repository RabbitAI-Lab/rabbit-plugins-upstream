## Description:

Check an AI agent's repayment record, pay x402 APIs in USDG on Robinhood Chain within limits, borrow from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators check repayment records before dealing with other agents, and optionally use a dedicated wallet to pay for APIs, borrow USDG, and repay loans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet-enabled actions move real USDG or create loans on mainnet.

Mitigation: Use a dedicated low-balance wallet, enforce spending limits, and confirm each amount before payment or borrowing.

Risk: Exposing the wallet private key could allow unauthorized spending.

Mitigation: Keep PRIORS_KEY out of chat and configuration files; review the external setup sources before running them.

Risk: A loan that is not repaid by its due date can result in default.

Mitigation: Check open loans and their due dates, borrow only repayable amounts, and repay on time.

## Reference(s):

- [Priors skill homepage (publisher-provided metadata)](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Priors check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security documentation](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)
- [agent001 setup project](https://github.com/priors-agents/agent001)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only record checks need no wallet key; payment and loan guidance requires user approval.]

## Skill Version(s):

0.2.8 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
