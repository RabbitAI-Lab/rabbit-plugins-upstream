## Description:

Guides agents to access OurFamilyWizard messages, calendar, expenses, and journal through shell commands using a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents working with an authorized OurFamilyWizard account can use this skill to retrieve family records and prepare or execute API requests without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A live session token grants access to sensitive, shared family-court records.

Mitigation: Use only an account you are authorized to access; protect the token and avoid exposing it in logs or shared shells.

Risk: Writes and deletes can change shared records immediately without built-in confirmation or a dry run.

Mitigation: Review every request payload, identifier, recipient, visibility setting, and file path before execution; add explicit confirmation for publication or deletion.

Risk: Opening an unread message by ID can mark it as read.

Mitigation: Review message lists first and open unread messages only when the read-state change is acceptable.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)
- [ofw-fpx on ClawHub](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands and API request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests may read, publish, or delete account records.]

## Skill Version(s):

2.20.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
