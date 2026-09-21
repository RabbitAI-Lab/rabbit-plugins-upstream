## Description:

A local payroll, social-insurance, housing-fund, individual-tax, commission, bonus, overtime, piece-rate, and construction-wage checker that runs 14 built-in checks per client directory and reports one conclusion line per client with source file and line evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Payroll, HR, and bookkeeping staff use this skill before monthly payroll and social-insurance filing to check each client folder for arithmetic, reconciliation, coverage, and source-line issues across the included payroll and HR worksheets. It helps flag review items but does not provide legal, tax, social-insurance, audit, or assurance conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Payroll and HR materials can contain sensitive employee compensation, tax, and identity information.

Mitigation: Run the skill only on payroll/HR data the user is comfortable processing locally through the agent, and keep input directories limited to the client materials needed for the check.

Risk: A clean result may be mistaken for complete legal, tax, social-insurance, audit, or assurance coverage.

Mitigation: Treat results as review findings only, and have qualified staff verify payroll, tax, social-insurance, audit, and local-policy conclusions before relying on them.

Risk: Some checks and sub-checks are explicitly not run in this free release or when input material is incomplete.

Mitigation: Review the not-run and sub_checks_not_run sections before acting on results, and do not interpret unexecuted checks as passed checks.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/payroll-hr-pack-free)
- [Publisher Profile](https://clawhub.ai/user/chenqg618)
- [Skill README](artifact/SKILL.md)
- [Sample Input Template](artifact/templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain-text or JSON payroll-check summaries with client-level conclusions, issue counts, and source file/line evidence.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local Node.js checks against user-provided payroll/HR material; evidence reports no network use or persistence.]

## Skill Version(s):

1.0.30 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
