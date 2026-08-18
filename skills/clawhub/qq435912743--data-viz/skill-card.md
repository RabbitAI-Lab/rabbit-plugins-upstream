## Description:

数据可视化。读 CSV/JSON 数据集，自动推断列类型，纯 Python 生成 SVG 图表（直方图/散点/柱状/折线）与 HTML 看板，无 matplotlib/pandas 依赖。当用户需要"画个图""数据可视化""做个图表""看分布""dashboard"时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to turn local CSV or JSON datasets into lightweight static chart dashboards in restricted environments where heavy plotting libraries are unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional learning component can keep persistent local records of operations, notes, errors, and preferences beyond a visualization run.

Mitigation: Review learner usage before installation, avoid recording sensitive dataset details in notes, and use scoped retention or deletion controls where local persistence is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/data-viz)
- [Publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python command examples and generated static SVG, HTML, and JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local histogram, scatter, and bar chart SVG files, an index.html dashboard, and summary.json statistics from CSV or JSON input.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
