## Description:

Helps agents search MusicBrainz music metadata, find cover art, and, with OAuth and user confirmation, edit the user's own tags, ratings, and collections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music listeners, researchers, and developers use this skill to look up artists, releases, recordings, and cover art, or manage their own MusicBrainz tags, ratings, and collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled edits can change tags, ratings, or collections on the user's MusicBrainz account.

Mitigation: Review each proposed change and its preview, and obtain user approval before confirming any write.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MusicBrainz identifiers, cover-art URLs, and account-edit confirmation previews.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
