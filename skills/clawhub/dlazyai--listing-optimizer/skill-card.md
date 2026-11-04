## Description:

主图 A/B 组与转化复盘。商品图 + 卖点 → 多组对照主图 + 每组的差异假设 + 复盘模板。当用户说「A/B 测试」「主图优化」「提点击率」「哪版更好」「换个版本试试」时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

面向电商运营人员与商品内容创作者，用于规划单变量主图 A/B 实验、生成对照图并记录预期效果，之后用复盘模板整理表现数据。点击率、转化率等投放数据需由用户填写。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected product or brand reference images are sent to the chosen image provider for generation.

Mitigation: Choose the intended provider, review inputs with --dry-run, and submit only images and prompts suitable for that provider.

Risk: Saving generated images to an existing path can overwrite files.

Mitigation: Use a dedicated output directory for each experiment.

Risk: A/B results can mislead when groups change multiple factors or exposure is too low.

Mitigation: Change one factor at a time, record the hypothesis before launch, and avoid drawing conclusions from small samples.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [Image provider CLI reference](references/provider-cli.md)
- [Platform Compliance skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/platform-compliance/skill.md)
- [Brand Kit skill](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/brand-kit/skill.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Files, Markdown]

**Output Format:** [Markdown experiment plan and review table, shell commands, and generated image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A/B groups vary one selected factor and include a rationale; the user supplies performance data for review.]

## Skill Version(s):

1.0.25 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
