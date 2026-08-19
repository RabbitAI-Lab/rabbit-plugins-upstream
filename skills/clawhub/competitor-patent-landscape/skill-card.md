## Description:

竞争对手专利布局策略调研技能：给定竞争对手公司名称与技术领域，自动检索专利、识别重点布局、分析核心/外围策略，输出带有产品图可视化的HTML/PDF报告供企业IP团队和研发参考。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Enterprise IP teams, R&D engineers, and strategy analysts use this skill to investigate a competitor's patent position in a technology area, identify core and peripheral patents, and prepare evidence-backed strategy recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent counts, patent-family data, and strategy conclusions may be incomplete or misleading if source searches, PatSnap access, or web evidence are unavailable or stale.

Mitigation: Treat generated reports as analytical drafts and verify patent counts, family data, links, and legal conclusions against authoritative patent databases and qualified IP review.

Risk: Untrusted or script-like content in analysis JSON could be carried into generated HTML reports.

Mitigation: Review and sanitize report input data before rendering, and avoid feeding untrusted HTML or script-like content into the report JSON.

## Reference(s):

- [Competitor Patent Landscape Workflow Guide](references/workflow_guide.md)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [ClawHub Skill Page](https://clawhub.ai/yuanzhian-patsnap/skills/competitor-patent-landscape)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [HTML or PDF report, with structured analysis data and optional shell commands for report generation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include patent statistics, core and peripheral patent analysis, market distribution, product SVG visualization, and R&D recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
