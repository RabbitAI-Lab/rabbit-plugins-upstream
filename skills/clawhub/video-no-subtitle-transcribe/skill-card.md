## Description:

Fallback transcription for videos without subtitles: it downloads audio with yt-dlp, transcribes locally with faster-whisper, and produces a timestamped transcript.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bccbok](https://clawhub.ai/user/bccbok)

### License/Terms of Use:

MIT

## Use Case:

Developers, researchers, and content reviewers use this skill when a video has no captions or subtitle retrieval fails, and they need a local timestamped transcript for downstream reading or summarization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill downloads audio from user-provided video URLs and downloads a local Whisper model on first use.

Mitigation: Run it only where those network connections are allowed, and review expected video and model hosts before use in constrained environments.

Risk: Proxy routing can be supplied by --proxy, environment variables, or OpenClaw configuration.

Mitigation: Set --proxy explicitly, or clear inherited proxy settings when routing, privacy, or compliance requirements matter.

Risk: Transcription quality depends on source audio clarity and the local small Whisper model.

Mitigation: Review the timestamped transcript against the source audio before relying on summaries or decisions.

## Reference(s):

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [faster-whisper](https://github.com/SYSTRAN/faster-whisper)
- [faster-whisper small model on ModelScope](https://modelscope.cn/models/Systran/faster-whisper-small/resolve/master/model.bin)
- [Companion subtitle skill](https://clawhub.ai/donnycui/skills/bilibili-youtube-watcher)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Guidance]

**Output Format:** [Timestamped plain text transcript with supporting Markdown instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcript lines use [start-end seconds] followed by recognized speech text.]

## Skill Version(s):

1.0.2 (source: frontmatter and changelog, released 2026-08-15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
