## Description:

Spraay × Bankr helps an agent prepare Bankr-funded Spraay batch payments for token airdrops, fee splits, USDC payroll, and other ERC-20 distributions with validation, estimation, and explicit user confirmation before funds move.

This skill is ready for commercial/non-commercial use.

## Publisher:

[plagtech](https://clawhub.ai/user/plagtech)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to coordinate batch payouts from a Bankr wallet through Spraay, including airdrops, creator-fee splits, treasury payroll, and other onchain recipient distributions. The workflow emphasizes recipient validation, cost estimation, and clear confirmation before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can prepare Bankr-funded Spraay batch payments, so mistakes in recipients, token, amounts, chain, or total cost can move real funds.

Mitigation: Verify the recipient list, token, amounts, total cost, chain, and transaction estimate before approving any execution.

Risk: The Bankr API key controls access to real funds.

Mitigation: Treat the key as sensitive and avoid exposing it outside the intended Bankr API flow.

Risk: A malformed or fabricated recipient list can cause incorrect payouts.

Mitigation: Use only user-provided or verifiable recipient data and run Spraay validation and estimation before requesting confirmation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/plagtech/skills/spraay-bankr)
- [Spraay gateway](https://gateway.spraay.app)
- [Spraay docs](https://docs.spraay.app)
- [Spraay live dashboard](https://live.spraay.app)
- [Bankr docs](https://docs.bankr.bot)
- [Bankr skills](https://github.com/BankrBot/skills)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown instructions with API endpoint details, validation steps, estimates, confirmation prompts, and transaction summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided or verifiable recipient data and explicit confirmation before execution; may return transaction hashes and per-recipient payout summaries.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
