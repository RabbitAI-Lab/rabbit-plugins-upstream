## Description:

用于小红书博主数据、小红书博主信息、账号资料、达人画像、主页信息和粉丝规模查询。覆盖 Xiaohongshu / XHS / RedNote creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts can look up Xiaohongshu / XHS / RedNote creator profiles by user ID or profile link to review account basics, creator positioning, and audience scale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key could be exposed through chat or version control.

Mitigation: Keep the key in the execution environment's secret configuration and out of chat and version control.

Risk: Profile IDs or links are sent to SocialDataX as lookup inputs.

Mitigation: Send only the profile ID or link needed for the requested lookup.

Risk: The external CLI implementation and future releases were unavailable for review.

Mitigation: Prefer a reviewed, pinned CLI version.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-profile)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON profile data with a concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile facts are separated from strategic interpretation.]

## Skill Version(s):

0.1.18 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
