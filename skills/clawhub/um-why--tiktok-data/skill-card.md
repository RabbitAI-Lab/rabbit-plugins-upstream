## Description:

以只读方式获取 TikTok 公开视频搜索结果、创作者作品和视频评论，并返回结构化 JSON。

This skill is ready for commercial/non-commercial use.

## Publisher:

[um-why](https://clawhub.ai/user/um-why)

### License/Terms of Use:

MIT

## Use Case:

内容创作者、品牌和研究人员可用它搜索 TikTok 公开视频、查看创作者作品并汇总视频评论，用于选题、竞品和舆情分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial, and some components were not fully inspected.

Mitigation: Review the remaining scripts and assess them before installing or providing a service token.

Risk: Requests send the configured API token to guaikei.com and results may include public creator or commenter usernames.

Mitigation: Use a token authorized for this service and follow applicable data handling rules before storing or publishing returned information.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/um-why/skills/tiktok-data)
- [Service and token setup](https://www.guaikei.com)
- [Parameter and output reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [Structured JSON envelope containing search results, creator posts, or video comments.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may be empty or contain fewer items than requested; available counts depend on the service plan.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
