## Description:

Helps agents find concert setlists and live-performance history through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

People researching concerts use this skill to find songs performed by an artist, at a venue, or on a particular date. It also offers account-attendance actions that change a user's setlist.fm state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attendance tools can change a user's account state without confirmation, despite read-only claims elsewhere in the skill.

Mitigation: Review before installation and disable or gate attendance tools unless account changes are intended.

Risk: An account API key is required and could be exposed if shared.

Mitigation: Keep the API key private and do not include it in responses.

Risk: A free setlist.fm API key is limited to non-commercial use.

Mitigation: Obtain setlist.fm permission before commercial use.

## Reference(s):

- [setlist-mcp package](https://www.npmjs.com/package/setlist-mcp)
- [setlist.fm API key setup](https://www.setlist.fm/settings/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with source links to setlist.fm]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include songs, concert details, and links to source setlists.]

## Skill Version(s):

1.1.9 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
