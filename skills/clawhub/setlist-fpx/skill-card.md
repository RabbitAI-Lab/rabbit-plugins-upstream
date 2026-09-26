## Description:

Helps agents search and read setlist.fm concert data through its REST API and update a user's attendance through an authenticated browser session, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other setlist.fm users can search concert setlists, artists, venues, cities, and users from a shell, and mark or unmark their own attendance when signed in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing and replaying a setlist.fm browser session cookie can expose account access if the value is disclosed.

Mitigation: Treat the cookie like a password: never share, log, or paste it into transcripts or scripts; avoid leaving it in shell history, and sign out or revoke the session when finished.

Risk: Blindly triggering the attendance toggle can reverse the intended account setting.

Mitigation: Read the current state first, confirm the intended change before toggling, then reload the page to verify the result.

## Reference(s):

- [setlist.fm API access](https://www.setlist.fm/settings/api)
- [REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Free API keys are for non-commercial use; show followable setlist.fm attribution links and avoid persistent caching.]

## Skill Version(s):

1.1.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
