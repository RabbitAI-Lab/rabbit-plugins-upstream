## Description:

TikTok 公开数据只读技能：关键词搜视频、博主作品、视频评论，输出 JSON，不登录不发布。触发词：TikTok、tiktok、抖音国际版、TikTok搜索、TikTok评论、TikTok博主。用户要查 TikTok 视频、评论、爆款选题、竞品监控、KOL 筛选或评论舆情时使用；抖音、小红书、快手、B站、微博、公众号不要用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT-0

## Use Case:

TikTok creators, brands, and research teams can retrieve public videos, creator posts, and video comments to support topic research, competitor monitoring, KOL screening, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan found no clear malicious behavior, but only 22 of 34 components were fully inspected; the benign verdict has medium confidence.

Mitigation: Review the package and available scan findings before installation; a benign verdict does not eliminate risk.

Risk: Queries send TikTok keywords or links to the external data service at guaikei.com.

Mitigation: Use public TikTok content and avoid including private or sensitive information in queries.

## Reference(s):

- [TikTok data service](https://www.guaikei.com)
- [Usage options](references/options.md)
- [FAQ and environment setup](references/faq.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON response envelope containing TikTok public search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes status, request metadata, and structured results; empty results and errors use documented status codes.]

## Skill Version(s):

1.1.3 (source: SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
