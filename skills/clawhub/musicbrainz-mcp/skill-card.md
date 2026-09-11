## Description:

Search and browse MusicBrainz metadata, fetch Cover Art Archive image links, resolve musicbrainz.org URLs, and, with OAuth configured, prepare confirm-gated MusicBrainz tag, rating, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up music metadata, fetch cover art links, resolve MusicBrainz URLs, and manage their own MusicBrainz tags, ratings, and collections when OAuth is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Read-only metadata and cover-art lookups contact MusicBrainz or the Cover Art Archive.

Mitigation: Use the skill when external metadata lookup is appropriate and avoid submitting sensitive account context unless needed.

Risk: OAuth-enabled calls can modify the user's MusicBrainz tags, ratings, or collections.

Mitigation: Review the dry-run preview and only approve confirm:true write calls when the proposed edit matches the user's intent.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown guidance with JSON-compatible MusicBrainz and Cover Art Archive tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups contact MusicBrainz or the Cover Art Archive; account-changing operations require OAuth and explicit confirmation.]

## Skill Version(s):

0.3.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
