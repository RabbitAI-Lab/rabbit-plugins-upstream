## Description:

Connects an agent to OurFamilyWizard co-parenting messages, calendars, expenses, and journal records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting matters use this skill to review OurFamilyWizard messages, calendar events, expenses, and journal entries, and to prepare shared updates with explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ambiguous requests could lead to access to private OurFamilyWizard records.

Mitigation: Require clear OFW context before accessing records.

Risk: Reading an unread message can irreversibly reveal when it was viewed.

Mitigation: Use allowMarkRead:false until the user approves changing its visible read status.

Risk: Shared writes can create co-parent-visible records.

Mitigation: Review the proposed change and obtain explicit user confirmation before making a shared write.

Risk: Credentials and cached family data are sensitive.

Mitigation: Protect local credentials and cached data, and use a reviewed server version.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw)
- [npm package](https://www.npmjs.com/package/ofw-mcp)
- [Publisher documentation](https://github.com/chrischall/ofw-mcp#write-protection-ofw_write_mode)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Natural-language summaries and structured OurFamilyWizard record data]

**Output Parameters:** [Messages, calendar events, expenses, journal entries, profile, and notifications]

**Other Properties Related to Output:** [May involve sensitive family records; some reads affect visible read status, and shared writes require explicit confirmation.]

## Skill Version(s):

2.20.6 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
