## Description:

Guides agents to read setlist.fm data through its REST API and update attendance through a signed-in browser session, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents can look up setlists, artists, venues, cities, and users from a shell, and—with the account holder's approval—mark or unmark attendance on their own setlist.fm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A browser bridge can access the user's signed-in setlist.fm session cookie; disclosing or retaining the cookie can expose the account.

Mitigation: Use only your own account; treat COOKIE and RememberMeCookie as passwords, avoid logging or saving them, and unset them after use.

Risk: The attendance action is a toggle and can reverse the intended state if issued without checking it first.

Mitigation: Confirm the dry-run attendance state and intended change before executing the write step.

## Reference(s):

- [setlist.fm API access](https://www.setlist.fm/settings/api)
- [REST API usage reference](references/rest-api.md)
- [Attendance update reference](references/attendance-write.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results may contain setlist.fm links; attendance changes require a separate confirmed write step.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
