## Description:

Helps an agent access and manage OurFamilyWizard co-parenting messages, calendar events, expenses, and journal entries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People using an agent with their OurFamilyWizard account can review co-parenting records and, with approval, compose messages or update shared calendars and expenses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive co-parenting records and account credentials.

Mitigation: Connect only an intended account, protect credentials, review the package before installation, and choose the narrowest available deployment mode.

Risk: Messages, deletions, shared expenses, calendar changes, and uploads can affect other people or create lasting records.

Mitigation: Show the proposed action and require explicit user confirmation before each write or deletion.

Risk: Some reads can mark messages as read or update last-seen status; cached results may be stale.

Mitigation: Warn before state-changing reads and check live status before reporting current account state.

## Reference(s):

- [OFW skill on ClawHub](https://clawhub.ai/chrischall/skills/ofw)
- [ofw-mcp npm package](https://www.npmjs.com/package/ofw-mcp)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Text]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May surface sensitive account records and propose account changes.]

## Skill Version(s):

2.20.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
