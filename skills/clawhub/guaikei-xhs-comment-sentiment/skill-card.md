## Description:

返回结构化 JSON 的小红书公开数据，支持关键词搜索、笔记详情、评论获取和博主作品监控，便于后续做选题汇总、高赞对比、评论聚类和报告生成。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, brand marketers, analysts, and agent developers use this skill to retrieve structured Xiaohongshu public content and comment data for content research, competitor monitoring, KOL screening, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords, note or profile URLs, and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when this third-party data transfer is acceptable, verify the token source, and keep GUAIKEI_API_TOKEN out of chats, shell history, and logs.

Risk: The skill can automatically save full Xiaohongshu result data under logs/.

Mitigation: Review local log retention needs and delete generated logs when the retrieved Xiaohongshu data is no longer needed.

Risk: The scanner verdict is suspicious because of third-party API submission and local result retention.

Mitigation: Review the skill before installing and run it only in an environment where those behaviors are approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-xhs-comment-sentiment)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Structured JSON on stdout, with concise Markdown or text summaries when the agent explains results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require GUAIKEI_API_TOKEN and may save full result JSON files under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact metadata reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
