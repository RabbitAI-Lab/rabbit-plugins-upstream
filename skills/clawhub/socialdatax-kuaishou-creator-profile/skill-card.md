## Description:

用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询，覆盖 Kuaishou / Kwai creator profiles。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向需要研究快手创作者的外部用户和开发者，用于按关键词发现账号，或按用户 ID、主页链接查询创作者资料与受众规模。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The automatically installed package is unpinned and could change between releases.

Mitigation: Review the package and its version before running it, especially in environments with access to credentials or personal files.

Risk: Creator search terms and profile identifiers are sent to SocialDataX for lookup.

Mitigation: Submit only search terms and profile identifiers you are comfortable sharing with SocialDataX.

Risk: The security scan was partial because some referenced paths were unresolved, so its coverage is incomplete.

Mitigation: Review unresolved referenced files and scan the complete release contents before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Guidance]

**Output Format:** [JSON profile data with concise text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookup; returned profile fields depend on the available account data.]

## Skill Version(s):

0.1.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
