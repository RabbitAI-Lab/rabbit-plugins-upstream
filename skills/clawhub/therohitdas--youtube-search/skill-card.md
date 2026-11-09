## Description:

Use when the user wants to find YouTube content on any topic: searching for videos or channels, finding creators who cover a subject, discovering tutorials, talks, or expert discussions, or looking up a channel by name or handle.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to search YouTube videos, channels, playlists, and channel-specific content through TranscriptAPI, then optionally retrieve transcripts for discovered videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may ask the agent to collect and persist TranscriptAPI credentials, email, and OTP data.

Mitigation: Use a trusted secret manager or existing API key where possible, avoid pasting credentials into chat, and confirm where any persistent secret will be stored and how it can be revoked.

Risk: The skill depends on outbound requests to TranscriptAPI for YouTube search and transcript retrieval.

Mitigation: Install and run it only when third-party API access is acceptable for the user's workflow and data handling expectations.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/therohitdas/skills/youtube-search)
- [Publisher profile](https://clawhub.ai/user/therohitdas)
- [TranscriptAPI homepage](https://transcriptapi.com)
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json)
- [TranscriptAPI authentication setup](references/auth-setup.md)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with curl commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
