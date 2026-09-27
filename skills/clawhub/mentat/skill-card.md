## Description:

Helps agents request OTC token-swap quotes and manage trades through Base escrow, CoW Protocol relay, or an XMR route via Wagyu.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agora0x](https://clawhub.ai/user/agora0x)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use MENTAT to obtain token-swap quotes, prepare or place orders, and check settlement status and transaction proofs across its supported routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sending funds to an incorrect address or on the basis of an estimated quote can cause loss.

Mitigation: Review the created order's exact destination, amount, and expiry before funding; do not treat a quote as funding instructions.

Risk: Token approvals or signed trade data may authorize unwanted transfers or fees.

Mitigation: Check typed data, approval targets, amounts, and fees before signing or approving.

Risk: The XMR route depends on Wagyu to deliver and is not trustless; trades may leave public records.

Mitigation: Assess counterparty trust and record visibility before using the route, and review its settlement proofs.

## Reference(s):

- [MENTAT on ClawHub](https://clawhub.ai/agora0x/skills/mentat)
- [MENTAT website](https://mentat.market)
- [MENTAT agent documentation](https://mentat.market/llms.txt)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses and Markdown usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Quote and order responses include the settlement path, route legs, and available transaction proofs.]

## Skill Version(s):

1.4.3 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
