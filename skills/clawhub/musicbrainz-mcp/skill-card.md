## Description:

Search and browse the MusicBrainz music encyclopedia, fetch Cover Art Archive images, resolve musicbrainz.org URLs, and, with OAuth configured, submit the user's own tags, ratings, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve MusicBrainz metadata, discographies, MBIDs, cover art links, and account-specific MusicBrainz edits through the exposed MCP tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled tools can modify the user's own MusicBrainz tags, ratings, or collections.

Mitigation: Configure OAuth only when account edits are intended, show dry-run previews to the user, and submit only after explicit confirmation.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Text]

**Output Format:** [Markdown guidance with MCP tool-call examples and JSON-shaped parameters]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only lookups need no credentials; OAuth-enabled writes use dry-run previews and require explicit confirmation.]

## Skill Version(s):

1.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
