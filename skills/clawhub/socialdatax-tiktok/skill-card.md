## Description:

用于 TikTok 数据助手、视频和图文搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 TikTok content and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users can use the skill to research TikTok videos and image posts, inspect post details and comments, and look up creator profiles and post lists through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly invokes an unpinned CLI package, including during authentication, so the package could change between runs.

Mitigation: Review the package and pin an approved version before installing or using it.

Risk: Search terms and post or creator identifiers are sent to SocialDataX for data requests.

Mitigation: Use only query terms and identifiers you are comfortable sharing with the service.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-tiktok)

## Skill Output:

**Output Type(s):** [JSON, Research findings, Guidance]

**Output Format:** [Structured TikTok data and concise text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only post, comment, and creator data]

## Skill Version(s):

0.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
