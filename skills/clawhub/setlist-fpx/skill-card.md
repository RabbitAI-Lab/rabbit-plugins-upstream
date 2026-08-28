## Description:

Query and update setlist.fm from a shell by using curl for public REST reads and an fpx-captured browser session cookie for the authenticated attendance toggle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically comfortable users use this skill to produce curl-based workflows for searching and reading setlist.fm artists, venues, cities, users, and setlists, and for marking or unmarking their own attendance when they have an authenticated browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uses a setlist.fm API key and browser session cookies that can expose account access if shared or logged.

Mitigation: Keep COOKIE, JSESSIONID, RememberMeCookie, the WAF token, and SETLIST_API_KEY out of commits, logs, shared shells, and messages; revoke the key or sign out if any value is exposed.

Risk: The attendance action is an authenticated website toggle, so blind execution can leave the wrong attendance state.

Mitigation: Dry-run first, compare the current and desired state before sending the toggle, then re-fetch the page and verify the final state after the request.

Risk: setlist.fm API use has attribution, caching, rate, and free-key use constraints described by the skill.

Mitigation: Surface followable setlist.fm links when displaying data, fetch live instead of maintaining a persistent cache, back off on rate limits, and confirm the intended use complies with the applicable setlist.fm terms.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx)
- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell command blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include curl, jq, perl, fpx, and environment-variable examples; users must supply their own setlist.fm API key and authenticated session cookie.]

## Skill Version(s):

0.9.8 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
