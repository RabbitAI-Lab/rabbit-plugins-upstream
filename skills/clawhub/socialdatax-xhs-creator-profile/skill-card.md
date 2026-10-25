## Description:

用于小红书博主数据、小红书博主信息、账号资料、达人画像、主页信息和粉丝规模查询。覆盖 Xiaohongshu / XHS / RedNote creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, analysts, and marketing teams use this skill to look up Xiaohongshu/XHS/RedNote creator profile details and audience scale using a creator ID or profile link.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs and usage attribution are sent to SocialDataX.

Mitigation: Prefer a creator ID or clean profile link and avoid sending unnecessary share-text details.

Risk: API access requires a secret key, and lookups may consume credits.

Mitigation: Protect SOCIALDATAX_API_KEY and consider credit use before making a lookup.

Risk: CLI package updates can change behavior.

Mitigation: Consider pinning a reviewed CLI version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-creator-profile)
- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [Structured JSON profile data, with concise text summaries when presented to the user.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profile fields are included when available; strategic interpretation should be kept separate from profile facts.]

## Skill Version(s):

0.1.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
