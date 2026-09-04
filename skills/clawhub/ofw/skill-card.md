## Description:

This skill helps an agent access and manage OurFamilyWizard (OFW) co-parenting messages, calendar events, shared expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to work with OFW co-parenting records, including inbox and sent messages, calendar events, shared expenses, and journal entries. It is most appropriate when the user explicitly asks the agent to inspect or update OFW data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent persistent access to sensitive co-parenting records.

Mitigation: Install only in a dedicated private environment and protect configured OFW credentials.

Risk: The trigger scope is broad enough to activate on many OFW or co-parenting requests.

Mitigation: Require explicit user intent before accessing OFW data and avoid silent background use.

Risk: Some actions can send, delete, or write records in OFW.

Mitigation: Require explicit confirmation before any send, delete, expense, calendar, or journal write.

Risk: Some reads can change OFW-visible state, such as last-seen or message read status.

Mitigation: Warn the user before calls that may update visibility or mark unread content as read.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)
- [ofw-mcp repository link from skill documentation](https://github.com/chrischall/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, account setup guidance, and confirmation steps for sensitive OFW actions.]

## Skill Version(s):

2.14.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
