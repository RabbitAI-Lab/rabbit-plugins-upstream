## Description:

进度款申请与产值确认表逐项核对（申请/确认产值比对、确认产值×支付比例复算、累计确认产值滚动、本期实付勾稽、合计逐列复核、重复与空缺检测），每条结论引用原文行号。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Construction and finance teams use this skill to check Chinese-language progress-payment and output-confirmation tables before monthly payment workflows. It verifies table arithmetic, consistency, missing fields, duplicates, and source-line evidence without treating the result as legal, contract, or site-completion verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may overread arithmetic and table-consistency findings as legal, contract, or site-completion verification.

Mitigation: Present outputs as limited consistency checks and require qualified review for legal, contract, payment-approval, and site-completion decisions.

Risk: Incomplete or malformed tables can lead to missing context or unsupported conclusions.

Mitigation: Use the skill's insufficient-input responses and provide complete table headers and data rows before relying on findings.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/progress-output-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [analysis, text, json, shell commands, guidance]

**Output Format:** [Human-readable text or JSON containing findings, missing-input guidance, executed checks, omitted checks, and source-line references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source lines; insufficient materials return missing-field guidance instead of conclusions.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
