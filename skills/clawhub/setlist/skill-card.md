## Description:

Helps agents find concert setlists and live-music history through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music fans and researchers use this skill to find songs performed at concerts and explore artists, venues, tours, and live-performance history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attendance tools can change the user's setlist.fm account despite read-only wording and no built-in confirmation step.

Mitigation: Require explicit user approval before marking or unmarking attendance.

Risk: The integration needs a setlist.fm API key.

Mitigation: Provide the key only to a trusted integration, keep it secret, and do not include it in responses.

Risk: The free setlist.fm API key is for non-commercial use.

Mitigation: Obtain setlist.fm permission before using its API commercially and follow its attribution terms.

## Reference(s):

- [Setlist skill on ClawHub](https://clawhub.ai/chrischall/skills/setlist)
- [setlist.fm API terms](https://www.setlist.fm/help/api-terms)
- [setlist-mcp package](https://www.npmjs.com/package/setlist-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Distinguish exact-show setlists from nearby-tour examples and link to setlist.fm sources.]

## Skill Version(s):

1.1.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
