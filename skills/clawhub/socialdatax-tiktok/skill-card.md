## Description:

用于 TikTok 数据助手、视频和图文搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 TikTok content and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media researchers, creators, and other TikTok data users can search video and image posts, inspect post details and audience comments, and retrieve creator profiles and post lists through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: TikTok searches and links are sent to the SocialDataX service, and API credentials are used for data calls.

Mitigation: Share only searches and links you are comfortable sending to SocialDataX, and protect the SOCIALDATAX_API_KEY.

Risk: Broad pagination can increase credit usage, and an unpinned @latest package can change after review.

Mitigation: Set pagination limits and prefer a reviewed, pinned CLI version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-tiktok)

## Skill Output:

**Output Type(s):** [API Calls, JSON data, Analysis]

**Output Format:** [Structured TikTok data returned as JSON and readable summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results for posts, comments, replies, and creator profiles or post lists.]

## Skill Version(s):

0.1.3 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
