## Description: <br>
YouTube Full helps agents search YouTube, inspect channels and playlists, and retrieve TranscriptAPI transcripts for video research, summaries, quotes, translations, tutorials, reviews, and creator lookup tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill when YouTube video content is relevant to research or support tasks, including transcript retrieval, channel or playlist browsing, video search, and monitoring recent uploads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow asks an agent to handle TranscriptAPI signup, OTP verification, persistent API key storage, and redaction-sensitive token handling. <br>
Mitigation: Prefer creating the TranscriptAPI account directly, completing verification yourself, and storing TRANSCRIPT_API_KEY through a platform-managed secret store. <br>
Risk: Using the skill sends YouTube-related inputs to TranscriptAPI and can consume account credits. <br>
Mitigation: Install only when third-party TranscriptAPI processing and credit usage are acceptable, and review requested endpoints before running commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/therohitdas/skills/youtube-full) <br>
- [Publisher profile](https://clawhub.ai/user/therohitdas) <br>
- [TranscriptAPI homepage](https://transcriptapi.com) <br>
- [TranscriptAPI OpenAPI specification](https://transcriptapi.com/openapi.json) <br>
- [TranscriptAPI authentication setup](references/auth-setup.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires TRANSCRIPT_API_KEY, internet access to transcriptapi.com, Authorization and User-Agent headers, and TranscriptAPI credits for paid endpoints.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
