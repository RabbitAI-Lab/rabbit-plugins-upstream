## Description:

Reach for this when structured YouTube data is the goal: video metadata, transcripts for analysis, channel upload history, search results or playlist contents, with no Google Cloud project and no quota units. Triggers on YouTube links, creator names and topic research even when unstated. Skip it for uploads and text-only research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve YouTube metadata, transcripts, search results, channel uploads, and playlist contents for research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key is sent to TranscriptOut and API requests can spend the account's service credits.

Mitigation: Prefer the runtime secret store; otherwise use the private key file, remove shell startup entries when finished, and revoke the key when it is no longer needed.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut API key setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Structured YouTube data]

**Output Format:** [JSON metadata and search results, plus transcripts in text or subtitle formats]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript formats can include timestamps; results may be paginated.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
