## Description:

setlist-fpx helps agents query setlist.fm data with curl and guide users through marking or unmarking attendance by replaying authenticated website requests with an fpx-captured session cookie.

This skill is for research and development only.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation-minded users use this skill to search or fetch setlist.fm artists, venues, cities, users, and setlists from the REST API, and to carefully toggle their own attendance state when they have an authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fpx CLI and browser extension can access setlist.fm login cookies that may be replayed to change account state.

Mitigation: Use a dedicated browser profile when possible, avoid shared terminals and logs, do not paste or commit cookie values, unset SETLIST_API_KEY and COOKIE after use, and revoke the fpx pairing when finished.

Risk: The attendance toggle mutates the user's setlist.fm account state and a successful HTTP response does not prove the desired state was applied.

Mitigation: Dry-run first, parse the current attendance state, send the toggle only when it differs from the desired state, then re-fetch the page and verify the final state.

Risk: The setlist.fm free API key is described as non-commercial and the skill notes attribution and caching obligations for displayed setlist.fm data.

Mitigation: Confirm setlist.fm API terms before commercial use, include followable setlist.fm links when presenting data, and avoid persistent local caching.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may include API-key setup, cookie capture steps, request examples, dry-run checks, and verification steps.]

## Skill Version(s):

0.11.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
