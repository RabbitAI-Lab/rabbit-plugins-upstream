## Description:

查询抖音创作者主页资料、账号信息与粉丝规模。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

开发者和数据分析人员可使用抖音号、sec_user_id 或主页链接查询创作者资料，以了解账号基础信息和粉丝规模。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs are processed by SocialDataX using the user's API key, and lookups may consume credits.

Mitigation: Provide only the needed public identifier or profile link, omit unrelated private text, and monitor account credit usage.

Risk: Future package releases may differ from the supplied skill instructions.

Mitigation: Use a reviewed, pinned CLI version where possible; the security review covers the supplied instructions, not every future package release.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with concise textual reporting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only creator profile fields when available; distinguishes profile facts from strategic interpretation.]

## Skill Version(s):

0.1.20 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
