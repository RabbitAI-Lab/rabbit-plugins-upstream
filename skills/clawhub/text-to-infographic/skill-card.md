## Description:

将对话或用户提供的内容组织成结构化信息图 plan（JSON），经布局语义与数值一致性校验后，用内置渲染器产出自包含静态 HTML 信息图。支持飞轮/鱼骨/桑基/金字塔/时间线/仪表盘六种 chart_family 布局。仅在用户明确请求信息图时调用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bonniegeng-max](https://clawhub.ai/user/bonniegeng-max)

### License/Terms of Use:

MIT-0

## Use Case:

需要把对话、文章或笔记整理为单页信息图的用户和内容创作者，可在明确请求时使用此 skill 生成可编辑 plan、检查布局和数值，再导出静态 HTML。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rendering overwrites an existing file at the selected output path.

Mitigation: Choose an unused output path or preserve the existing file before rendering.

Risk: Limited validation heuristics may miss inaccurate facts or numbers in a plan.

Mitigation: Review the plan against its source facts before sharing the infographic.

## Reference(s):

- [Text to Infographic on ClawHub](https://clawhub.ai/bonniegeng-max/skills/text-to-infographic)
- [Infographic plan schema](artifact/schemas/infographic-plan.schema.json)
- [Layout and fact validation rules](artifact/docs/校验规则规格-v0.1.md)

## Skill Output:

**Output Type(s):** [JSON, HTML, Validation report]

**Output Format:** [Structured infographic plan, validation findings, and a self-contained static HTML infographic.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports six layouts: flywheel, fishbone, sankey, pyramid, timeline, and dashboard. The HTML uses inline CSS and SVG, with no JavaScript or external requests.]

## Skill Version(s):

1.2.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
