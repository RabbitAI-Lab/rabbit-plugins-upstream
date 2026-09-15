## Description:

增值税进销项汇总表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and tax operations users can run this local checker before monthly VAT filing to recalculate VAT payable, ending input tax credit, VAT burden rate, totals, duplicate periods, and missing key fields. It is intended for worksheet consistency checks, not tax advice or special VAT treatment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documentation includes an optional paid-upgrade prompt that asks an agent to run an unpinned remote installer and purchase or install a separate skill.

Mitigation: Ignore or manually vet the paid-upgrade section; independently verify the package, version, publisher, payment page, and newly installed skill before allowing any agent-run install or purchase flow.

Risk: Users may overread the worksheet check as tax advice or as coverage for VAT cases outside the free checker.

Mitigation: Review the executed, withheld, and out-of-scope checks before relying on results, and use qualified tax review for deductibility, special VAT treatments, planning, or source worksheets missing required headers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/vat-burden-check-free)
- [SkillPay storefront referenced by the skill](https://skillpay.alipay.com/public/tokendidi)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Human-readable console text or structured JSON findings with source line references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally with Node.js standard library; reports insufficient input instead of fabricating conclusions.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
