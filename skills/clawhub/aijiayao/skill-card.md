## Description:

Helps AI agents find restaurants in China and, with permission, publish restaurant information and feedback through 爱佳肴 (Love Life).

This skill is ready for commercial/non-commercial use.

## Publisher:

[xianghui-shi](https://clawhub.ai/user/xianghui-shi)

### License/Terms of Use:

MIT-0

## Use Case:

People and restaurant owners use an AI agent to find nearby restaurants, check listing freshness, or publish and maintain restaurant listings and feedback with their consent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Restaurant searches may share a user's query and location with tutulife.cn.

Mitigation: Tell users before sharing location context and send only the details needed for the search.

Risk: Registration, listings, claims, reports, and feedback may publish information or associate it with a saved agent key.

Mitigation: Get the user's consent before writing, publish only authorized and accurate information, and keep the agent key in secure storage rather than chats or public files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/xianghui-shi/skills/aijiayao)
- [Merchant guide](https://tutulife.cn/merchant)
- [Service rules](https://tutulife.cn/rules)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Chinese-language restaurant recommendations and listing details; optional structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Listings may include freshness indicators and customer feedback; authorized actions can publish listings or feedback.]

## Skill Version(s):

1.4.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
