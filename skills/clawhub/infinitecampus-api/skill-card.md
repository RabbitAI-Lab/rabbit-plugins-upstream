## Description:

Query an Infinite Campus Campus Parent portal directly with curl to log in, capture a session cookie and XSRF token, and retrieve grades, attendance, assignments, schedules, messages, documents, and fees without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, parents, guardians, and authorized users use this skill to retrieve their own Infinite Campus portal data with curl and jq when they need scriptable access without installing the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Credentials, cookie jars, XSRF tokens, downloaded documents, and command output may contain sensitive student records.

Mitigation: Use only authorized Infinite Campus accounts, keep secrets and outputs out of logs, avoid sharing them, and delete temporary session files after use.

Risk: Fetching a message body may mark it read on some district configurations.

Mitigation: Fetch message bodies only when the possible read-state change is acceptable.

Risk: Some district modules or endpoints may be disabled or unavailable, and the behavior and food service paths are documented as unconfirmed live paths.

Mitigation: Check displayOptions feature flags first and treat documented module 404 responses as disabled or unavailable rather than as unexpected failures.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API Calls, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and curl/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only curl recipes using user-provided district URL, district app name, username, password, cookie jar, and XSRF token.]

## Skill Version(s):

3.1.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
