## Description:

Query and update setlist.fm from a shell without running the setlist-mcp server: search and read concert setlists, artists, venues, cities, and users through the public REST API, and toggle "I was there" attendance on a setlist through the authenticated website using an fpx-captured session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical music-data users use this skill to generate shell-based workflows for reading setlist.fm data and, when explicitly intended, marking or unmarking attendance on their own setlist.fm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to capture and reuse live setlist.fm browser session cookies for authenticated attendance changes.

Mitigation: Treat the captured cookie as a password: avoid logging or storing it, keep it out of shared terminals, and refresh or revoke the session if exposure is possible.

Risk: Attendance writes mutate the user's setlist.fm account state and the toggle response alone may not prove the final state.

Mitigation: Dry-run first, send the toggle only after explicit intent is established, and re-fetch the page afterward to verify the attendance state.

Risk: Rapid authenticated write attempts or expired sessions can produce unreliable results.

Mitigation: Pace write requests, detect logged-out pages, and re-capture the session cookie before retrying when the session has expired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl, jq, fpx, and browser-session cookie handling steps for live setlist.fm requests.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
