## Description:

setlist-fpx helps agents produce curl-based guidance for searching setlist.fm data through the public REST API and toggling a user's "I was there" attendance using an authenticated browser session cookie captured by fpx.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and power users use this skill to query artists, venues, cities, users, and setlists from setlist.fm with shell commands, and to mark or unmark attendance when they intentionally provide an authenticated browser session cookie.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to expose setlist.fm browser session cookies for authenticated attendance changes.

Mitigation: Keep captured cookies ephemeral, avoid logging or sharing them, clear the COOKIE variable after use, and revoke browser pairing when finished.

Risk: The skill recommends installing an unpinned global CLI for fpx cookie capture.

Mitigation: Pin or isolate the @fetchproxy/cli installation before use and review it before granting browser-session access.

Risk: Attendance toggles mutate account state on setlist.fm.

Mitigation: Dry-run first, confirm the desired state before sending the toggle request, and re-fetch the page afterward to verify the result.

Risk: setlist.fm API usage can be rate-limited and the free key is described as non-commercial with attribution and caching limits.

Mitigation: Respect the documented request limits, surface followable setlist.fm links with returned data, and avoid persistent local caching.

## Reference(s):

- [setlist-fpx ClawHub release](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm API settings](https://www.setlist.fm/settings/api)
- [setlist.fm REST API walkthrough](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and API request patterns]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl, jq, fpx, and shell environment variable examples for live setlist.fm requests.]

## Skill Version(s):

0.11.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
