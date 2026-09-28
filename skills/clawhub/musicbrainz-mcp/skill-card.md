## Description:

Helps agents search MusicBrainz metadata, find cover art, and, with OAuth and user confirmation, update a user's tags, ratings, and collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music listeners and researchers use this skill to identify artists, releases, recordings, and cover art. With OAuth configured, they can also manage their own MusicBrainz tags, ratings, and collections after approving each change.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled account edits can change personal tags, ratings, or collections.

Mitigation: Enable OAuth only when needed and review each preview before approving a change.

Risk: Music metadata lookups connect to external MusicBrainz services.

Mitigation: Submit only queries you are comfortable sending to MusicBrainz.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [MusicBrainz MCP on ClawHub](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Natural-language answers and structured MusicBrainz tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read results default to compact view; full view retains image links. Account changes return a preview requiring user confirmation.]

## Skill Version(s):

1.2.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
