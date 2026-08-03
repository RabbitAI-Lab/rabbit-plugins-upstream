## Description: <br>
Query setlist.fm data from a shell with curl and an API key, and optionally toggle a user's attendance state by replaying an authenticated website session cookie captured with fpx. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search and read artists, setlists, venues, cities, and users from setlist.fm without running an MCP server. It also provides a controlled shell workflow for marking or unmarking a user's own attendance when authenticated website access is required. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The attendance workflow asks users to extract and replay live setlist.fm browser session cookies that can change account state. <br>
Mitigation: Use only with an account you control, treat captured cookie values like passwords, avoid pasting them into chats or files, and clear shell variables after use. <br>
Risk: Authenticated attendance toggles can mutate setlist.fm account state if run without checking the current state first. <br>
Mitigation: Prefer read-only API use unless attendance toggling is specifically needed; dry-run first, send the toggle only after explicit intent, and re-fetch the page to verify the final state. <br>


## Reference(s): <br>
- [setlist.fm REST API read endpoints](references/rest-api.md) <br>
- [Attendance write walkthrough](references/attendance-write.md) <br>
- [setlist.fm API key settings](https://www.setlist.fm/settings/api) <br>
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/setlist-fpx) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and curl examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API request examples, jq projections, environment variable setup, and safety checks for authenticated attendance changes.] <br>

## Skill Version(s): <br>
0.9.5 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
