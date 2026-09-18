## Description:

逐项核对备用金与报销核销表的行级算术、合计勾稽、重复行、空白占位符和负金额，并为结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and cashier teams use this skill during monthly close, reconciliation, stocktaking, handoff, and internal control checks to review petty-cash and reimbursement write-off ledgers. It helps identify arithmetic mismatches, repeated rows, missing placeholders, negative amounts, and insufficient input without sending materials off the local machine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes an optional paid-version workflow that asks an agent to run an unpinned remote npx install and proceed toward purchase steps.

Mitigation: Use only the bundled local checker unless the external package, merchant, and payment flow have been separately reviewed; require the user to confirm any wallet authorization or payment.

Risk: The free checker omits several checks and does not evaluate invoice authenticity, ERP/OA exports, internal limits, approval authority, tax treatment, or collection decisions.

Mitigation: Treat findings as ledger arithmetic and completeness checks only; review withheld checks and local finance policies before relying on the result for close, audit, or recovery decisions.

Risk: Release evidence and artifact frontmatter disagree on license terms.

Mitigation: Confirm the governing release license before publication or redistribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/petty-cash-check-free)
- [Optional paid-version purchase instructions referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON summaries with row-level findings and cited source lines]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; input is a JSON file or pasted tabular text.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
