## Description:

通过关键词搜索 TikTok 公开内容、获取创作者作品和视频评论，帮助用户发现并评估潜在合作达人。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

营销人员、内容运营团队和研究人员可检索 TikTok 公开作品、创作者及评论，以筛选合作达人、分析内容表现和了解受众反馈。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The provider receives the access token and requested TikTok keywords, URLs or IDs.

Mitigation: Use a dedicated token and submit only queries you are comfortable sharing with the provider.

Risk: Saved JSON results in the system temp directory may expose public usernames and comments on shared machines.

Mitigation: Review and clear saved results after use, especially for sensitive research.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/tiktok-kol-discovery)
- [Provider and API information](https://www.guaikei.com)
- [Command options and output fields](references/options.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Structured JSON results and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator-post and comment results may include public usernames, engagement metrics and links; empty and error results are distinguished.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
