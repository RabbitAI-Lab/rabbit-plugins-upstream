## Description:

Provides TranscriptOut-backed YouTube transcript, metadata, search, channel, and playlist API guidance without requiring Google quota units, OAuth consent screens, or a Google Cloud project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to retrieve YouTube transcripts, metadata, search results, channel uploads, and playlist contents through TranscriptOut's API when Google's YouTube Data API is unavailable or impractical.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to manage TranscriptOut signup and persist a reusable API key, which can expose or over-retain credentials if stored casually.

Mitigation: Provide the key through a scoped secret manager or agent secret store, avoid logging keys or tokens, and remove TRANSCRIPTOUT_API_KEY from local storage when it is no longer needed.

Risk: YouTube searches, video URLs, and account setup details are sent to a third-party TranscriptOut service.

Mitigation: Avoid sending sensitive non-YouTube content in searches or URLs, and review the service before using it for confidential workflows.

## Reference(s):

- [YouTube API ClawHub page](https://clawhub.ai/artemchuikin/skills/youtube-api)
- [TranscriptOut homepage](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut Auth Setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON response examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com; API responses use JSON envelopes.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
