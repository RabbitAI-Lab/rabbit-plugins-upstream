## Description:

Helps agents query setlist.fm concert data with shell commands and update attendance using an authenticated browser session without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and concertgoers use this skill to find artists, venues, cities, and setlists or to mark and unmark their own attendance. Free setlist.fm API keys are restricted to non-commercial use; check API terms before commercial use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The write workflow handles authenticated browser session cookies and an API key.

Mitigation: Use the browser-session helper only if you trust it; keep cookies and the API key out of chats, logs, files, screenshots, and shell history.

Risk: The attendance toggle can change account history or reverse an intended change.

Mitigation: Dry-run, check the current state, change only explicitly selected setlists, and re-fetch the page to verify the result.

## Reference(s):

- [setlist.fm REST API read endpoints](references/rest-api.md)
- [Attendance write walkthrough](references/attendance-write.md)
- [setlist.fm API key and terms](https://www.setlist.fm/settings/api)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results should link to setlist.fm; attendance changes require confirmation and a fresh state check.]

## Skill Version(s):

1.1.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
