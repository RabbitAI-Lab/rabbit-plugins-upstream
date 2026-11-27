## Description:

抖音高赞视频搜索工具。支持关键词获取抖音实时高赞视频数据，助力创作者发现热门趋势、获取创作灵感。支持五大能力：(1) 关键词搜索视频/图文，可按点赞数、发布时间、视频时长、内容类型筛选排序；(2) 实时热榜查询，获取抖音热搜词条与热度数据；(3) 单条作品详情，按视频链接或 aweme_id 获取文案、互动与作者；(4) 博主作品抓取，按主页链接或 sec_uid 获取公开作品列表；(5) 视频评论分析，按视频链接或 aweme_id 获取评论内容与互动数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video creators, marketers, and analysts use this skill to find public Douyin videos, creators, trending topics, post details, and comments for content planning and trend or audience analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious, citing broad routing, keyword-based account discovery beyond declared capabilities, and partial file analysis.

Mitigation: Review the source and requested command path before installation or use, and limit execution to the user's requested public-data query.

Risk: The scan notes limited disclosure that inputs may be sent to a third-party API; the skill documentation identifies Guaikei as the service receiving queries.

Mitigation: Tell the user before execution that search terms or Douyin links are sent to Guaikei, and use only inputs approved for that transmission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-video-search)
- [Guaikei service](https://www.guaikei.com)
- [Output contract](references/contract.md)
- [Options and filters](references/options.md)
- [Error handling](references/errors.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON results with a concise natural-language summary for the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are available for search, user lookup, creator posts, work details, comments, and hot lists; most query results are also saved under the skill directory's logs/.]

## Skill Version(s):

1.5.0 (source: frontmatter, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
