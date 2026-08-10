## Description:

Query setlist.fm from shell commands and guide authenticated attendance toggles using curl, an API key, and an fpx-captured browser session cookie.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill when they want setlist.fm data or need to mark and unmark attendance from a shell without running the setlist MCP server. It provides curl-oriented guidance for public REST reads and for the authenticated website-only attendance toggle.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles setlist.fm API keys and browser session cookies, including JSESSIONID, RememberMeCookie, aws-waf-token, and COOKIE values.

Mitigation: Treat those values as secrets: do not paste them into shared logs or commits, avoid long-lived shell history exposure, and unset them after use.

Risk: The attendance workflow can change the user's setlist.fm attendance state.

Mitigation: Dry-run first, confirm the current and desired state before sending the toggle, and re-fetch the page afterward to verify the result.

Risk: setlist.fm REST API use has attribution, caching, rate, and free-key non-commercial constraints documented by the skill.

Mitigation: Surface followable setlist.fm links when displaying data, avoid persistent local caching, pace requests, and confirm current API terms before commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints for curl](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include commands that use SETLIST_API_KEY, COOKIE, browser session cookies, and authenticated setlist.fm requests.]

## Skill Version(s):

0.9.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
