## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server by using curl for public REST API reads and an fpx-captured browser session cookie for the authenticated attendance toggle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search setlist.fm artists, venues, cities, users, and setlists from shell workflows, and to mark or unmark their own attendance after confirming the desired state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attendance writes require access to the user's setlist.fm browser session cookie.

Mitigation: Use fpx only for the intended setlist.fm profile, keep the captured cookie out of logs, avoid persistent local caching, and recapture the cookie when the session expires.

Risk: The attendance control is a toggle, so sending it without checking state can mark the opposite of the intended outcome.

Mitigation: Dry-run first, parse the current attendance state, require explicit confirmation before sending the toggle, and re-fetch the page afterward to verify the final state.

Risk: setlist.fm API reads depend on an API key and service usage terms.

Mitigation: Keep SETLIST_API_KEY out of logs, respect rate limits and attribution requirements, and avoid persistent caching as the skill instructs.

## Reference(s):

- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl, jq, fpx, and environment-variable handling steps for read and attendance workflows.]

## Skill Version(s):

0.9.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
