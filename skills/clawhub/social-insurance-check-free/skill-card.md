## Description:

社保申报明细逐项核对（逐行算术、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and payroll users use this skill during monthly payroll, closing, and reconciliation workflows to check social-insurance and housing-fund declaration details. It performs deterministic arithmetic, total cross-checks, duplicate-person checks, and blank or placeholder detection while citing source line numbers for each finding.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive payroll and social-insurance data.

Mitigation: Run it only on a trusted local machine and avoid sharing input or output files outside the intended review workflow.

Risk: The free skill includes an optional paid-upgrade path that asks the user to run a mutable external installer and complete a purchase/install flow.

Mitigation: Do not run the installer or approve purchase actions unless the SkillPay package, merchant, product, and payment flow have been independently verified.

Risk: The free edition omits several checks, including contribution-ratio, base-limit, and personal-versus-company base consistency checks.

Mitigation: Treat results as scoped reconciliation findings and keep human payroll or compliance review for omitted checks and policy-sensitive judgments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/social-insurance-check-free)
- [SkillPay shelf for optional full edition](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay install and purchase guide](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Plain text or JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally over copied social-insurance detail text or JSON input; insufficient input returns missing-field guidance instead of a conclusion.]

## Skill Version(s):

1.0.4 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
