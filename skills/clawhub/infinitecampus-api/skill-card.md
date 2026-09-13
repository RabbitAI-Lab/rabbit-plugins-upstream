## Description:

Query an Infinite Campus Campus Parent district portal with curl by logging in with user credentials, capturing session cookies and an XSRF token, and retrieving student records such as grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and technically capable portal users use this skill to query a district-specific Infinite Campus Parent portal without running the MCP server. It helps agents provide curl and jq recipes for reading student data from configured district endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles real Infinite Campus credentials and student records from a terminal session.

Mitigation: Use the correct HTTPS district portal, keep credentials and downloads out of untrusted files, and delete the cookie jar when the session is finished.

Risk: Session cookies and XSRF tokens could be exposed if reused with the wrong host or document URL.

Mitigation: Send cookies and XSRF headers only to the trusted district portal host, and do not forward them to cross-origin document URLs.

Risk: District modules and endpoint behavior vary, and some endpoints may be disabled or unconfirmed.

Mitigation: Check feature flags before treating 404 responses as failures, and verify endpoint behavior against the target district before relying on results.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash and jq code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require a user-provided district portal URL, district app name, username, password, cookie jar, and XSRF token.]

## Skill Version(s):

2.8.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
