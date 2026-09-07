## Description:

Search and browse the MusicBrainz music encyclopedia for artists, releases, recordings, labels, works, cover art, resolved MusicBrainz URLs, and optional user-approved account edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to query MusicBrainz metadata, retrieve cover art, resolve MusicBrainz links, and, when OAuth is configured, prepare user-approved edits to their own MusicBrainz tags, ratings, and collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled tools can modify the user's own MusicBrainz tags, ratings, or collections.

Mitigation: Configure OAuth only when account edits are intended, review the dry-run preview, and approve confirmed writes only after user consent.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown and structured tool-call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read lookups require no credentials; account writes require OAuth and confirmation after a dry-run preview.]

## Skill Version(s):

0.3.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
