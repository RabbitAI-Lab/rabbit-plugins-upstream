## Description:

用于抖音达人数据、抖音达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Douyin creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

需要查询抖音创作者公开主页资料的用户可使用此技能获取账号基本信息、创作者定位和受众规模等资料。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile lookups send the supplied identifier or share text to SocialDataX and may consume paid credits.

Mitigation: Provide only a public profile identifier or the necessary share text, and account for possible credit charges before making a lookup.

Risk: A changing CLI release or exposed API key could affect lookup behavior or access to the service account.

Mitigation: Use a reviewed fixed CLI version instead of @latest and keep SOCIALDATAX_API_KEY protected.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with a concise natural-language summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields vary by account and response; report only fields returned.]

## Skill Version(s):

0.1.21 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
