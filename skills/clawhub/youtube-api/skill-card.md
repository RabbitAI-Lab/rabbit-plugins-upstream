## Description: <br>
Use when YouTube data is needed without Google API quotas or OAuth setup: transcripts, video metadata, channel info, search results, playlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search YouTube, retrieve transcripts, inspect video and channel metadata, and browse playlists through TranscriptAPI without setting up Google OAuth or YouTube Data API quota. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow asks an agent to handle and persist a TranscriptAPI key and email verification code. <br>
Mitigation: Use a dedicated TranscriptAPI key stored in the platform secret manager, avoid exposing tokens in logs, and rotate or revoke the key when the skill is no longer needed. <br>
Risk: Using the skill sends YouTube URLs, search queries, channel handles, and playlist IDs to TranscriptAPI. <br>
Mitigation: Install only if you trust TranscriptAPI and are comfortable sharing those YouTube-related inputs with the service. <br>
Risk: The skill depends on internet access to transcriptapi.com and can fail when credentials, credits, headers, or rate limits are not valid. <br>
Mitigation: Confirm the TRANSCRIPT_API_KEY is available, include the required User-Agent header, and handle 401, 402, 403, 408, 422, and 429 responses before relying on results. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI Specification](https://transcriptapi.com/openapi.json) <br>
- [Authentication Setup](references/auth-setup.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/therohitdas/skills/youtube-api) <br>
- [Publisher Profile](https://clawhub.ai/user/therohitdas) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY and internet access to transcriptapi.com.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
