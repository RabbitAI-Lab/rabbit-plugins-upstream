## Description:

Use when YouTube data is needed without Google API quotas or OAuth setup, including transcripts, video metadata, channel information, search results, and playlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[therohitdas](https://clawhub.ai/user/therohitdas)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch YouTube transcripts, metadata, channel details, search results, playlists, and related video data through TranscriptAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: YouTube-related requests and prompts may be routed through TranscriptAPI, a third-party service.

Mitigation: Use the skill only when routing YouTube data through TranscriptAPI is intended, and avoid sending private or sensitive content.

Risk: The setup flow can create or persist a TRANSCRIPT_API_KEY in the agent environment.

Mitigation: Prefer manually setting the API key in a trusted secret manager and limit credential persistence to the intended runtime.

Risk: Broad activation language may lead an agent to use the external service whenever YouTube content appears useful.

Mitigation: Confirm external API use for privacy-sensitive work and withhold or disable TRANSCRIPT_API_KEY where automatic calls are not desired.

## Reference(s):

- [TranscriptAPI homepage](https://transcriptapi.com)
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json)
- [TranscriptAPI authentication setup](references/auth-setup.md)
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/youtube-api)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, text]

**Output Format:** [Markdown guidance with inline curl examples and environment variable configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses TRANSCRIPT_API_KEY and TranscriptAPI HTTP endpoints for YouTube data access.]

## Skill Version(s):

1.6.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
