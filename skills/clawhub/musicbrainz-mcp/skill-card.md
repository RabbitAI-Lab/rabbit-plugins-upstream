## Description:

Helps agents search MusicBrainz music metadata, retrieve cover art links, and, with OAuth and user confirmation, update tags, ratings, and collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music enthusiasts and developers use this skill to find artists, recordings, releases, and cover art, or to manage their own MusicBrainz tags, ratings, and collections with confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated tag, rating, and collection edits change the user's MusicBrainz account.

Mitigation: Configure OAuth only when edits are needed; review each preview and obtain user confirmation before submitting.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured music metadata]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes MBIDs, cover art URLs, and confirmation previews or write receipts when applicable.]

## Skill Version(s):

1.2.4 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
