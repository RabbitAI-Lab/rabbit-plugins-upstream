## Description:

Guides authorized Campus Parent users through querying district-specific Infinite Campus portal data with curl without an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized parents, guardians, and developers use the skill to retrieve grades, attendance, assignments, schedules, messages, documents, and fees from their district's Campus Parent portal without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account credentials, session cookies, and student records could be exposed if logged, shared, or left on a shared machine.

Mitigation: Use only an account you are authorized to access; keep credentials, tokens, reports, and records private, and remove temporary session files and downloads when finished.

Risk: Fetching a message body may mark the message as read on some district portals.

Mitigation: Fetch message bodies only when marking the message read would be acceptable.

## Reference(s):

- [Infinite Campus endpoint recipes](references/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/infinitecampus-api)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [District-specific portal URL and authorized account credentials required.]

## Skill Version(s):

3.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
