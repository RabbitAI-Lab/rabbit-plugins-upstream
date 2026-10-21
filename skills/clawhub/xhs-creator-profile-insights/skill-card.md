## Description:

当用户需要做小红书博主画像、小红书博主信息、账号资料、创作者定位、粉丝规模判断或合作对象初筛时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, MCNs, content operators, and creators can use this skill to retrieve Xiaohongshu creator profile information, assess creator positioning and audience scale, and screen potential collaboration partners.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The selected account ID, profile link, or share text is processed by SocialDataX and may consume paid credits.

Mitigation: Tell users about the external processing and possible credit use; submit only the relevant account input and remove unrelated confidential text.

Risk: The skill relies on a third-party package and an API key.

Mitigation: Protect the SOCIALDATAX_API_KEY environment variable and prefer a reviewed fixed package version.

## Reference(s):

- [SocialDataX account and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-profile-insights)

## Skill Output:

**Output Type(s):** [JSON, Text, Guidance]

**Output Format:** [JSON creator profile data with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields may vary; distinguish observable account details from strategic assessments and suggest relevant follow-up questions.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
