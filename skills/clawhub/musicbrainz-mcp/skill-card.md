## Description:

Helps agents find MusicBrainz music metadata and cover art, and optionally update a user's own tags, ratings, and collections with OAuth and confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Music listeners, researchers, and developers use this skill to search artists and recordings, browse discographies, retrieve cover-art links, and optionally manage their own MusicBrainz tags, ratings, or collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: With OAuth enabled, the skill can change the user's MusicBrainz tags, ratings, or collections.

Mitigation: Configure OAuth only when account edits are needed; keep confirmation enabled and approve each proposed edit before submission.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [MusicBrainz MCP on ClawHub](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MusicBrainz identifiers, cover-art links, and confirmation previews or receipts for account edits.]

## Skill Version(s):

1.2.7 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
