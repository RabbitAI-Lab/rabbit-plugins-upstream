## Description:

小红书内容灵感聚合技能，覆盖选题灵感全链路：关键词爆款笔记搜索、批量获取作品数据、每日爆款 TOP50、低粉爆款挖掘、账号榜单和对标账号推荐。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanyi-github](https://clawhub.ai/user/yuanyi-github)

### License/Terms of Use:

MIT-0

## Use Case:

Xiaohongshu creators, content operators, brands, and MCN teams use this skill to find viral topic ideas, collect recent note data, track creator and content leaderboards, and identify benchmark accounts for content planning or partnership decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a RedFox API key and handles credentials during normal operation.

Mitigation: Provide the key through a scoped secret or temporary environment variable, confirm reset and revocation options, and avoid hard-coding or printing the key in prompts, code, logs, or report files.

Risk: Credential discovery may inspect shell startup files, and setup guidance may encourage permanent credential writes.

Mitigation: Do not allow broad shell profile scanning unless intended; prefer process-scoped environment variables or a managed secret store for agent runs.

Risk: The security evidence calls out TLS-verification and HTML-escaping issues before use with sensitive accounts or data.

Mitigation: Fix TLS verification and HTML escaping before using the skill with sensitive accounts, private data, or privileged network contexts.

Risk: Generated HTML reports are active web pages and may load third-party scripts.

Mitigation: Open generated reports only in a trusted browser context, review report contents before sharing, and treat exported HTML as executable web content.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanyi-github/skills/xiaohongshu-inspiration)
- [Xiaohongshu Content Inspiration Expert README](README.en.md)
- [小红书热门笔记数据格式说明](references/m1_hot_article_format.md)
- [小红书每日爆款笔记核心工作流程](references/m3_core_workflow.md)
- [小红书低粉爆款笔记 API 接口规范](references/m4_api_spec.md)
- [小红书榜单 API 接口文档](references/m5_api_docs.md)
- [小红书账号综合评分规则](references/m5_score_rules.md)
- [RedFox Hub](https://redfox.hk)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown responses, JSON data, shell command invocations, and generated CSV or HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Xiaohongshu note tables, account leaderboard tables, benchmark account summaries, API-derived JSON, cache files, Excel-compatible CSV exports, and browser-viewable HTML reports.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
