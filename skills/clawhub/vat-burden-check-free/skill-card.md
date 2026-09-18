## Description:

增值税进销项汇总表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, tax, and operations users can run this skill before monthly VAT filing to check VAT input-output worksheets for arithmetic consistency, carry-forward credit issues, total-row mismatches, duplicate periods, and missing required cells. The free release reports only the checks it actually executes and cites source line numbers for findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The free VAT checker is local and purpose-aligned, but the artifact includes paid-upgrade instructions that ask an agent to run unpinned remote code and follow newly installed instructions.

Mitigation: Do not run the paid-upgrade command or authorize installation or purchase of the full version unless the SkillPay source, package version, integrity, and newly installed instructions are independently verified in a restricted environment.

Risk: The checker reads the VAT table file supplied by the user.

Mitigation: Use it only when local Node execution over the provided VAT table is acceptable for the data involved.

Risk: The free release omits several checks that are listed as paid-version functionality.

Mitigation: Treat results as limited to the executed free checks and do not rely on them as a full tax compliance review.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chenqg618/skills/vat-burden-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)
- [SkillPay public shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source line numbers; JSON mode is available for machine-readable results.]

## Skill Version(s):

1.0.12 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
