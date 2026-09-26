## Description:

Helps agents find concert setlists and live-performance history by artist, venue, tour, city, or date through setlist.fm.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer questions about songs performed at concerts and to explore artists, venues, and tour histories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite read-only wording, attendance tools can mark or unmark concerts on the user's setlist.fm account without confirmation.

Mitigation: Treat the integration as write-capable and invoke attendance changes only when the user explicitly intends them.

Risk: The connected service requires access to a setlist.fm API key.

Mitigation: Provide the key only to an MCP server you trust and do not expose or share it.

Risk: A free setlist.fm API key is for non-commercial use, even though this skill release has a commercial usage posture.

Mitigation: Obtain setlist.fm permission before using its API commercially.

## Reference(s):

- [setlist on ClawHub](https://clawhub.ai/chrischall/skills/setlist)
- [setlist-mcp npm package](https://www.npmjs.com/package/setlist-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with links to source setlists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some shows have no recorded songs; nearby tour setlists are references, not exact show records.]

## Skill Version(s):

1.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
