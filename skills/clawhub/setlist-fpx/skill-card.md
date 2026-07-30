## Description: <br>
Tmp.2fojgKgotX helps agents produce curl-based commands and guidance for reading setlist.fm data through the public REST API and toggling a user's attendance status with an fpx-captured session cookie. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technically comfortable setlist.fm users use this skill to query artists, venues, cities, setlists, and user attendance from a shell, and to mark or unmark their own attendance when they have a valid browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The fpx-captured setlist.fm session cookie is sensitive account material. <br>
Mitigation: Treat the cookie like a password: keep it out of logs and long-lived shell history, clear it after use on shared terminals, and rotate or log out the session if it may have been exposed. <br>
Risk: Attendance writes can change a user's setlist.fm account state. <br>
Mitigation: Dry-run first, verify the current attendance state before sending a toggle, and re-read the page afterward to confirm the final state. <br>
Risk: setlist.fm API use is subject to attribution, caching, rate-limit, and key-use constraints. <br>
Mitigation: Surface followable setlist.fm links when showing API data, avoid persistent local caching, and back off when rate-limited. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx) <br>
- [setlist.fm REST API read endpoints for curl](references/rest-api.md) <br>
- [Attendance write walkthrough](references/attendance-write.md) <br>
- [setlist.fm API key settings](https://www.setlist.fm/settings/api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl, jq, perl, npm, and fpx command examples; users must supply their own API key and browser session cookie.] <br>

## Skill Version(s): <br>
0.9.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
