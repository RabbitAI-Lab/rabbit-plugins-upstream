## Description:

Checks monthly housing fund contribution schedules locally, recalculating contribution amounts, totals, duplicate people, missing or negative fields, and base amounts above table-provided limits with line-cited findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, treasury, and HR staff use this skill during monthly payroll and housing-fund remittance checks to verify pasted contribution schedules before reporting, payroll posting, or bookkeeping. It helps recalculate table-provided arithmetic and surface missing, duplicate, negative, or out-of-range entries with source line references.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: The skill is intended for sensitive payroll-style housing-fund data.

Mitigation: Use it only in an environment where the user is comfortable processing that data locally, and avoid sharing pasted contribution schedules outside the local agent session.

Risk: The optional paid-upgrade path may run an unpinned remote npx installer and initiate payment onboarding.

Mitigation: Treat the paid upgrade as a separate decision; do not run the installer, payment onboarding, or purchase steps unless the user independently verifies the source and intends to buy.

Risk: The default human-readable path includes an upsell prompt and may write a small temporary marker file.

Mitigation: Use --json when the user wants the checker result without the default upsell prompt path and temporary marker writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/housing-fund-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [Optional paid upgrade instructions](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance, Shell commands]

**Output Format:** [Human-readable console text by default; structured JSON when run with --json.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields and no conclusion.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
