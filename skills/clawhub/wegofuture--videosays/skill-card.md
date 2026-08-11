## Description:

Videosays video transcription, video to text, speech to text, subtitle extraction, caption transcription, YouTube transcript, TikTok transcript, Instagram Reels transcript, X or Twitter video transcript, Douyin transcript, Xiaohongshu transcript, WeChat Channels transcript, and AI agent video transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wegofuture](https://clawhub.ai/user/wegofuture)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit one or more video links or share-text snippets to Videosays, then retrieve transcripts, subtitles, account balance, or transcription history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted video links, share text, and authenticated requests are sent to the Videosays service.

Mitigation: Use the skill only for content the user is comfortable sending to Videosays, and never print or reveal the Videosays API key.

Risk: Transcription can consume account credits, especially when forcing a fresh transcription.

Mitigation: Use the default reuse and status-check workflow, check recent history after ambiguous retries, and use --force-new only when the user explicitly requests a fresh transcription.

Risk: Insufficient credits can pause batch processing while preserving completed tasks.

Mitigation: Report the balance issue and recharge URL, ask the user to top up, then continue the same batch ID after confirmation.

## Reference(s):

- [Videosays website](https://videosays.com/?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill)
- [Videosays API docs](https://videosays.com/docs?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill&utm_content=api_docs)
- [Videosays CLI package](https://www.npmjs.com/package/videosays)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and transcript or subtitle text from the Videosays CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, batch IDs, status messages, transcript text, subtitles, balance information, history entries, or error guidance.]

## Skill Version(s):

1.2.3 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
