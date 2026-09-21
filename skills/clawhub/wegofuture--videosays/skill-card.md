## Description:

Transcribe video links and extract spoken scripts or subtitles from Douyin, Xiaohongshu, Bilibili, YouTube, TikTok, and other supported platforms. Use for single or batch transcription, timestamped transcripts, SRT/VTT export, credit balance, and transcription history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wegofuture](https://clawhub.ai/user/wegofuture)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to submit supported video links or share text to Videosays, then retrieve transcripts, timestamped text, or subtitle files. It also supports account checks, credit balance review, transcription history, and batch transcription workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs the current npm latest release of the Videosays CLI locally, including for login and API-key workflows.

Mitigation: Use a pinned, reviewed CLI version when possible, or run it in an isolated environment with limited credentials.

Risk: The CLI sends configured credentials and submitted links or share text to the configured Videosays API.

Mitigation: Use only links that are appropriate to share with Videosays, keep API keys secret, and prefer accounts with limited scope or credit exposure.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wegofuture/skills/videosays)
- [Videosays website](https://videosays.cn/?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill)
- [Videosays API](https://api.videosays.cn)
- [Videosays API docs](https://videosays.cn/docs?utm_source=videosays_skill&utm_medium=agent_skill&utm_campaign=videosays_agent_skill&utm_content=api_docs)
- [Videosays CLI package](https://www.npmjs.com/package/videosays)
- [Videosays CLI source](https://github.com/xwchris/videosays-agent-tools/tree/main/packages/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and transcript or subtitle text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return original-language transcripts, timestamped timelines, SRT, or VTT depending on the requested CLI format.]

## Skill Version(s):

1.3.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
