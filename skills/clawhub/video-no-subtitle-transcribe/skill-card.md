## Description:

Fallback transcription for videos without subtitles by downloading audio with yt-dlp, transcribing locally with faster-whisper, and producing a timestamped transcript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bccbok](https://clawhub.ai/user/bccbok)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and content analysts use this skill when a video has no usable subtitles and they need a local timestamped transcript for review, summarization, or follow-up analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The script contacts the source video site through yt-dlp and downloads a Whisper model from ModelScope.

Mitigation: Use the skill only where those network calls are acceptable, and review proxy and network settings before running it on sensitive workloads.

Risk: The optional browser fallback shares a YouTube URL with youtube.iiilab.com after local yt-dlp attempts fail.

Mitigation: Avoid that fallback for private, unlisted, sensitive, or client-owned videos unless the user explicitly accepts the disclosure.

Risk: Local Whisper transcription can produce errors when audio is noisy, fast, or ambiguous.

Mitigation: Review timestamped segments against the source audio before relying on summaries or decisions derived from the transcript.

## Reference(s):

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [Systran faster-whisper-small model on ModelScope](https://modelscope.cn/models/Systran/faster-whisper-small/resolve/master/model.bin)
- [Companion subtitle skill](https://clawhub.ai/donnycui/skills/bilibili-youtube-watcher)
- [ClawHub skill page](https://clawhub.ai/bccbok/skills/video-no-subtitle-transcribe)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain-text timestamped transcript with Markdown usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript lines use [start-end seconds] text segments; local transcription speed depends on audio length and CPU performance.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
