## Description:

Query and update setlist.fm from a shell using curl: read artists, setlists, venues, cities, and users through the public REST API, and toggle "I was there" attendance on the authenticated website with an fpx-captured session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable setlist.fm users use this skill to retrieve setlist.fm data from shell scripts and to deliberately mark or unmark attendance without running the setlist MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The attendance workflow requires a live setlist.fm browser session cookie for account-changing actions.

Mitigation: Treat the COOKIE value like a password, keep it out of shared logs, scripts, issues, commits, and shell transcripts, and refresh or revoke the browser session if it may have been exposed.

Risk: Attendance changes can modify the user's setlist.fm account state.

Mitigation: Use the documented dry-run path, confirm each intended attendance change deliberately, and re-fetch the page afterward to verify the final state.

## Reference(s):

- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance separates read-only API calls from authenticated attendance changes and calls for dry-run verification before writes.]

## Skill Version(s):

0.10.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
