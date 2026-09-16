## Description:

出口退税（免抵退）计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号，本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

External users with export operations use this skill before monthly export VAT rebate filing to recheck worksheet calculations, totals, duplicate customs declaration numbers, and blank or placeholder entries. It reports findings with source line references and returns insufficient-input status rather than conclusions when required worksheet data is missing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a prompt that asks an agent to install an unpinned external payment package and continue a paid purchase workflow.

Mitigation: Use the free checker only for local worksheet review unless a user intentionally chooses the paid workflow after independently reviewing the package version, permissions, and payment steps.

Risk: The free checker omits several validation checks, including rebate-rate bounds, non-positive FOB or exchange-rate detection, over-refund checks, and negative exempt-credit checks.

Mitigation: Treat a clean free-check result as confirmation only for the listed executed checks, and perform separate review for omitted checks and tax eligibility questions.

Risk: The checker does not determine the applicable export rebate rate, tax eligibility, processing-trade treatment, carryover treatment, or tax advice.

Mitigation: Have qualified tax staff verify rates, eligibility, enterprise-specific treatment, and filing decisions before using results in a tax process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/export-rebate-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay storefront referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay installation guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance and command examples; optional JSON checker results from the local Node runner]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; insufficient input returns missing fields instead of a pass/fail conclusion.]

## Skill Version(s):

1.0.15 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
