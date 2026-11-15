## Description:

通过关键词搜索 TikTok 公开视频、获取创作者公开作品并读取指定视频评论，返回结构化 JSON，供内容调研、竞品分析和舆情分析使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

TikTok 创作者、MCN、跨境营销团队、研究人员和 Agent 开发者可查询公开视频、创作者作品与视频评论，并将结果用于选题调研、竞品跟踪和内部舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign but partial: 20 of 32 components were fully inspected and 12 were only partially inspected.

Mitigation: Review the skill and its requested permissions before installation; treat the scan verdict as incomplete evidence.

Risk: Results can contain public creator names and other user information, and the documentation limits use to personal or team analysis.

Mitigation: Confirm authorization before external publication or commercial use, and redact usernames when sharing results.

Risk: Result timestamps use fixed Beijing-time formatting, which may be mistaken for the viewer's local time.

Mitigation: Interpret timestamps as Beijing time and convert them before comparing or reporting across time zones.

## Reference(s):

- [API access and support](https://www.guaikei.com)
- [Command options and plan limits](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON response envelope containing search results, creator posts, or video comments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may omit empty or zero-valued fields; monthly-token requests are limited to 30 search or post results and 40 comments.]

## Skill Version(s):

1.1.1 (source: SKILL.md frontmatter, package.json, server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
