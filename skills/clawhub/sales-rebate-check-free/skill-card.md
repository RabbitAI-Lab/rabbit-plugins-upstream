## Description:

返利台账逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Sales finance and commercial operations teams use this skill before monthly accruals and quarterly or annual rebate payouts to check sales rebate ledgers for arithmetic mismatches, duplicate customer/policy rows, blank fields, and negative rebate or payout values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime messaging about anonymous usage statistics and a --no-stats option is inconsistent with the inspected code and may confuse users who require strict data-flow clarity.

Mitigation: Ask the publisher to remove or implement that messaging consistently, and evaluate the release against the server security summary before use in strict environments.

Risk: The skill checks ledger arithmetic and completeness but does not make accounting, audit, contract authenticity, system reconciliation, or tax determinations.

Mitigation: Treat results as a rebate-ledger review aid and have qualified finance, audit, or tax reviewers make final judgments under company policy and applicable rules.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/sales-rebate-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Console text or JSON containing findings, severity levels, cited source values, summary counts, and checks not run in the free edition.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided ledger text or JSON; reports insufficient input without producing a clean-result conclusion.]

## Skill Version(s):

1.0.13 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
