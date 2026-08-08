## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server: search and read concert setlists, artists, venues, cities, and users with curl against the public REST API, and toggle setlist attendance through the authenticated website using an fpx-captured session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and shell users use this skill to fetch setlist.fm data with curl and jq, then optionally mark or unmark attendance for a setlist from an authenticated browser session. It is intended for scripted or local workflows where running the setlist MCP server is unnecessary or unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The attendance workflow uses a setlist.fm browser session cookie for authenticated website actions.

Mitigation: Keep the COOKIE value local to the shell session; do not paste, log, commit, or share it, and clear it when finished.

Risk: The attendance control is a toggle, so sending it without checking state can mark the wrong attendance status.

Mitigation: Perform the documented dry-run, confirm the desired state before sending the toggle, and re-fetch the page afterward to verify the result.

Risk: Read and write paths use different credentials and surfaces.

Mitigation: Keep SETLIST_API_KEY usage separate from cookie capture, and use the session cookie only for the user-directed attendance toggle.

## Reference(s):

- [setlist.fm API key settings](https://www.setlist.fm/settings/api)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown instructions with shell command examples and jq projections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces user-directed command guidance; read operations require a setlist.fm API key, and attendance writes require an authenticated setlist.fm browser session cookie.]

## Skill Version(s):

0.9.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
