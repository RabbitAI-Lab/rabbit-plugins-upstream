## Description:

分包结算与产值核对表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and construction operations users use this skill during monthly closing, reconciliation, and subcontract settlement review to check table arithmetic, totals, duplicate rows, blanks, and negative values. It reports only conclusions supported by the provided source material and lists missing inputs when the table cannot be checked.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a paid-upgrade prompt that asks an AI assistant to install external code and start a payment workflow.

Mitigation: Use the free local checker without the paid path unless the user explicitly wants that workflow; verify package source, pin versions where possible, avoid elevated privileges, and require the user to personally confirm payment steps.

Risk: The free checker performs only the declared subset of settlement checks and withholds several checks for a separate paid version.

Mitigation: Treat results as coverage for the listed free checks only and review withheld and out-of-scope checks before relying on the output for settlement decisions.

Risk: The checker depends on complete, recognizable table input and reports no conclusion when required columns or data are missing.

Mitigation: Provide the subcontract settlement table with headers and source rows, and have a qualified reviewer confirm financial conclusions against the original records.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/subcontract-settlement-check-free)
- [SkillPay shelf referenced by artifact](https://skillpay.alipay.com/public/tokendidi)
- [Purchase and installation guide referenced by artifact](https://chenqg618.github.io/compliance-skills/buy.html)
- [SkillPay build guide referenced by artifact](https://skillpay.alipay.com/buildguide.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with shell commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local checker output cites source rows when input is sufficient and reports missing inputs instead of fabricating conclusions.]

## Skill Version(s):

1.0.6 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
