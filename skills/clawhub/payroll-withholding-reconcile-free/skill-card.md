## Description:

工资表与个税社保申报对照表逐项核对，覆盖逐行复算、合计勾稽、重复与空缺检测，并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, payroll, and HR operators use this skill during monthly payroll reconciliation to compare payroll withholding data with individual income tax and social security filing data. It helps identify row-level mismatches, total-row issues, duplicate personnel, blanks, placeholders, and missing filing-side values from user-provided tabular text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises a paid upgrade workflow that asks an agent to run unpinned remote code through `npx ...@latest`.

Mitigation: Only run that purchase or installation workflow after independently verifying the publisher, package, and source, and only when the user intentionally wants to use SkillPay.

Risk: The free checker intentionally omits several payroll reconciliation checks that are described as available only in the paid edition.

Mitigation: Treat clean free-edition output as limited to the listed checks, and review the `checks_not_run` and `checks_out_of_scope` fields before relying on the result.

Risk: Payroll and filing data can contain sensitive personal and compensation information.

Mitigation: Prefer the documented local execution path and avoid sending input files or pasted table contents to untrusted services.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/payroll-withholding-reconcile-free)
- [ClawHub Publisher Profile](https://clawhub.ai/user/chenqg618)
- [SkillPay Shelf Referenced by Skill Documentation](https://skillpay.alipay.com/public/tokendidi)
- [Paid Upgrade Purchase Information Referenced by Skill Documentation](https://chenqg618.github.io/compliance-skills/buy.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Human-readable text or JSON containing executed checks, findings, summary, scope, and disclaimers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; accepts JSON or pasted tabular text input; does not make network requests according to the artifact.]

## Skill Version(s):

1.0.7 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
