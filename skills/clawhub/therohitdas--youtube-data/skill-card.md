## Description:

Use when structured YouTube data is needed: pasted video/channel/playlist links, transcripts for analysis, video metadata, channel upload history, search results, or playlist contents without Google API quotas or OAuth.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to retrieve YouTube transcripts, metadata, channel uploads, search results, playlists, and related structured video data through TranscriptAPI. It is suited for YouTube content analysis and discovery workflows, not YouTube uploads, account management, or written-source-only research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow may involve an agent handling a TranscriptAPI email signup, OTP, API key, and persistent credential storage.

Mitigation: Create the TranscriptAPI account yourself when practical, provide the API key through a scoped secret manager, and avoid pasting secrets or OTPs into chat logs.

Risk: Requests send YouTube URLs, search terms, and channel or playlist identifiers to TranscriptAPI.

Mitigation: Use the skill only for content you are comfortable sharing with TranscriptAPI, and review requests before the agent sends sensitive research topics or private links.

Risk: TranscriptAPI requests consume credits, and paginated or sorted channel requests can use one credit per page.

Mitigation: Set clear limits before broad searches or pagination, and prefer free endpoints such as video info, channel resolve, or channel latest when they satisfy the task.

## Reference(s):

- [TranscriptAPI](https://transcriptapi.com)
- [TranscriptAPI OpenAPI Specification](https://transcriptapi.com/openapi.json)
- [TranscriptAPI Authentication Setup](references/auth-setup.md)
- [ClawHub Skill Page](https://clawhub.ai/therohitdas/skills/youtube-data)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and inline shell commands for TranscriptAPI requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires internet access to transcriptapi.com and a TRANSCRIPT_API_KEY for API requests.]

## Skill Version(s):

1.6.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
