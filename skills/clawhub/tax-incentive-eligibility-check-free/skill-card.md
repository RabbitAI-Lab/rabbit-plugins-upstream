## Description:

Checks Chinese tax incentive eligibility self-check tables by recalculating row ratios, deduction limits, totals, duplicate rows, blanks, and negative values, with each finding tied to the submitted table content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax staff use this skill to check arithmetic and consistency in tax incentive eligibility self-check tables during recurring close, reconciliation, prepayment, or annual settlement review. It is a table consistency aid, not tax or legal advice.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may treat arithmetic and table-consistency findings as tax or legal eligibility advice.

Mitigation: Use the output as a formatting and consistency aid only, and have qualified tax staff verify policy eligibility against current rules and the competent tax authority.

Risk: The free release intentionally omits several checks and may report no issues even when out-of-scope eligibility problems remain.

Mitigation: Review the reported scope and checks_not_run list before relying on the result, and perform separate review for omitted eligibility conditions.

Risk: The package text mentions anonymous statistics while the inspected code did not implement network telemetry.

Mitigation: Review the current release behavior before processing sensitive material and do not assume package descriptions about telemetry are complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/tax-incentive-eligibility-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Console text or JSON findings with status, scope, checks run, checks not run, findings, summary, and disclaimers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs against user-provided table text or a sample input; insufficient input returns missing-field guidance instead of an eligibility conclusion.]

## Skill Version(s):

1.0.42 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
