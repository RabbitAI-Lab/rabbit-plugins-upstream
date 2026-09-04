## Description:

Search and browse the MusicBrainz music encyclopedia (artists, releases, recordings, labels, works), fetch Cover Art Archive images, resolve musicbrainz.org URLs, and - with OAuth configured - submit your own tags, ratings, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and external users use this skill to retrieve music metadata, discographies, MusicBrainz identifiers, cover art links, and account-edit previews for tags, ratings, and collections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled tools can modify the user's MusicBrainz tags, ratings, and collections.

Mitigation: Review the dry-run preview and only repeat the call with confirm set to true after explicit user approval.

Risk: MusicBrainz data and cover art results come from external community-maintained sources and may be incomplete or outdated.

Mitigation: Keep MBIDs and source links in the response so users can verify important metadata before relying on it.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/musicbrainz-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Natural language or Markdown summaries with MusicBrainz identifiers, links, and optional account-edit previews.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [OAuth-gated account edits return dry-run previews until the user confirms.]

## Skill Version(s):

0.2.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
