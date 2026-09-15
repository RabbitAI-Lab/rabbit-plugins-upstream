## Description:

Query an Infinite Campus Campus Parent portal district directly with curl by logging in with a username and password, capturing the session cookie and XSRF token, and retrieving grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to query their own district's Infinite Campus Parent portal from scripts or agent workflows without running the infinitecampus-mcp server. It is useful for read-oriented access to student records such as grades, attendance, assignments, schedules, messages, documents, and fees.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles real school-portal credentials, cookies, and XSRF tokens.

Mitigation: Use only a verified HTTPS district portal URL, keep credentials in a trusted secret store or controlled environment, and protect the cookie jar and XSRF token from disclosure.

Risk: Downloaded documents may contain sensitive student or family information.

Mitigation: Save downloads only to a protected path controlled by the user and avoid shared or world-readable locations.

Risk: Fetching a message body may mark that message as read on some district configurations.

Mitigation: Fetch message bodies only when the user intends to open them, and prefer listing message metadata when read state matters.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Curl and jq recipes for read-oriented portal requests, including login, session reuse, endpoint calls, downloads, and feature checks.]

## Skill Version(s):

2.8.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
