## Description:

快手舆情监测助手。针对任意关键词获取快手作品数据、详情、互动数据、评论数据，基于快手实时数据，综合分析舆情健康、情感占比、负面信息、事件时间、热度排行、竞品口碑对比与风险建议等，进行分析并输出舆情报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, marketers, content teams, and agents use this skill to collect public Kuaishou video, creator, and comment data for sentiment monitoring, competitor research, creator screening, topic discovery, and report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile URLs, video URLs, request metadata, and the API token are sent to the disclosed Guaikei service.

Mitigation: Use the skill only for data you are comfortable sending to Guaikei, keep GUAIKEI_API_TOKEN scoped and private, and rotate the token if exposure is suspected.

Risk: Generated logs may contain sensitive monitoring targets, competitor research, or collected comment data.

Mitigation: Review the local logs directory after runs and delete or protect files that contain sensitive analysis targets or collected comments.

Risk: Returned public data and sentiment outputs can be incomplete, stale, or misleading if treated as a final business judgment.

Mitigation: Use the JSON output as source material for human-reviewed analysis and confirm important claims against the original public Kuaishou content before action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/kuaishou-sentiment-monitor)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON results with concise Markdown summaries and command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; runtime commands may save result logs locally.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
