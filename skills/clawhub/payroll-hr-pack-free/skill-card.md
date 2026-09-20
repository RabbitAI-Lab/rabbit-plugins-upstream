## Description:

A local payroll, social insurance, housing fund, tax withholding, commission, overtime, piece-rate, bonus, and construction wage worksheet checker that runs 14 checks per client and reports cited findings with source files and line numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, HR, and bookkeeping staff use this skill before monthly payroll and social-insurance filing to check customer payroll materials for arithmetic and reconciliation issues. It is intended for Chinese payroll and HR text exports and reports one conclusion line per customer with detailed findings when input material is sufficient.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Users may treat checks_not_run or sub_checks_not_run as cleared checks.

Mitigation: Review checks_not_run and sub_checks_not_run before relying on results, and only treat executed checks as reviewed.

Risk: Users may rely on the output as an audit, legal opinion, or complete payroll compliance review.

Mitigation: Use the output as a worksheet-checking aid and have qualified staff verify payroll, audit, tax, and local policy decisions.

Risk: Construction wage special-account payout-total consistency may still require manual review.

Mitigation: Manually verify the special-account payout totals when that control matters.

Risk: Payroll materials may contain sensitive employee information.

Mitigation: Keep input directories and CLI output in approved local storage and limit access to staff who need the payroll review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-hr-pack-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON CLI output with per-client summaries, checks not run, and cited findings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; results cite source file and line when checks can be executed.]

## Skill Version(s):

1.0.26 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
