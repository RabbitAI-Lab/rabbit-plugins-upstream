## Description:

Helps an agent read and manage OurFamilyWizard messages, calendars, expenses, attachments, and journal entries for co-parenting tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with their OurFamilyWizard account can review co-parenting records and, with appropriate approval, draft or make changes to messages, calendar events, expenses, attachments, and journal entries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad co-parenting requests may expose sensitive records or lead to unintended account actions.

Mitigation: Invoke only for explicit OFW requests and protect account credentials.

Risk: Messages, shared uploads, calendar changes, expenses, deletions, and journal entries can affect sensitive co-parenting records.

Mitigation: Show the proposed action and obtain user confirmation before writing, sending, sharing, or deleting.

Risk: Opening an unread message can mark it read and expose a first-viewed time to the co-parent.

Mitigation: Warn before fetching unread messages and avoid marking them read without approval.

Risk: Cached or incomplete results can misstate whether a draft, message, or other record is current.

Mitigation: Check live status, freshness, and pagination before asserting the current state or retrying uncertain writes.

## Reference(s):

- [ClawHub OFW skill release](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package (linked in skill)](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown responses and setup examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-dependent results may require a fresh check before reporting current status.]

## Skill Version(s):

2.20.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
