## Description:

Query an Infinite Campus Campus Parent portal district directly with curl by logging in with a username and password, capturing the session cookie and XSRF token, and retrieving grades, attendance, assignments, schedules, messages, documents, fees, and related student records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized Infinite Campus users use this skill to make direct curl requests against a district Campus Parent portal when they need scriptable access to student portal data without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles real parent credentials, session cookies, XSRF tokens, and student records.

Mitigation: Use only accounts and student records you are authorized to access; keep credentials and cookie jars out of logs and shared directories.

Risk: Document download URLs may be absolute and could direct requests outside the intended district portal.

Mitigation: Verify that IC_BASE_URL is the exact HTTPS district portal and do not follow absolute document URLs unless they match the same trusted district origin.

Risk: Downloaded documents and session files may contain sensitive student information.

Mitigation: Delete session files and downloaded documents when the task is complete.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown with inline bash and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only curl recipes that require a trusted district portal URL, authorized credentials, a session cookie jar, and an XSRF header.]

## Skill Version(s):

2.8.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
