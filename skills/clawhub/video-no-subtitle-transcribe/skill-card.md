## Description:

Fallback transcription for videos without subtitles: downloads audio from supported video sources or accepts local media, then uses faster-whisper locally to produce a full timestamped transcript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bccbok](https://clawhub.ai/user/bccbok)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and content reviewers use this skill when a video has no usable subtitles or subtitle retrieval fails, and they need a local timestamped transcript for review or summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads media from user-provided URLs.

Mitigation: Use it only with media the user is allowed to access and transcribe.

Risk: The skill may download and cache a roughly 483 MB speech model locally.

Mitigation: Confirm local storage and network expectations before first use; rely on the documented integrity check for the cached model.

Risk: Transcription can run for a long time and may be inaccurate when audio is noisy, fast, or in the wrong language.

Mitigation: Set the correct language option, allow long-running jobs to complete, and review the timestamped output before using it in summaries or decisions.

## Reference(s):

- [Server-resolved source repository](https://github.com/BCCBOK/video-no-subtitle-transcribe)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [ModelScope faster-whisper small model](https://modelscope.cn/models/Systran/faster-whisper-small/resolve/master/model.bin)
- [Companion ClawHub skill: bilibili-youtube-watcher](https://clawhub.ai/donnycui/skills/bilibili-youtube-watcher)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell commands and timestamped transcript text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript lines use [start-end seconds] timestamps; runtime can be long for large media, and the local model may be downloaded on first use.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact frontmatter and changelog show 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
