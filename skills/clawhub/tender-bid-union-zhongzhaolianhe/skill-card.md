## Description:

Analyzes tender and award data to summarize market trends, buyer and supplier rankings, and historical pricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhiliaobiaoxun](https://clawhub.ai/user/zhiliaobiaoxun)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts and procurement teams use this skill to search tender records, compare buyers and suppliers, and assess market size, trends, and historical bid prices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation may trigger vendor data queries and credentialed account checks without sufficiently clear user control.

Mitigation: Confirm the user's intended query before sending it to the vendor; limit account, contact, and update-related actions to what the task requires.

Risk: Automatic registration collects device characteristics and stores a new API key locally.

Mitigation: Request explicit consent before registration, explain the device data and local key storage, and offer the manual registration path if consent is declined.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhiliaobiaoxun/skills/tender-bid-union-zhongzhaolianhe)
- [Skill documentation](https://ai.zhiliaobiaoxun.com/docs/skill)
- [Market analysis API reference](references/api-market.md)
- [Automatic registration and privacy details](references/auto-register.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries may include source links, search filters, rankings, and monetary units.]

## Skill Version(s):

1.0.9 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
