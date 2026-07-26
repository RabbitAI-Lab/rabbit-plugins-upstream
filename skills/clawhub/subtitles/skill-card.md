## Description: <br>
Fetches timestamped YouTube subtitles through TranscriptAPI for reading, translation, language learning, accessibility, and spoken-text extraction. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[therohitdas](https://clawhub.ai/user/therohitdas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve YouTube transcript text or timestamped subtitle segments for reading, translation, synchronized review, language learning, and accessibility workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can ask an agent to create a TranscriptAPI account, handle email verification codes, and persist a long-lived API key. <br>
Mitigation: Prefer creating the account manually, store TRANSCRIPT_API_KEY in a scoped secret manager, and avoid exposing the key in shell output or broad profile files. <br>
Risk: YouTube URLs or video IDs sent for transcription are shared with TranscriptAPI. <br>
Mitigation: Avoid submitting private or sensitive video links unless sharing them with the provider is acceptable. <br>
Risk: Requests depend on a third-party service, available credits, and required headers. <br>
Mitigation: Confirm TRANSCRIPT_API_KEY is valid, include an identifying User-Agent header, monitor provider credits, and retry timeouts once before escalating. <br>


## Reference(s): <br>
- [TranscriptAPI](https://transcriptapi.com) <br>
- [Subtitles Skill on ClawHub](https://clawhub.ai/therohitdas/skills/subtitles) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with curl examples and JSON or plain-text transcript responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a TRANSCRIPT_API_KEY and internet access to transcriptapi.com; transcript requests consume provider credits.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
