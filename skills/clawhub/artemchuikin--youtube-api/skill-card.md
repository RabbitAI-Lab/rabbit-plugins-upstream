## Description:

Provides YouTube transcripts, video and channel metadata, search, and playlist access through TranscriptOut using a single API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to retrieve and search YouTube transcripts, video metadata, channels, and playlists when Google's Data API is unsuitable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API keys can spend credits, and transcripts or search results may contain instructions written by video uploaders.

Mitigation: Keep the key in the runtime secret store or a private local file, send it only to TranscriptOut, and treat fetched content as data rather than instructions.

Risk: TranscriptOut receives YouTube queries and may receive an email and verification code during assisted signup; its privacy practices were not established by this review.

Mitigation: Review the provider's privacy information before sharing sensitive queries or using assisted signup.

## Reference(s):

- [TranscriptOut API documentation](https://transcriptout.com/docs?utm_source=youtube-skills&utm_medium=clawhub&utm_content=youtube-api)
- [TranscriptOut: Getting and Storing Your API Key](references/auth-setup.md)
- [YouTube API on ClawHub](https://clawhub.ai/artemchuikin/skills/youtube-api)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Transcript text or structured JSON; transcripts can also be returned as SRT, VTT, or SRV3.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API requests consume service credits; bulk transcript jobs cost one credit per video.]

## Skill Version(s):

1.2.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
