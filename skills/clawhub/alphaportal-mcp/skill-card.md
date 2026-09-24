## Description:

Provides shell-based AlphaPortal (AlphaRoute) access guidance for student transportation data, including students, stops, live bus GPS, and notifications, by capturing a browser refresh token, minting access tokens, and calling the REST API with curl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and authorized AlphaPortal users use this skill to retrieve school-bus student, stop, notification, and vehicle-location data from scripts or shell sessions without running the MCP server. It is intended for accounts and records the user is already permitted to access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Refresh and access tokens can expose AlphaPortal accounts and sensitive student transportation data if copied into chats, logs, shared shells, or persistent history.

Mitigation: Use the skill only for accounts and student records you are authorized to access; treat tokens like passwords; avoid shared machines and persistent shell history; do not paste tokens or student-location output into chats or logs.

Risk: Shell write endpoints can change real transportation records without the MCP server's dry-run confirmation flow.

Mitigation: Prefer official or MCP flows with confirmations and audit controls for write operations; review request bodies before execution and limit use to authorized changes.

## Reference(s):

- [AlphaPortal endpoint reference](references/endpoints.md)
- [AlphaRoute API base](https://api.alpharoute.app)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes curl and jq examples for authenticated AlphaPortal API calls.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
