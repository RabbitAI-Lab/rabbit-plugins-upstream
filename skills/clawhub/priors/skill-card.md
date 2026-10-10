## Description:

Check an AI agent's repayment record before you pay or trust it, pay x402 APIs in USDG on Robinhood Chain within caps, borrow the shortfall from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their operators use Priors to review counterparties' repayment records and, with explicit approval, pay for APIs or manage USDG loans using a dedicated wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wallet payments and borrowing move real money on mainnet.

Mitigation: Obtain explicit approval for each transaction, use a dedicated low-balance wallet, and set and verify payment and borrowing caps.

Risk: A wallet private key may be exposed to untrusted software or configuration.

Mitigation: Use the read-only hosted server for record checks; install wallet-signing packages only if trusted, and never share or log the private key.

Risk: Missed repayments can result in default.

Mitigation: Check loan due dates, borrow only amounts the wallet can repay, and repay before the due date.

## Reference(s):

- [Priors skill on ClawHub](https://clawhub.ai/priors-agents/skills/priors)
- [Priors skill homepage (listed in metadata)](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Priors check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security notes](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with repayment-record summaries and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports repayment status and amounts; wallet actions require user approval.]

## Skill Version(s):

0.2.6 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
