## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server: search and read concert setlists, artists, venues, cities, and users through the public REST API, and toggle setlist attendance through the authenticated website using an fpx-captured session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical users use this skill to retrieve setlist.fm data with curl, compose API requests, and mark or unmark attended shows from a signed-in browser session without running the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The attendance workflow handles a captured setlist.fm browser session cookie that can authorize account actions if exposed.

Mitigation: Treat the cookie like a password, avoid logging or sharing commands that expose it, and clear the shell variable after use.

Risk: Attendance changes can toggle account state on setlist.fm.

Mitigation: Keep the documented dry-run and confirmation step before sending any attendance change, then re-fetch the page to verify the final state.

Risk: The workflow depends on the external fpx CLI and Transporter browser extension to capture cookies.

Mitigation: Install and use the workflow only when those external components are trusted.

## Reference(s):

- [setlist-fpx ClawHub release](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints](artifact/references/rest-api.md)
- [Attendance write walkthrough](artifact/references/attendance-write.md)
- [setlist.fm API settings](https://www.setlist.fm/settings/api)
- [setlist.fm REST API base URL](https://api.setlist.fm/rest)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided setlist.fm API credentials for reads and a captured authenticated website cookie for attendance changes.]

## Skill Version(s):

0.11.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
