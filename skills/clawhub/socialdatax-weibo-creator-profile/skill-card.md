## Description:

用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to retrieve Weibo creator profile details and audience scale by user ID or profile URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookups send supplied Weibo IDs or profile URLs and usage attribution to SocialDataX, and may consume paid credits.

Mitigation: Confirm the lookup input, protect SOCIALDATAX_API_KEY, and check account credits before making requests.

Risk: The downloaded package runs with the agent process's permissions and may change when updated.

Mitigation: Review the package and use a fixed, reviewed package version where practical.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with platform, tool, arguments, and available creator fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields depend on the returned Weibo data.]

## Skill Version(s):

0.1.20 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
