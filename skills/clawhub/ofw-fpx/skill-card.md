## Description:

Guides agents in accessing OurFamilyWizard messages, calendar, expenses, and journal from a signed-in browser session using shell commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with a signed-in OurFamilyWizard account use this skill to guide an agent in reading family records and preparing shell commands for messages, calendar events, expenses, attachments, and journal entries without the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Writes and deletions can change sensitive family-court records visible to a co-parent, with no built-in confirmation.

Mitigation: Manually review and approve each message send, deletion, upload, calendar edit, expense, or journal entry before execution.

Risk: Opening an unread message can mark it as read in OurFamilyWizard.

Mitigation: Confirm before fetching unread message details; use folder listings when read status must remain unchanged.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read or change live OurFamilyWizard account records.]

## Skill Version(s):

2.19.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
