## Description:

Provides shell-based access to OurFamilyWizard messages, calendar events, expenses, journal entries, and files using a signed-in account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

OurFamilyWizard users can use this skill to read and manage family communication and coordination records from shell workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Messages and other family records can be changed or exposed to a co-parent without a built-in confirmation step.

Mitigation: Require explicit approval before each send, deletion, upload, privacy change, or financial-record edit.

Risk: The signed-in session token can provide access to sensitive family records.

Mitigation: Protect the token and revoke browser pairing when finished.

Risk: Opening an unread message can mark it as read, and dashboard access updates last-seen status.

Mitigation: Check whether those account-visible effects are acceptable before fetching message details or the dashboard.

Risk: An incomplete expense update can erase fields from the existing record.

Mitigation: Retrieve the current expense first and include every field that should remain unchanged.

Risk: Dependency releases and live API behavior are not verified by the supplied security review.

Mitigation: Verify dependency versions and extension releases, and confirm behavior before relying on consequential updates.

## Reference(s):

- [OurFamilyWizard request examples](references/requests.md)
- [OFW FPX ClawHub release](https://clawhub.ai/chrischall/skills/ofw-fpx)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)
- [fetchproxy extension reference](https://github.com/chrischall/fetchproxy#extension)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands and guidance for reading and changing OFW records and files.]

## Skill Version(s):

2.26.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
