## Description:

体育赛事信息可视化与观赛辅助助手，聚合球队和球员资料、战术风格、赛事情报、数据可视化和自查结果，生成面向观赛参考的赛事报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect public sports-event information, structure it into readable comparisons, and generate sports viewing reports. It is intended for legal viewing, research, commentary preparation, and sports-data education, not outcome prediction or conclusive advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may browse the web and write report files to the user's Desktop.

Mitigation: Run it with least-privilege workspace access and review generated file paths before sharing or retaining reports.

Risk: Refresh, audit, or fix workflows may modify JSON files.

Mitigation: Keep source data under version control or make backups, and review diffs after write-enabled workflows.

Risk: An arbitrary URL fetch option can be risky with untrusted or internal URLs.

Mitigation: Use only public sports-data URLs and avoid internal, private, or untrusted endpoints.

Risk: Sports reports can be misunderstood as predictions or advice.

Mitigation: Preserve source labels, freshness notices, and the stated boundary that the skill organizes public information without outcome judgments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/hmily741963/skills/sport-skill)
- [Analysis Methodology](references/analysis_methodology.md)
- [Daily Update Workflow](references/daily_update_workflow.md)
- [Data Sources](references/data_sources.md)
- [Risk Compliance](references/risk_compliance.md)
- [Professional Analysis](references/professional_analysis.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance, shell commands, JSON inputs, and generated HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates sports-event report files and may update JSON data files during refresh, audit, or fix workflows.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
