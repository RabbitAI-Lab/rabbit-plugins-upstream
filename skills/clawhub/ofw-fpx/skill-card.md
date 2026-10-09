## Description:

Guides agents in accessing OurFamilyWizard messages, calendar, expenses, and journal through shell commands using a browser-acquired session token.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and developers with an authorized OurFamilyWizard account use this skill to read family records or prepare API requests for messages, events, expenses, and journal entries without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access a live OurFamilyWizard session token and sensitive family records.

Mitigation: Grant access only to trusted agents and authorized accounts; keep the token out of logs and shared outputs.

Risk: Writes and deletes affect the shared record immediately, without an enforced confirmation or dry run.

Mitigation: Manually verify the target and content before allowing any mutation; confirm message posts by retrieving the resulting message.

Risk: Opening an unread message can mark it as read.

Mitigation: Check message metadata before requesting details when preserving unread status matters.

## Reference(s):

- [ofw-fpx ClawHub release](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses may include sensitive family records; some reads can change message status.]

## Skill Version(s):

2.20.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
