## Description:

面向快手公开数据的数据分析技能，通过 GuaiKei 获取关键词搜索、博主作品列表和视频评论，并返回结构化结果用于内容调研、竞品分析和报告生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

内容创作者、运营和市场人员、数据分析师以及代理开发者可使用该技能查询快手公开视频、账号作品和评论数据，用于选题调研、竞品监控、评论洞察和后续报告生成。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou search terms or URLs and the GUAIKEI_API_TOKEN are sent to GuaiKei's API.

Mitigation: Use the skill only when that data sharing is acceptable for the task and environment.

Risk: Returned public comments or post data may be saved locally under logs.

Mitigation: Clean the logs directory when retained results should not remain on disk.

## Reference(s):

- [完整选项说明](references/options.md)
- [更新日志](references/changelog.md)
- [GuaiKei API service](https://www.guaikei.com)
- [Server-resolved GitHub provenance](https://github.com/why20261/kuaishou-detail-guaikei)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/kuaishou-detail-guaikei)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful command output includes status and results fields.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
