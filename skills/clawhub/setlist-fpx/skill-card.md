## Description:

Guides agents in searching and reading setlist.fm concert data with its REST API and updating a user's attendance through an authenticated browser session, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other setlist.fm users can use this skill to look up artists, setlists, venues, cities, and users from a shell, or mark and unmark their attendance at a show. The free setlist.fm API key is restricted to non-commercial use under the site's API terms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A captured setlist.fm session cookie can enable account actions if disclosed.

Mitigation: Treat the cookie like a password; keep it out of logs, shell history, commits, and shared transcripts, and use the bridge only if you trust it with your session.

Risk: Blindly toggling attendance can undo the intended state.

Mitigation: Check the current state, dry-run before sending the toggle, and re-fetch the page to verify the result.

## Reference(s):

- [setlist-fpx release on ClawHub](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm API key and terms](https://www.setlist.fm/settings/api)
- [REST API read endpoints](references/rest-api.md)
- [Attendance update walkthrough](references/attendance-write.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [REST reads require an API key; attendance changes require an authenticated setlist.fm session and confirmation of the current state.]

## Skill Version(s):

1.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
