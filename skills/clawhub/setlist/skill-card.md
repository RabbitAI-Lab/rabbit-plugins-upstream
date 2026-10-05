## Description:

Helps agents find concert setlists, songs, artists, venues, and live-music history through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music fans and researchers use this skill to look up concert setlists, songs performed, artists, venues, and shows by date or location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only descriptions, attendance tools can change a user's setlist.fm account without an additional confirmation step.

Mitigation: Only mark or unmark attendance following an explicit user request; treat these actions as account changes.

Risk: The integration requires access to a setlist.fm API key.

Mitigation: Supply the key only to a trusted server and do not expose it in responses.

Risk: A free setlist.fm API key is for non-commercial use; commercial use requires permission.

Mitigation: Check setlist.fm's API terms and obtain permission before commercial use.

## Reference(s):

- [Setlist skill on ClawHub](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp package](https://www.npmjs.com/package/setlist-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with setlist.fm source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live results may have incomplete song lists; show attribution links when presenting setlist.fm data.]

## Skill Version(s):

1.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
