## Description:

Helps agents find concert setlists and live-music history through setlist.fm, with optional attendance updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music fans and researchers use this skill to find songs played at concerts, explore artists' tours and venue histories, and identify shows by date or location. It can also mark or unmark concerts attended on a user's setlist.fm account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attendance tools can change a setlist.fm account despite the skill describing itself as read-only and saying confirmation is unnecessary.

Mitigation: Require explicit user approval before marking or unmarking attendance.

Risk: Connecting the server requires sharing a setlist.fm API key with it.

Mitigation: Install only if comfortable granting the server access to the API key; do not expose the key in responses.

## Reference(s):

- [Setlist ClawHub release](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key settings](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration instructions, Shell commands]

**Output Format:** [Markdown with setlist.fm links and optional setup snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setlist results may include song details and links; attendance actions change the user's account.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
