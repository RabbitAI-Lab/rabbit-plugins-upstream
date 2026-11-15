## Description:

TikTok高赞视频搜索工具。支持关键词获取TikTok实时高赞视频数据，助力创作者发现热门趋势、获取创作灵感。提供3个能力①关键词搜索（可按点赞/相关度排序、发布时间筛选）②博主作品获取，按主页链接或用户名批量获取公开作品列表，支持最新/最热排序 ③视频评论抓取，按视频链接或作品 ID 获取评论内容、评论者与互动数据，输出结构化 JSON（含作者、互动数据、标签、链接）。当用户需要搜TikTok视频、抓博主作品、看TikTok评论、做竞品/对标账号监控、短视频选题调研、评论舆情分析、热点追踪、爆款挖掘时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

TikTok creators, marketers, and researchers can search public videos by keyword, review a creator's public posts, and retrieve video comments for trend discovery, content planning, competitor research, and audience analysis. The skill returns structured data for an agent to summarize or compare.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found no AIG issues and rated the skill benign, but its medium confidence reflects partial inspection: 62.5% coverage, with 12 files only partly interpreted.

Mitigation: Review the skill and complete a full security scan before deployment; a benign verdict does not remove the coverage gap.

Risk: The API token is sent to the Guaikei service, and retrieved comments or creator details may contain personal information.

Mitigation: Keep GUAIKEI_API_TOKEN private, confirm the service's data handling fits your use, and redact usernames or other personal details before sharing results externally.

## Reference(s):

- [Guaikei TikTok data service](https://www.guaikei.com)
- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-video-search)
- [Options and limits](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [Structured JSON containing video search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public data may include creator names, engagement counts, tags, links, and comment text. The skill does not return video files.]

## Skill Version(s):

1.1.1 (source: frontmatter, changelog released 2026-11-04, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
