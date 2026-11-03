## Description:

用于快手达人数据、快手达人信息、账号资料、创作者画像、主页信息和粉丝规模查询。覆盖 Kuaishou / Kwai creator profiles，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to find Kuaishou creators by keyword and retrieve profile information such as account details and audience scale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Profile search terms and identifiers are sent to SocialDataX.

Mitigation: Submit only the profile information needed for the requested lookup.

Risk: The external npm package was not included for code inspection.

Mitigation: Use a reviewed, fixed CLI version where practical.

Risk: API credentials or local credential files could be exposed, and API calls may incur credit charges.

Mitigation: Store the API key using supported secret storage, keep credential files out of version control, and consider API credit charges before making lookups.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-creator-profile)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Text or structured profile data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creator search candidates and profile facts, when available.]

## Skill Version(s):

0.1.22 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
