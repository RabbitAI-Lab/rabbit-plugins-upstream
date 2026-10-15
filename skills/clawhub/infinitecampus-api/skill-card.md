## Description:

Guides agents in using curl to access a district's Infinite Campus parent portal for student grades, attendance, assignments, schedules, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized developers use this skill to query their district's Campus Parent portal directly with curl when an MCP server is unavailable or unnecessary.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and session cookies can expose sensitive student information.

Mitigation: Keep credentials in a secret store or environment variables, and protect or delete the cookie jar after use.

Risk: Document downloads can overwrite an existing report-card.pdf file.

Mitigation: Choose and confirm a safe output path before downloading documents.

Risk: Fetching a message body may mark the message as read in some districts.

Mitigation: Confirm before retrieving message bodies.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires district-specific portal settings and authorized parent credentials.]

## Skill Version(s):

3.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
