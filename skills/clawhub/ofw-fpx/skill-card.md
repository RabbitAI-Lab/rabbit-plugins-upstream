## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from a shell by using the fpx CLI to capture a signed-in browser session token and curl the OFW REST API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve and update OurFamilyWizard records from scripts or shell workflows when the MCP server is not installed or desired. It is intended for direct API work with messages, calendar events, expenses, journal entries, and attachments after the user has an authenticated OFW browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a captured OFW bearer token from an authenticated browser session, which can expose sensitive family-court records if mishandled.

Mitigation: Use the skill only in a trusted shell, avoid command tracing or token logging, and re-capture the token only from a signed-in OFW tab you control.

Risk: Write and delete examples affect live OurFamilyWizard records and may be permanent or visible to a co-parent.

Mitigation: Review every command, verify record IDs and payloads before execution, and re-fetch records after message writes to confirm the expected result.

Risk: The setup installs an unpinned globally available fpx helper.

Mitigation: Prefer a pinned or isolated fpx installation when possible and install only if the browser pairing access is acceptable for the environment.

## Reference(s):

- [OurFamilyWizard request examples](artifact/references/requests.md)
- [ClawHub skill page: ofw-fpx](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes read and write API examples that require a captured OFW bearer token; users should verify identifiers and command effects before execution.]

## Skill Version(s):

2.16.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
