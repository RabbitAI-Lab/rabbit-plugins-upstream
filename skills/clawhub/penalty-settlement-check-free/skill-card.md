## Description:

Provides a free, local, deterministic check for penalty and liquidated damages ledgers, including balance recalculation, total reconciliation, duplicate document IDs, missing or placeholder fields, direction and amount sign consistency, and inverted dates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and accounting users use this skill to check Chinese-language penalty and liquidated damages ledgers before monthly closing or annual settlement. It reports line-referenced arithmetic, consistency, duplicate, missing-field, sign, and date-order findings without giving tax or legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ledger inputs can contain sensitive financial or counterparty information.

Mitigation: Run the checker only in trusted environments and review input files before use; the security evidence reports no hidden data access, persistence, or destructive behavior.

Risk: A passed check can be mistaken for tax or legal approval.

Mitigation: Use the output as ledger arithmetic and consistency analysis only; route tax deductibility, administrative penalty, and legal questions to qualified reviewers.

Risk: The free version omits several checks that may matter for full settlement review.

Mitigation: Review the reported checks_not_run and do not treat a clean result as coverage for omitted tax adjustment, overdue receivable, missing basis document, cross-period, same-matter duplicate, or ranked action-list checks.

Risk: Some help text mentions anonymous statistics even though the current evidence describes the code as local-only.

Mitigation: Confirm the deployed package version's network behavior against organizational policy before using it with confidential ledger data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/penalty-settlement-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable text or JSON containing findings, source line references, summary totals, executed and omitted checks, and remediation advice.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on tabular ledger text with required headers; reports insufficient input rather than filling missing values or issuing a false clean result.]

## Skill Version(s):

1.0.49 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
