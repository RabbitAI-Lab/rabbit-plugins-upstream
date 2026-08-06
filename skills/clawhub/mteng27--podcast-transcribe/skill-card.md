## Description: <br>
Downloads podcast audio from RSS feeds, transcribes episodes with the AuralWise API, and generates transcripts, show notes, subtitles, and episode overviews. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mteng27](https://clawhub.ai/user/mteng27) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and content teams use this skill to download podcast episodes from RSS feeds, produce searchable transcripts, and generate concise episode overview files for later retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Podcast audio and speech content may be sent to a paid third-party transcription service. <br>
Mitigation: Confirm the podcast content, privacy expectations, and AuralWise terms before transcription; use download-only mode when transcription is not intended. <br>
Risk: The skill includes a referral signup URL for the transcription service. <br>
Mitigation: Use a neutral AuralWise signup or settings URL when referral tracking is unwanted. <br>
Risk: Episode filtering and test mode can process a subset of episodes rather than the full feed. <br>
Mitigation: Start with test or download-only mode and review the selected episodes and pipeline state before batch transcription. <br>
Risk: The AuralWise API key may be stored in a local .env file. <br>
Mitigation: Keep API keys out of shared repositories and logs, and prefer environment-specific secret handling for shared or production workspaces. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mteng27/skills/podcast-transcribe) <br>
- [AuralWise API reference](references/auralwise_api.md) <br>
- [RSS feed discovery methods](references/rss_discovery.md) <br>
- [AuralWise API documentation](https://auralwise.cn/api-docs) <br>
- [Apple iTunes Search API podcast lookup](https://itunes.apple.com/search?term={podcast_name}&media=podcast&limit=5) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated text, Markdown, SRT, log, and JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local podcast audio, show notes, plain-text transcripts, timestamped Markdown transcripts, SRT subtitles, overview Markdown files, pipeline logs, and resume state.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
