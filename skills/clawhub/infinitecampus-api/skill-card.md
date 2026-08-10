## Description:

Query an Infinite Campus Campus Parent portal district directly with curl to log in, capture session credentials, and retrieve grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and authorized Infinite Campus users use this skill to script read-oriented Campus Parent portal queries without installing the MCP server. It is intended for accounts and student records the user is authorized to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles live parent-portal sessions and sensitive student records.

Mitigation: Use only accounts and students you are authorized to access, keep credentials and cookie jars out of chats, logs, shell history, and repositories, and clean up session files when done.

Risk: Document downloads may include sensitive student files and can use a relative or absolute URL.

Mitigation: Constrain downloads to the expected district portal host and store downloaded files only in protected locations.

Risk: Fetching a message body may mark it read on some district configurations.

Mitigation: Avoid retrieving message bodies when preserving unread status matters, or warn the user before doing so.

Risk: Some district modules and endpoint paths may be disabled or unconfirmed.

Mitigation: Check displayOptions before calling module-specific endpoints and treat expected 404 responses as disabled features rather than failures.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and curl/jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-oriented API calls and document downloads against a user-provided district portal using environment variables for district URL, app name, username, and password.]

## Skill Version(s):

2.4.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
