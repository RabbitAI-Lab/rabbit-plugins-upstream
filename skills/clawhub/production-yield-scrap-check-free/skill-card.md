## Description:

生产投入产出与报废表逐项核对（逐行复算、合计勾稽、重复与空缺检测），每条结论引用原文。本免费版执行引擎声明的免费检查项。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Finance, cashier, and manufacturing operations staff use this skill during monthly close, reconciliation, or inventory checks to verify production yield and scrap tables. It recomputes row-level arithmetic, total rows, duplicate rows, blank placeholders, and selected negative quantities, while reporting missing material instead of issuing unsupported conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may assume the free release runs every production yield and scrap control.

Mitigation: Review the reported checks_not_run list and apply separate controls for withheld checks such as cross-process transfer matching.

Risk: Incomplete or malformed table input can make conclusions unreliable.

Mitigation: Provide the required table headers and rows, and treat insufficient-input responses as no conclusion.

Risk: The checker does not establish whether a yield or scrap rate is reasonable for a specific industry or plant.

Mitigation: Compare results with plant history, customer requirements, and internal manufacturing or finance review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/production-yield-scrap-check-free)
- [ClawHub publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Human-readable console text or pretty-printed JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings cite source rows; insufficient input returns missing fields rather than a pass/fail conclusion.]

## Skill Version(s):

1.0.53 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
