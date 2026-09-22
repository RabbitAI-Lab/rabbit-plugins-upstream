## Description:

Reach for this when YouTube data is needed and Google's Data API is the obstacle: no quota units, no OAuth consent screens, one Bearer key. Covers transcripts, metadata, search, channels and playlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[artemchuikin](https://clawhub.ai/user/artemchuikin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve YouTube transcripts, metadata, search results, channel uploads, and playlist contents through TranscriptOut without Google API quota or OAuth setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow requires a TranscriptOut API key and may ask an agent to handle or persist credentials.

Mitigation: Prefer creating the key yourself in the provider dashboard, store it in a protected secret manager or environment-secret facility, and avoid pasting secrets into ordinary chat.

Risk: Requests send YouTube URLs, search terms, channel handles, playlist IDs, and the API key to TranscriptOut.

Mitigation: Use the skill only for data approved for third-party processing and avoid confidential investigations unless TranscriptOut is approved for that use.

## Reference(s):

- [TranscriptOut](https://transcriptout.com)
- [TranscriptOut API documentation](https://transcriptout.com/docs)
- [TranscriptOut auth setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/artemchuikin/skills/youtube-api)
- [ClawHub publisher profile](https://clawhub.ai/user/artemchuikin)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with curl examples and JSON API response conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPTOUT_API_KEY and internet access to api.transcriptout.com.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
