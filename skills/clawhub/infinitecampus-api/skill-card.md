## Description:

Guides authorized Campus Parent users through querying their district's Infinite Campus portal with curl for student grades, attendance, assignments, schedules, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents and developers use this skill to retrieve student portal information from their own district using curl, including grades, attendance, assignments, and documents.

### Deployment Geography for Use:

Global; requires access to a participating district's Campus Parent portal.

## Known Risks and Mitigations:

Risk: Portal credentials and session cookies can expose a school account if logged or left on an untrusted machine.

Mitigation: Use an authorized account on a trusted machine, keep credentials and cookies out of logs, and delete temporary cookie jars after use.

Risk: Downloaded documents and query results may disclose protected student records.

Mitigation: Limit access to records you are authorized to view, store downloaded files securely, and remove temporary files when finished.

Risk: Opening a message body may mark the message as read on some districts.

Mitigation: Avoid opening message bodies unless a possible read-status change is acceptable.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance]

**Output Format:** [Markdown with curl and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific portal settings and authorized parent credentials are required; responses may contain protected student information.]

## Skill Version(s):

3.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
