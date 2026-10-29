## Description:

当用户需要做小红书博主画像、小红书博主信息、账号资料、创作者定位、粉丝规模判断或合作对象初筛时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

品牌方、MCN、内容运营者和创作者可通过小红书账号 ID、主页链接或分享文本获取创作者资料与互动信号，用于账号画像和合作对象初筛。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookups may consume credits, and share text may include unrelated personal information.

Mitigation: Prefer an account ID or profile link and provide only information needed for the lookup; review API usage.

Risk: The lookup depends on a third-party package and runtime access.

Mitigation: Pin a reviewed package version and keep runtime access limited.

## Reference(s):

- [SocialDataX API information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-profile-insights)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [JSON creator profile data summarized in concise text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available profile fields vary; separate visible account facts from strategic interpretation.]

## Skill Version(s):

0.1.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
