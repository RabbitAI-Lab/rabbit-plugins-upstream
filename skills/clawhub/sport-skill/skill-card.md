## Description:

一句话生成今日赛事全景报告，覆盖多类球类运动，通过阵型动画、球员聚焦和数据面板整理公开赛事信息；它不做赛果判断，只做信息整理、可视化和反诈骗提示。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users, sports fans, commentators, and educators use this skill to turn public match data into visual pre-match or daily sports reports. It is intended for legal sports information review, tactical learning, and source-aware discussion, not result prediction or outcome advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can fetch public web or API data, including a generic URL fetch path.

Mitigation: Use trusted sports data sources and explicit input URLs only; avoid generic --url fetches for untrusted locations.

Risk: The skill can write reports to desktop paths and mutate JSON files when refresh, fix, or write modes are enabled.

Mitigation: Use explicit input and output paths, review generated reports before sharing, and run mutation modes only on reviewed copies of data files.

Risk: The skill can read sports-provider API keys from environment variables.

Mitigation: Keep API keys scoped to the intended provider, do not hard-code them in skill files, and rotate keys if report generation runs in shared environments.

Risk: Daily automation or recurring report generation can run more often than expected.

Mitigation: Enable automation only when recurring runs are intended, and monitor generated files and schedules.

Risk: Generated reports may mix live, verified sample, and demo data if current data is unavailable.

Mitigation: Check live/example badges, source tiers, timestamps, and audit output before relying on a report as current information.

Risk: Generated browser reports can store feedback locally.

Mitigation: Avoid entering sensitive information in report feedback and clear browser storage or review exported feedback JSON before sharing.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/sport-skill)
- [Analysis Methodology](references/analysis_methodology.md)
- [Data Sources and Tiering](references/data_sources.md)
- [Daily Update Workflow](references/daily_update_workflow.md)
- [Professional Analysis Metrics](references/professional_analysis.md)
- [Risk Compliance](references/risk_compliance.md)
- [Report Template](assets/report_template.md)

## Skill Output:

**Output Type(s):** [text, markdown, HTML files, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands; generated HTML reports and JSON data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write reports to desktop paths, update JSON inputs, and store browser feedback locally when generated reports are viewed.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 2.9.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
