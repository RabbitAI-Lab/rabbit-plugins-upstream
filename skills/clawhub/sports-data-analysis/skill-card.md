## Description:

一句话生成今日赛事全景报告，覆盖足球、篮球、NBA、英超、中超、欧冠等运动，将公开赛事信息整理成阵型动画、球员聚焦、数据雷达和反诈骗提示，不做赛果判断。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External sports fans, commentators, educators, and agents use this skill to turn public match schedules, team context, player information, and source-graded pre-match notes into structured viewing reports. The skill supports lawful sports information review and visualization, while avoiding result prediction or conclusive recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may fetch public web or API data, including through user-controlled data-gathering workflows.

Mitigation: Use only trusted public sports and weather sources, avoid generic fetches against untrusted or internal URLs, and retain source labels and timestamps in generated reports.

Risk: Report generation and refresh workflows can write HTML reports and rewrite JSON input files.

Mitigation: Review target paths before execution, use no-write workflows when preserving source data matters, and run audit checks before presenting generated reports.

Risk: Optional live data collection may read API keys from environment variables and can produce thin or sample data when keys or sources are unavailable.

Mitigation: Scope API keys to the intended public data providers, regenerate live data before use, and treat bundled live_today data as sample or verified snapshot data unless freshly refreshed.

Risk: The security summary flags biased avatar-generation logic in generated visual elements.

Mitigation: Review generated player avatar metadata and visuals before publication, and use the bundled avatar and audit self-checks to catch inconsistent or inappropriate outputs.

Risk: Sports information can be misread as result prediction or wagering advice.

Mitigation: Keep outputs framed as public information organization and visualization, preserve anti-fraud warnings, and reject requests for guaranteed results, paid picks, or conclusive betting-style recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/sports-data-analysis)
- [赛事信息整理方法（三步法）](references/analysis_methodology.md)
- [每日信息更新工作流（refresh）](references/daily_update_workflow.md)
- [数据源与分级采集规范](references/data_sources.md)
- [合规红线与反诈骗清单](references/risk_compliance.md)
- [报告专业指标说明（信息维度）](references/professional_analysis.md)
- [单场分析报告输入模板（match.json）](assets/report_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, structured JSON inputs, and generated HTML reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be written as local HTML files; refresh and audit commands can update JSON inputs unless no-write or review workflows are used.]

## Skill Version(s):

2.9.9 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
