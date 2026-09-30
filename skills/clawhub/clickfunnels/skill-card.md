## Description:

Helps agents manage ClickFunnels contacts, products, orders, courses, forms, and webhooks through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and marketing teams use this skill to have an agent retrieve and, with approval, update ClickFunnels business records or set up workflows through their authorized connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes can modify or delete business records.

Mitigation: Confirm the target record and intended effect with the user before each write.

Risk: Webhooks and trigger destinations can create ongoing data flows.

Mitigation: Require separate approval for each destination and review what data it receives before enabling it.

Risk: Hosted functions can run ClickFunnels actions automatically.

Mitigation: Review function code, permissions, and schedule or event source before deployment.

## Reference(s):

- [ClickFunnels skill release](https://clawhub.ai/byungkyu/skills/clickfunnels)
- [Maton homepage](https://maton.ai)
- [ClickFunnels API reference](https://developers.myclickfunnels.com/reference)
- [ClickFunnels webhooks overview](https://developers.myclickfunnels.com/docs/webhooks)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Scheduled trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access and a user-authorized Maton connection; writes and new automations require user approval.]

## Skill Version(s):

1.2.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
