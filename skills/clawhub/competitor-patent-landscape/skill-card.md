## Description:

竞争对手专利布局策略调研技能：给定竞争对手公司名称与技术领域，自动检索专利、识别重点布局、分析核心/外围策略，输出带有产品图可视化的HTML/PDF报告供企业IP团队和研发参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise IP teams, R&D engineers, and strategy analysts use this skill to investigate a competitor's patent activity in a technology area, identify core and peripheral patent coverage, and prepare evidence-backed patent landscape reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent landscape conclusions may be incomplete or misleading when the underlying patent, web, or analysis.json data is sparse, stale, or unverified.

Mitigation: Review the generated report against PatSnap and cited source data before using it for IP, R&D, or strategy decisions.

Risk: The workflow depends on intended PatSnap MCP or account access for live patent retrieval.

Mitigation: Confirm the PatSnap account, authorization, and configured MCP tools before running database-backed analysis.

Risk: Generated report files can be written to user-selected output paths.

Mitigation: Review or choose output filenames and paths before execution.

## Reference(s):

- [Workflow Guide](references/workflow_guide.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/competitor-patent-landscape)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [HTML or PDF patent landscape report, with supporting JSON analysis data and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include patent tables, market distribution, technology heatmaps, SVG product visualization, strategy summaries, and data-source notes.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
