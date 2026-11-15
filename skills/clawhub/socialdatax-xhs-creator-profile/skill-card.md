## Description:

用于小红书博主数据、小红书博主信息、账号资料、达人画像、主页信息和粉丝规模查询。覆盖 Xiaohongshu / XHS / RedNote creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

用户可使用此技能，按小红书博主的用户 ID、主页链接或分享文本查询账号资料和受众规模。它返回可用的个人资料字段，便于将资料事实与后续分析分开。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a changeable CLI package for local authentication and lookups, creating supply-chain risk.

Mitigation: Review the CLI package and version before installing or using the skill.

Risk: Profile identifiers or URLs are sent to SocialDataX for lookup.

Mitigation: Consider whether you are comfortable sharing the supplied identifiers or URLs with SocialDataX.

Risk: The security scan was partial because two local references could not be resolved, so its evidence is incomplete.

Mitigation: Review the skill and package before use, taking the incomplete scan evidence into account.

## Reference(s):


## Skill Output:

**Output Type(s):** [API Calls, JSON, Text]

**Output Format:** [JSON profile data with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields depend on the service response; keep profile facts separate from strategic interpretation.]

## Skill Version(s):

0.1.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
