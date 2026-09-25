## Description:

Search and browse the MusicBrainz music encyclopedia, fetch Cover Art Archive images, resolve musicbrainz.org URLs, and, with OAuth configured, submit the user's own tags, ratings, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent developers use this skill to look up music metadata, retrieve cover art links, resolve MusicBrainz identifiers, and manage their own MusicBrainz account tags, ratings, or collections when OAuth is configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled write tools can modify the user's own MusicBrainz tags, ratings, or collections.

Mitigation: Configure OAuth only when write access is needed, review the returned preview, and submit the confirmation token only after user approval.

Risk: Compact view can omit image URL relation resources when resolving URL relationships.

Mitigation: Request full view when image URL relations are needed.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [JSON tool responses and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read operations return MusicBrainz or Cover Art Archive data; write operations return confirmation previews or submission receipts.]

## Skill Version(s):

1.2.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
