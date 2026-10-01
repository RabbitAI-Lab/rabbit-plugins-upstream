## Description:

Guides agents in accessing OurFamilyWizard messages, calendar, expenses, and journal through browser-assisted token capture and shell-based API requests without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OFW users and developers can use the skill to read and manage family communications, events, expenses, and journal entries from a shell when the MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured OFW bearer token grants the agent and shell access to sensitive family records.

Mitigation: Use the token only in a trusted session, keep it out of logs and shared files, and stop using it when the task is complete.

Risk: Message sends, uploads, calendar and expense changes, journal entries, and deletions can change sensitive court-visible records without an enforced confirmation step.

Mitigation: Manually review recipients, record IDs, visibility, attachments, and complete payloads before each write or delete; confirm the result in OFW afterward.

Risk: Reading an unread message can mark it read, and opening the dashboard can update last-seen status.

Mitigation: Confirm that these account-visible effects are acceptable before fetching message details or dashboard status.

## Reference(s):

- [OFW request examples](references/requests.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [ContextMint Bridge extension](https://github.com/nullnet-app/contextmint-bridge)
- [Fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell command examples and JSON response projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requests act on the signed-in user's OFW account; writes can alter shared records.]

## Skill Version(s):

2.20.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
