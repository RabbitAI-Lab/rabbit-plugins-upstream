## Description:

Provides a free local check of payroll payable ledgers for row arithmetic, total reconciliation, duplicate months, and blank or placeholder fields, with source-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, and bookkeeping users can run this skill during monthly close or reconciliation to check payroll payable ledger arithmetic, totals, duplicate periods, and missing values. It reports missing input instead of drawing conclusions when the ledger lacks required columns or recognizable data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions include a paid-upgrade flow that asks an AI assistant to install remote payment software and start a purchase.

Mitigation: Do not copy the paid-upgrade prompt or run the npx command unless you independently verify the SkillPay instructions, package version, merchant, product, price, and permissions, and personally approve each installation and payment step.

Risk: Payroll ledger text can contain sensitive compensation data.

Mitigation: Run the local checker only in a trusted environment and avoid sharing ledger input outside approved channels.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/payroll-payable-check-free)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Human-readable text or JSON findings with source line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally on user-provided payroll ledger text; insufficient input returns missing-field guidance rather than conclusions.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
