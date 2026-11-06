## Description:

Query an Infinite Campus (Campus Parent portal) district directly with curl instead of running the infinitecampus-mcp server — log in with a real username/password, capture the session cookie + XSRF token, and curl grades, attendance, assignments, schedule, messages, documents, and fees. Use when you want IC data without the MCP, in a script, or on a machine where the MCP isn't installed. Infinite Campus is per-district: the base URL and district app name are configurable, not hardcoded.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and developers use this skill to query a district's Infinite Campus Campus Parent portal from shell scripts and retrieve student grades, attendance, assignments, schedules, messages, documents, and fees without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The document-download example may send portal cookies and the XSRF header to an unchecked external address.

Mitigation: Verify that the download URL uses the district's HTTPS origin; omit portal cookies and XSRF headers for other hosts.

Risk: Portal queries and downloaded documents can expose sensitive student records.

Mitigation: Request only the records needed, protect downloaded files, and delete the temporary cookie jar after use.

## Reference(s):

- [Endpoint recipes](references/endpoints.md)
- [ClawHub release page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, JSON data, Guidance]

**Output Format:** [Markdown with inline curl and jq commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific portal URL and app name; requires portal credentials and an authenticated session.]

## Skill Version(s):

3.3.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
