## Description:

一句话生成今日赛事全景报告，覆盖多类体育赛事的公开信息整理、阵型动画、球员聚焦、数据雷达和反诈骗提示，不做赛果判断或结论性建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmily741963](https://clawhub.ai/user/hmily741963)

### License/Terms of Use:

MIT-0

## Use Case:

Sports fans, commentators, educators, and agents use this skill to turn public match schedules and team/player context into structured viewing reports. It supports daily overviews, focus-match reports, source-tiered pre-match intelligence, and compliance checks that keep outputs informational rather than predictive.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can ask agents to gather broad web sports data and call sports APIs, which may introduce unverified or stale information.

Mitigation: Use source-tiering, prefer official or authoritative sources, keep timestamps visible, and run the audit workflow before presenting reports.

Risk: The skill can create or overwrite report files and refresh source JSON by default.

Mitigation: Use explicit output paths, review target file locations, and use no-write refresh mode when previewing changes.

Risk: API keys may be read from environment variables for optional live data sources.

Mitigation: Install only in environments where those credentials are intended for agent use, and avoid exposing keys in prompts, logs, or generated reports.

Risk: A generic URL fetch path may retrieve data from untrusted endpoints.

Mitigation: Use it only with trusted public sports-data endpoints and reject sources that cannot be verified.

Risk: Sports analysis content can be misread as outcome prediction or paid recommendation.

Mitigation: Keep outputs limited to public information organization, source labels, uncertainty, and anti-fraud warnings; do not provide outcome predictions or conclusion-style advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hmily741963/skills/sports-data-analysis)
- [Analysis methodology](references/analysis_methodology.md)
- [Data sources and source-tiering](references/data_sources.md)
- [Daily update workflow](references/daily_update_workflow.md)
- [Risk compliance and anti-fraud checklist](references/risk_compliance.md)
- [Professional analysis module guide](references/professional_analysis.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [HTML reports, Markdown summaries, JSON-backed report inputs, and concise agent guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update local report and JSON files; supports explicit output paths, refresh without writing, and audit checks before presentation.]

## Skill Version(s):

2.9.7 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
