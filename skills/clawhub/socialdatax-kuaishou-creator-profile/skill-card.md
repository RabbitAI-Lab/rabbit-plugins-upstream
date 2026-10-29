## Description:

用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要快手创作者资料的用户，用于按关键词发现账号，并查询创作者主页信息与受众规模。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default CLI command runs the latest npm package with the agent's permissions; the external package was not audited here.

Mitigation: Pin a reviewed package version when predictable code is needed.

Risk: API calls use the configured SocialDataX API key and may consume service credits.

Mitigation: Use an API key intended for this integration and consider service-credit costs.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON creator search and profile data, with text summaries when reported to the user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile fields vary with the available API response.]

## Skill Version(s):

0.1.21 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
