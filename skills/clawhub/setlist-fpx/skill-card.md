## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server: search and read concert setlists, artists, venues, cities, and users through the public REST API, and toggle setlist attendance through an authenticated website session cookie captured with fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users use this skill to generate shell workflows for retrieving setlist.fm data and marking or unmarking personal concert attendance without running an MCP server. It is useful for scripted lookup, lightweight automation, and account-scoped attendance updates that the public REST API does not provide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The write workflow uses a signed-in setlist.fm browser session cookie to change account attendance state.

Mitigation: Use the workflow only on trusted machines, avoid shared shells and shell tracing, do not paste cookies into scripts or logs, unset COOKIE after use, and sign out or revoke the browser session when finished.

Risk: An attendance toggle can change account state if the current page state is misread or the user skips confirmation.

Mitigation: Dry-run first, compare the current state with the desired state, require explicit confirmation before sending the Wicket AJAX request, and re-fetch the page afterward to verify the result.

Risk: API keys and captured cookies may be exposed through command history, logs, or copied shell output.

Mitigation: Store SETLIST_API_KEY and COOKIE only in the current shell environment, avoid logging request headers, and clear sensitive environment variables after use.

## Reference(s):

- [setlist-fpx ClawHub release](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API settings](https://www.setlist.fm/settings/api)
- [REST API read endpoint catalog](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include REST API calls, environment variable setup, cookie-capture steps, dry-run checks, and verification steps.]

## Skill Version(s):

0.11.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
