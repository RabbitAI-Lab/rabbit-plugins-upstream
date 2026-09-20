## Description:

Checks accrued and prepaid expense amortization detail tables for row-level arithmetic, total reconciliation, duplicate rows, blanks, and missing required columns, with findings tied to source evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

General ledger accountants use this skill before monthly close or expense-period review to check whether accrued and prepaid expense amortization detail tables reconcile internally. It supports arithmetic and completeness review, but does not replace accounting, tax, audit, or policy judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The results can be mistaken for accounting, tax, audit, or assurance conclusions.

Mitigation: Use the output as an internal table-arithmetic check and have qualified finance or audit reviewers validate policy, tax, and assurance decisions.

Risk: The free edition intentionally omits several checks, including line-method variance and negative ending-balance checks.

Mitigation: Treat results as covering only the listed free checks and review the omitted-check notice before relying on the output.

Risk: Incomplete or unrecognized table input can prevent checks from running or limit which checks apply.

Mitigation: Provide copied table text with the required headers and review missing-column or insufficient-input messages before drawing conclusions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/accrued-expense-amortization-check-free)

## Skill Output:

**Output Type(s):** [text, JSON, guidance, shell commands]

**Output Format:** [Plain text or JSON check results with cited table evidence and omitted-check notices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports P0/P1 findings, insufficient-input status, checks performed, and checks not included in the free edition.]

## Skill Version(s):

1.0.21 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
