## Description:

YouTube Data helps agents retrieve structured YouTube video metadata, transcripts, search results, channel uploads, and playlist contents through TranscriptOut without a Google Cloud project or quota units.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for YouTube transcripts, video metadata, search results, channel upload history, and playlist data for media research and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends YouTube requests through TranscriptOut, a third-party service.

Mitigation: Install only when use of TranscriptOut is acceptable for the intended YouTube links, searches, channels, playlists, and transcript requests.

Risk: Broad automatic triggering can send sensitive searches, private or unlisted links, channel targets, playlists, or bulk jobs before the user has reviewed them.

Mitigation: Require explicit confirmation before sensitive or bulk requests are sent.

Risk: The credential setup flow can expose or persist API keys unsafely if handled automatically.

Mitigation: Create the API key directly, provide it through a trusted secret manager, and avoid echoing or storing secrets in plain shell output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/youtube-data)
- [TranscriptOut homepage](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut authentication setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with curl command examples and JSON API response envelopes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com; TranscriptOut credits are consumed by most data endpoints.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
