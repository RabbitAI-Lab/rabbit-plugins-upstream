## Description:

Guides agents to read setlist.fm concert data via its REST API and update attendance through an authenticated browser session without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search and retrieve setlists, artists, venues, cities, and users from a shell, or to mark and unmark attendance on their own setlist.fm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Capturing a browser session cookie for attendance changes exposes sensitive account credentials to local tooling.

Mitigation: Use only your own account, verify the bridge and CLI source, do not print or save cookie values, and clear shell variables after use.

Risk: An attendance toggle can reverse the intended state if sent blindly.

Mitigation: Dry-run and check the current state before toggling, then re-fetch the page to verify the result.

## Reference(s):

- [setlist.fm REST API guide](references/rest-api.md)
- [Attendance update walkthrough](references/attendance-write.md)
- [setlist.fm API key setup](https://www.setlist.fm/settings/api)
- [ContextMint Bridge source and releases](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public API reads require an API key; the free key is non-commercial and displayed data requires attribution. Attendance changes require the user's signed-in session.]

## Skill Version(s):

1.1.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
