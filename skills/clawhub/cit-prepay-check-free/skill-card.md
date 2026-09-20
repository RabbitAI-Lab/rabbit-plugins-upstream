## Description:

季度预缴所得税计算表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance and bookkeeping users run this skill before quarterly enterprise income tax prepayment filing to check table arithmetic, totals, duplicate periods, blanks, and placeholder values. The skill reports findings with source citations and withholds conclusions when the supplied table is incomplete.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process sensitive financial worksheet content.

Mitigation: Provide only the relevant exported quarterly prepayment table text and avoid adding unrelated financial records or credentials.

Risk: The skill checks table arithmetic and consistency but does not determine tax-law eligibility or official filing positions.

Mitigation: Use the output as a local pre-check and confirm tax treatment, preferential-rate eligibility, and filing decisions with the applicable tax rules or a qualified reviewer.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/cit-prepay-check-free)
- [Sample input template](templates/sample.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON report with cited findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally, uses user-supplied table text, and returns insufficient-input guidance instead of unsupported conclusions when required fields are missing.]

## Skill Version(s):

1.0.51 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
