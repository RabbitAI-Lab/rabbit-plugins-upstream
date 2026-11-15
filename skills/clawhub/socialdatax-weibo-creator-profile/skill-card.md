## Description:

用于微博创作者数据、微博用户资料、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Weibo creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve read-only Weibo creator profile information by user ID or profile URL. It reports available profile facts such as bio, verification, and audience counts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI release is unpinned and could change or be compromised.

Mitigation: Review the package and version before installing.

Risk: Lookup identifiers are sent to SocialDataX, and the scan evidence is incomplete.

Mitigation: Use only identifiers you are comfortable sending to SocialDataX, and account for the partial scan when reviewing the skill.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Guidance]

**Output Format:** [JSON profile data with concise textual summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Weibo profile fields when available; separates profile facts from strategic interpretation.]

## Skill Version(s):

0.1.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
