## Description:

技术主题洞察报告全流程生成Skill。覆盖选题→采集→HTML编写→质检→发布五阶段SOP，内置六维信源框架、专利高风险排查、避坑经验与自动化质检脚本。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent, strategy, and market intelligence teams use this skill to produce HTML technology insight reports with a fixed ten-section structure, multi-source research workflow, patent risk screening, and release quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may require the agent to use a configured PatSnap MCP account and web research tools.

Mitigation: Install only after confirming the agent is allowed to access those tools and the associated account data.

Risk: Generated patent risk, FTO, and avoidance content can be incomplete or legally unreliable if used as final advice.

Mitigation: Treat generated legal-risk analysis as preliminary technical research and have a professional patent lawyer review conclusions before relying on them.

Risk: Patent landscape or white-space conclusions can be misleading if based on partial searches.

Mitigation: Follow the bundled full-search specification, record matched_total values, and validate cross-section consistency before publishing a report.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/tech-insight-report)
- [PatSnap Open Platform](https://open.zhihuiya.com/)
- [Chart.js 4.4.0 CDN](https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js)
- [HTML skeleton template](references/html_skeleton_template.html)
- [Quality checklist](references/quality_checklist.md)
- [Section 4 exhaustive patent search specification](references/s4_exhaustive_search_spec.md)
- [Cross-section sync table template](references/sync_table_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and HTML report guidance with supporting Python quality-check commands and templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces structured report instructions and validation workflows; final reports should be reviewed before publication.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
