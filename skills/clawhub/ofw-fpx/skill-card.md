## Description:

Access OurFamilyWizard messages, calendar, expenses, and journal from a shell with the fpx CLI to capture a signed-in web app bearer token, then use curl to call the REST API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve and modify OurFamilyWizard records from shell scripts when they prefer direct fpx and curl workflows over running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables shell access with a signed-in OurFamilyWizard bearer token, which can expose sensitive family-court records to the running agent or shell session.

Mitigation: Use the skill only in trusted sessions, avoid logging tokens or responses, and re-capture tokens only when necessary.

Risk: POST, PUT, DELETE, upload, and message-detail read operations may create visible, permanent, legally sensitive account changes without built-in confirmation.

Mitigation: Add an external review and confirmation step before mutating commands, and re-fetch newly posted messages to confirm the intended content landed.

## Reference(s):

- [Endpoint request reference](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/ofw-fpx)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes command patterns for authenticated API reads, writes, uploads, deletes, retry handling, and write confirmation checks.]

## Skill Version(s):

2.15.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
