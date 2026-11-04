## Description:

用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

创作者研究者和社媒分析人员可查询微博账号的基础资料与受众规模，并查看可用的简介、认证、粉丝、关注和互动字段。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile lookups send the supplied Weibo ID or profile URL and usage attribution to SocialDataX and may consume credits.

Mitigation: Use a reviewed, pinned CLI version or an existing authenticated MCP connection, and keep the API key in a supported secret store.

Risk: The external CLI implementation and future releases were not covered by the security review.

Mitigation: Prefer a reviewed, pinned CLI version and reassess the external implementation before changing versions.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON profile data with a concise text report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields depend on the data returned for the Weibo account.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
