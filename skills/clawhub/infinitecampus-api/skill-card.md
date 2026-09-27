## Description:

Guides authorized Campus Parent users in querying their district's Infinite Campus portal with curl for student grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use this skill to retrieve student portal information from their own district without installing the companion MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials, session cookies, and XSRF tokens may be exposed in logs or shared files.

Mitigation: Use only an authorized account, avoid logging or sharing secrets and cookie jars, and delete temporary files after use.

Risk: Grades, attendance, messages, documents, and fees may contain sensitive student records.

Mitigation: Limit access and sharing to authorized recipients; avoid retaining or logging raw responses and downloaded documents.

## Reference(s):

- [Infinite Campus API skill listing](https://clawhub.ai/chrischall/skills/infinitecampus-api)
- [Infinite Campus endpoint recipes](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific access requires authorized portal credentials; returned student records may be sensitive.]

## Skill Version(s):

3.1.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
