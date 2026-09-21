## Description:

Search and browse the MusicBrainz music encyclopedia (artists, releases, recordings, labels, works), fetch Cover Art Archive images, resolve musicbrainz.org URLs, and, with OAuth configured, submit your own tags, ratings, and collection edits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve MusicBrainz metadata, discographies, album art links, MBIDs, and details about artists, releases, recordings, labels, and works. Users with OAuth configured can also prepare and confirm account-scoped MusicBrainz edits such as tags, ratings, and collection changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OAuth-enabled write tools can change the user's own MusicBrainz tags, ratings, or collections when confirmed.

Mitigation: Review each dry-run preview with the user before making a confirm:true call.

Risk: Large browse requests may take longer because MusicBrainz clients are limited to roughly one request per second.

Mitigation: Expect paced responses for large result sets and avoid treating normal delay as failure.

## Reference(s):

- [MusicBrainz](https://musicbrainz.org)

## Skill Output:

**Output Type(s):** [Text, JSON, API Calls, Guidance]

**Output Format:** [JSON tool responses and concise text guidance, including MusicBrainz metadata, Cover Art Archive URLs, dry-run previews, and write receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read operations need no credentials; write operations require OAuth and confirm:true after dry-run review.]

## Skill Version(s):

1.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
