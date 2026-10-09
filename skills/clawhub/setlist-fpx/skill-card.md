## Description:

Helps agents search and read setlist.fm concert data through its REST API and update the user's attendance through an authenticated browser session, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and concertgoers use this skill to look up artists, venues, and setlists or intentionally mark and unmark their own attendance from the shell. The free setlist.fm API key is limited to non-commercial API use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to a signed-in browser session exposes sensitive setlist.fm cookies that could be reused to act on the user's account.

Mitigation: Treat captured cookies like passwords; do not save or log them, and clear shell variables after use.

Risk: The attendance control is a toggle and can change account state in the wrong direction.

Mitigation: Check the current state first, perform writes only on explicit request, and re-fetch the page to confirm the result.

## Reference(s):

- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API access](https://www.setlist.fm/settings/api)
- [ContextMint Bridge](https://github.com/nullnet-app/contextmint-bridge)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/setlist-fpx)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell examples and setlist.fm links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API reads need a key; attendance changes require the user's signed-in session.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
