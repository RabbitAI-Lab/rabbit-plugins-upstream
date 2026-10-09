## Description:

Check an AI agent's repayment record, pay x402 APIs in USDG within spending caps, borrow from a Priors credit line, and repay before the due date.

This skill is ready for commercial/non-commercial use.

## Publisher:

[priors-agents](https://clawhub.ai/user/priors-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use Priors to review an agent's repayment history before transacting, then make capped API payments or manage short-term credit with an approved wallet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payment, borrowing, and repayment can move real funds when a wallet key is configured.

Mitigation: Use a dedicated low-balance wallet, keep spend and borrow caps small, and confirm the amount and counterparty before each mainnet action.

Risk: Exposing a wallet private key could allow unauthorized transactions.

Mitigation: Keep the key out of chats and command lines; read-only record checks do not require it.

## Reference(s):

- [Priors skill homepage](https://github.com/priors-agents/agent001/tree/main/skills/priors)
- [Priors record-check API documentation](https://github.com/priors-agents/priors/blob/main/docs/CHECK-API.md)
- [Priors security documentation](https://github.com/priors-agents/priors/blob/main/docs/SECURITY-v2.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Record checks may include repayment figures and scores; payment and loan actions require user approval.]

## Skill Version(s):

0.2.4 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
