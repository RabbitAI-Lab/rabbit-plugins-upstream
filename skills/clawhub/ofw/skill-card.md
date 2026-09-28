## Description:

Helps an agent access OurFamilyWizard co-parenting messages, calendars, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People managing co-parenting arrangements use this skill to review and manage their OurFamilyWizard messages, events, expenses, and journal entries through an agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad co-parenting requests may trigger access to sensitive legal records without an explicit request to open OFW.

Mitigation: Use only for explicit OFW tasks and confirm account access with the user before reading sensitive records.

Risk: Sending messages, changing shared events or expenses, deleting records, and sharing attachments can affect a co-parenting record.

Mitigation: Show the proposed change and obtain explicit approval before each consequential write; verify uncertain outcomes before retrying.

Risk: Reading unread messages or checking notifications can change viewed or last-seen status.

Mitigation: Warn the user before reads that change status and avoid background checks.

Risk: Cached message and draft information may be incomplete or out of date.

Mitigation: Verify current status and completeness before reporting counts or claiming a draft remains unsent.

Risk: Configuring OFW credentials gives the connected agent access to private account data.

Mitigation: Configure credentials carefully and restrict use to intended OFW tasks.

## Reference(s):

- [ClawHub ofw release](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain-text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain sensitive co-parenting records and proposed messages.]

## Skill Version(s):

2.19.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
