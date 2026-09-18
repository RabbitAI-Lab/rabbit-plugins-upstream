## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server: search and read concert setlists, artists, venues, cities, and users via curl against the public REST API, and toggle attendance on a setlist through the authenticated website using an fpx-captured session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to retrieve setlist.fm data and mark or unmark personal attendance from shell workflows when they do not want to run the MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to expose setlist.fm session cookies to shell commands and a third-party CLI/browser-extension pairing.

Mitigation: Use it only when that access is acceptable, treat COOKIE and SETLIST_API_KEY as secrets, avoid logging or sharing terminal output, and remove or revoke the fpx pairing and global install when finished.

Risk: Attendance commands can change the user's setlist.fm account state.

Mitigation: Dry-run first, confirm the desired state before sending a toggle, and re-read the page afterward to verify the result.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm API settings](https://www.setlist.fm/settings/api)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs curl, jq, fpx, and shell snippets for live setlist.fm reads and authenticated attendance toggles.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
