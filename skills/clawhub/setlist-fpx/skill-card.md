## Description: <br>
Query and update setlist.fm from a shell without running the setlist-mcp server, using curl for REST reads and an fpx-captured session cookie for the website attendance toggle. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and shell users use this skill to read setlist.fm artists, setlists, venues, cities, and users via curl and to mark or unmark their own attendance from an authenticated browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The captured setlist.fm COOKIE value can authenticate as the user. <br>
Mitigation: Treat COOKIE like a password, use it only on trusted machines, avoid logging or sharing commands that expose it, and clear the variable when finished. <br>
Risk: The attendance control is a toggle, so an unverified write can set the opposite state from what the user intended. <br>
Mitigation: Dry-run first, compare the current state with the desired state, send the toggle only when needed, and re-fetch the page to verify the final state. <br>
Risk: setlist.fm sessions can expire, throttle, or encounter transient gateway errors during authenticated writes. <br>
Mitigation: Check for logged-out pages before acting, re-capture the cookie when needed, pace multiple writes, and retry transient failures with a short delay. <br>


## Reference(s): <br>
- [Attendance write walkthrough](references/attendance-write.md) <br>
- [setlist.fm REST API read endpoints](references/rest-api.md) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-only REST examples and a guarded attendance-toggle workflow that requires user-held credentials.] <br>

## Skill Version(s): <br>
0.9.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
