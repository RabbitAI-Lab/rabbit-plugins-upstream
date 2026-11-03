## Description:

用于 TikTok 达人数据、TikTok 达人作品、TikTok KOL 作品列表、TikTok 博主视频列表、TikTok 网红近期发布、TikTok 内容调研和创作者内容分析。支持三大能力：(1) 关键词搜索 TikTok 视频，可按最多点赞、相关度排序，并按发布时间筛选；(2) 博主作品抓取，按主页链接或用户名批量获取公开作品列表，支持最新/最热排序；(3) 视频评论分析，按视频链接或作品 ID 获取评论内容、评论者与互动数据。无需登录账号，只读公开数据，输出结构化 JSON 供 AI 直接做选题、竞品监控与舆情分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and marketing analysts use this skill to retrieve public TikTok search results, creator post lists, and video comments as structured JSON for topic research, competitor monitoring, influencer screening, and social-listening analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the configured GUAIKEI_API_TOKEN and requested TikTok keywords, URLs, or IDs to a third-party provider.

Mitigation: Use a scoped provider token, keep GUAIKEI_API_TOKEN private, and review the provider's terms and privacy handling before installation.

Risk: Public comments and creator metadata can be retained in local JSON logs.

Mitigation: Delete temporary log files periodically when scraped public comments or creator metadata should not be retained locally.

Risk: The evidence notes publisher clarification is needed for IP-attribution/location wording.

Mitigation: Confirm the meaning and intended use of any IP-attribution or location fields before relying on them in reports or decisions.

## Reference(s):

- [Parameter options](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Creator posts request schema](assets/post_cli_req.schema.json)
- [Creator posts response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Guaikei provider site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes with status, request metadata, results, errors, and warnings; guidance may be returned as Markdown prose around command usage and analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are read from stdout; progress and logs are written to stderr, and local JSON logs may be saved under the system temporary directory.]

## Skill Version(s):

1.0.0 (source: server release evidence, frontmatter, package.json, changelog released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
