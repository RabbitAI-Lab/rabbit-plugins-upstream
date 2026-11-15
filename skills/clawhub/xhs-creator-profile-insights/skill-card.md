## Description:

为品牌、MCN、内容运营和创作者提供小红书博主资料、创作者定位、粉丝规模判断和合作对象初筛支持。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Brands, MCNs, content teams, and creators use the skill to retrieve a Xiaohongshu creator's profile and visible account signals from an account ID, profile link, or shared profile text, then summarize the information for creator research or initial partnership screening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill repeatedly downloads and runs a changeable CLI release, creating supply chain risk; the security scan was partial, so its evidence is incomplete. Lookup details are also sent to SocialDataX.

Mitigation: Review the CLI release and run it in a controlled environment; provide only lookup details you are comfortable sending to SocialDataX.

## Reference(s):

- [SocialDataX AI and API key information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-creator-profile-insights)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured creator profile data summarized in concise Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports the profile fields returned for the selected account and separates visible facts from follow-up analysis.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
