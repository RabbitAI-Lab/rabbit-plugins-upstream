## Description:

Searches MusicBrainz music metadata, retrieves cover art links, and, with OAuth and user confirmation, updates the user's tags, ratings, and collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music researchers, listeners, and developers use this skill to find artists, releases, recordings, identifiers, discographies, and cover art, or to manage their own MusicBrainz tags, ratings, and collections with approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tag, rating, or collection changes can alter the user's MusicBrainz account.

Mitigation: Configure OAuth only when account changes are intended, and review the preview before confirming each write.

Risk: The default compact view can omit image URL relation targets.

Mitigation: Request the full view when image URL relations are needed.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [musicbrainz-mcp ClawHub release](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text or Markdown summaries of structured music metadata and cover art links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries need no credentials; account changes require OAuth and user confirmation.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
