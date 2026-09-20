## Description:

Query an Infinite Campus Campus Parent portal district directly with curl by logging in with authorized credentials, capturing a session cookie and XSRF token, and retrieving grades, attendance, assignments, schedule, messages, documents, fees, and related student records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, automation authors, and authorized parents use this skill to turn Infinite Campus parent portal sessions into repeatable curl and jq workflows without running the MCP server. It is intended for authorized access to district-specific student records and portal data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands handle protected student records, account credentials, session cookies, XSRF tokens, and downloaded documents.

Mitigation: Use the skill only for authorized accounts, keep secrets and records out of logs and repositories, store temporary files with restrictive permissions, and delete session files after use.

Risk: Fetching a message body may mark the message read on some district configurations.

Mitigation: Avoid message-body requests when preserving unread state matters.

Risk: Some districts disable modules or return district-specific endpoint shapes.

Mitigation: Check displayOptions and treat expected 404 responses as disabled modules before interpreting them as failures.

Risk: Downloaded portal documents may contain sensitive student information.

Mitigation: Write downloads only to secure temporary or approved storage and remove them when no longer needed.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and curl/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces read-oriented command recipes that require user-supplied district URL, district app name, username, password, cookie jar, and XSRF token.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
