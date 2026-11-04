## Description:

用于 TikTok 数据助手、视频和图文搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 TikTok content and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and marketing teams use the skill to research TikTok videos and image posts, inspect post details and comments, and review creator profiles and post lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and pasted share text are sent to a third-party data service, and requests may consume paid credits.

Mitigation: Use public research inputs only, omit confidential material, and check expected credit use before requesting data.

Risk: The skill relies on an external npm CLI package that was not included in the security review.

Mitigation: Use a reviewed, fixed CLI version with limited local access, and keep the API key in a secret store outside version control.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-tiktok)
- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Structured TikTok data and concise text guidance; Bash CLI examples when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; API requests may consume paid credits.]

## Skill Version(s):

0.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
