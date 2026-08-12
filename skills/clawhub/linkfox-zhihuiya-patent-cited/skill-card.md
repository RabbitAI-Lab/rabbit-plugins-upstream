## Description:

从智慧芽（PatSnap）查询专利被引用数据，包括被引用次数和引用专利详情。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, patent analysts, and developers use this skill to query forward citation counts and cited-by patent details for one or more PatSnap/Zhihuiya patent IDs or publication numbers. It helps compare citation metrics and present factual citation data without valuation or investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can make paid LinkFox patent lookup calls and includes account onboarding and billing flows.

Mitigation: Require explicit user confirmation before paid calls or payment actions, especially when a query may consume credits dynamically.

Risk: The skill handles API keys and may ask the user to use SMS-based account access.

Mitigation: Treat printed API keys and SMS codes as secrets, and share SMS codes only when the user intends to create or access a LinkFox account.

Risk: Patent query results, payment QR artifacts, and session metadata may be persisted locally.

Mitigation: Review or disable local response and QR persistence before use with sensitive patent or business data.

Risk: The release security evidence marks the skill as suspicious because it combines patent lookup, login, payments, feedback reporting, and local storage.

Mitigation: Review and scan the skill before installation, and disable automatic feedback reporting if sensitive data may be exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-cited)
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai)
- [智慧芽-专利被引用 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)
- [LinkFox Skills](https://skill.linkfox.com/)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance, API calls]

**Output Format:** [Markdown tables and guidance with JSON API responses, saved JSON files, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes full API responses under the working directory and may print either full JSON or a compact summary depending on response size.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
