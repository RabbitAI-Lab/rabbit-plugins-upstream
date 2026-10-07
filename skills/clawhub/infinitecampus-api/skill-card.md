## Description:

Guides authorized users through querying their district's Infinite Campus parent portal for student records using curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and authorized assistants use this skill to retrieve grades, attendance, schedules, messages, documents, and fees from their own district's Campus Parent portal without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials, session cookies, and student records may be exposed through shared files or terminal logs.

Mitigation: Use a trusted system, keep environment files and cookie jars private, avoid printing tokens or sharing logs, and remove temporary session files and downloaded records when finished.

Risk: Downloading a document to an existing report-card.pdf may overwrite a local file.

Mitigation: Choose a different download filename if report-card.pdf already exists.

Risk: Retrieving a message body may mark it read on some district configurations.

Mitigation: Treat message retrieval as potentially state-changing and confirm the effect in the relevant district before relying on unread status.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands query a district-specific parent portal; available records and features vary by district.]

## Skill Version(s):

3.1.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
