## Description:

抖音公开数据只读技能：关键词搜索视频/图文、博主作品与粉丝数据、视频评论、实时热榜，全部输出 JSON，不登录不发布。触发词：抖音搜索、抖音热搜、抖音热榜、抖音评论、博主作品、对标账号、sec_uid、aweme_id、douyin search、douyin hot、douyin comments。用户要查抖音视频、热搜、评论区、对标账号、竞品、选题或舆情时使用；小红书、快手、B站、微博、公众号不要用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营者与数据分析人员可检索抖音公开关键词内容、账号作品、评论和实时热榜，并将结构化结果用于选题、竞品对比及舆情跟踪。仅支持公开数据，不支持私密或隐藏内容。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and links are sent to a third-party API; the API may incur charges, and saved results can include profile and comment information.

Mitigation: Use only public-data queries, review provider charges, protect the API token, and secure saved logs; follow the documented internal-use restriction.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/um-why/skills/douyin-search-keyword)
- [Provider website](https://www.guaikei.com)
- [Usage options](references/options.md)
- [Demand mining guide](references/demand-mining.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator-post, comment, and hot-list results; timestamps use Beijing time.]

## Skill Version(s):

1.4.0 (source: evidence release, package.json, SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
