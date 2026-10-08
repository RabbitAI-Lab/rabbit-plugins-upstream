## Description:

Guides parents and their agents through querying their district's Infinite Campus Parent portal with curl for grades, attendance, assignments, schedules, messages, documents, and fees without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers use this skill to retrieve their own students' portal information from a district-specific Infinite Campus site using curl and jq, without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Portal credentials and session cookies could expose a parent's account if shared or stored insecurely.

Mitigation: Keep credentials, the cookie jar, and the XSRF token in private locations; remove session files after use.

Risk: Downloaded documents and query results may contain sensitive student records.

Mitigation: Avoid shared or synced storage for student records and delete downloaded files when finished.

## Reference(s):

- [Infinite Campus curl endpoint recipes](references/endpoints.md)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with curl and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Portal responses may include sensitive student records; available endpoints vary by district.]

## Skill Version(s):

3.1.8 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
