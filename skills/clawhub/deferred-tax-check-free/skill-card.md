## Description:

递延所得税台账逐项核对，逐行复算暂时性差异、递延所得税资产与负债余额、本期变动，复核合计行并检测重复与空缺，每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, tax, and audit users can run this skill to review deferred tax workpapers copied from spreadsheet tables. It performs local arithmetic and consistency checks for temporary differences, deferred tax balances, period movement, totals, duplicates, and missing fields, while preserving withheld paid checks as not executed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid-upgrade instructions ask an agent to run an unpinned remote installer and start purchase or install steps.

Mitigation: Do not run the paid-upgrade npx ... @latest command or start purchase/install steps unless the package, publisher, version, and payment flow are independently verified and the user confirms wallet or payment actions.

Risk: The security summary reports inconsistent claims about which financial checks actually ran.

Mitigation: Treat the output as a limited arithmetic/workpaper review and rely on executed versus withheld check lists; do not present withheld paid checks as completed.

Risk: Users may over-rely on checker output as a tax or audit conclusion.

Mitigation: Present results as local table arithmetic and consistency findings only, and require professional review for tax treatment, audit opinions, eligibility of deferred tax assets, and out-of-scope judgments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chenqg618/skills/deferred-tax-check-free)
- [Full Version Information](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay Shelf](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console report or JSON result object]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of a tax or audit conclusion.]

## Skill Version(s):

1.0.1 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
