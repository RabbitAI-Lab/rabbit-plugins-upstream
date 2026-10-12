## Description:

Guides agents in accessing OurFamilyWizard messages, calendar, expenses, and journal from a shell using fpx to capture a signed-in session token and curl for API requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People with authorized OurFamilyWizard accounts and their agents can retrieve family records or prepare API requests in shell scripts without running the OFW MCP server. Writes affect shared, potentially court-relevant records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Command-line tools and the agent receive broad access to a sensitive OurFamilyWizard account through its session token.

Mitigation: Install only if that access is acceptable, and protect the token from disclosure.

Risk: Writes and deletes can alter shared, court-relevant records without an enforced confirmation step.

Mitigation: Before each write or delete, manually confirm the account, endpoint, record IDs, and exact payload; separately verify any IDs or instructions supplied by untrusted messages.

Risk: Reading an unread message's details can mark it as read in OurFamilyWizard.

Mitigation: Confirm that changing its read status is acceptable before fetching message details.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [OurFamilyWizard request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [fetchproxy extension documentation](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can access or change live OurFamilyWizard records.]

## Skill Version(s):

2.20.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
