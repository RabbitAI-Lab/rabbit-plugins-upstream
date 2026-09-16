## Description:

预算执行表逐项核对（逐行复算、合计勾稽、重复与空缺检测），并为每条结论引用原文依据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

财务、出纳等用户在月度结账、对账或盘点时，用它复算预算执行表的逐行算术、合计勾稽、重复科目和空白占位符问题。材料不足时，技能应说明缺少的内容而不是给出结论。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill points users toward an external SkillPay/Alipay paid install path that can run unpinned remote code.

Mitigation: Use the bundled local checker for the free checks unless the external purchase and install path has been separately reviewed and trusted; do not run the suggested npx @latest command merely to use the free checker.

Risk: The free checker does not perform the withheld execution-rate, cumulative-actual, negative-budget, range, or sign-consistency checks.

Mitigation: Treat results as limited to the listed free checks and require additional review before relying on the output for full budget-control decisions.

Risk: Malformed or incomplete budget table input can produce an insufficient-input result rather than a finding.

Mitigation: Provide a table with the required headers and do not interpret insufficient input as evidence that no issue exists.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/budget-variance-check-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON result output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs on user-provided budget table text; the free checker reports listed checks, withheld checks, insufficient-input status, and cited findings.]

## Skill Version(s):

1.0.8 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
