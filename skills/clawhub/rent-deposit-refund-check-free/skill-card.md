## Description:

A local rent and security deposit ledger checker that recomputes refundable amounts, validates deduction basis and limits, flags overdue or duplicate refunds, reconciles ledger balances, and reports row-cited findings when input is sufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

Proprietary

## Use Case:

Finance, cashier, property, and leasing operations teams use this skill to check rent or security deposit ledgers before refund payment and month-end reconciliation. It helps verify table-internal arithmetic, refund timing, duplicate refund indicators, missing fields, and negative amounts without making legal or payment-validity determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes rent and security deposit ledger data locally, which may include sensitive business or tenant information.

Mitigation: Run it only in an environment approved for that ledger data and review outputs before using them for payment, accounting, or dispute decisions.

Risk: Documentation around anonymous usage statistics and the --no-stats option is confusing according to the security review.

Mitigation: Treat the current release as local-only per the security evidence, and require publisher clarification or correction before relying on the statistics wording.

Risk: The artifact is primarily designed around Chinese ledger headers and messages.

Mitigation: Users with non-Chinese workflows should verify that required headers, parsing behavior, and output messages match their data before operational use.

Risk: The checker validates table-internal consistency but does not verify whether deposits were actually collected or refunded, whether deduction text is legally valid, or whether refund deadlines comply with local rules.

Mitigation: Use bank records, receipts, contracts, policies, and legal review for those determinations; treat this skill's findings as reconciliation support, not final authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/rent-deposit-refund-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable console text or JSON containing status, findings, summary, scope, missing-input advice, and row-cited bases.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard libraries; findings are produced only when required ledger columns and sufficient input are present.]

## Skill Version(s):

1.0.1 (source: artifact/SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
