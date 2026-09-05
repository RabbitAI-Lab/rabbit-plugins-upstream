## Description:

Query an Infinite Campus Campus Parent portal district directly with curl by logging in with parent portal credentials, capturing the session cookie and XSRF token, and reading grades, attendance, assignments, schedules, messages, documents, and fees.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate curl and jq workflows for reading their authorized Infinite Campus Campus Parent portal data without running an MCP server. It is intended for per-district portal access where the user supplies the district base URL, app name, username, and password.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive student records and live session tokens.

Mitigation: Use it only with authorized Infinite Campus accounts, keep cookies and XSRF tokens out of logs and transcripts, store downloads in protected locations, and delete the cookie jar after use.

Risk: Absolute document URLs could point outside the expected district portal host.

Mitigation: Confirm absolute document URLs are on the expected district host before downloading.

Risk: Fetching an individual message body may mark it read on some district configurations.

Mitigation: Treat message-body fetches as potentially state-changing and avoid them when preserving unread state matters.

## Reference(s):

- [Infinite Campus endpoints for curl](references/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/infinitecampus-api)
- [ClawHub publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only portal query recipes; downloads may produce local files when the user chooses a document URL.]

## Skill Version(s):

2.8.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
