## Description:

Transcribes local audio and video files, public single-item media links, and podcast episodes by reusing existing captions when available and using VoiceFlow ASR only when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niuzb](https://clawhub.ai/user/niuzb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and employees use this skill to obtain raw transcripts from supported local media files, public single-video links, and public podcast episode URLs. It is intended for caption-first extraction with ASR fallback when usable page text is unavailable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media may be sent to VoiceFlow or signed storage when captions are unavailable.

Mitigation: Use caption extraction first, avoid private or sensitive media unless the user accepts the service path, and proceed with ASR only after authorization is available.

Risk: The skill can change the host environment by relying on FFmpeg behavior, storing VoiceFlow credentials, or caching yt-dlp.

Mitigation: Before first use, confirm whether FFmpeg may be installed and where credentials and the yt-dlp cache will be stored.

Risk: Persistent transcription credentials could expose account access if mishandled.

Mitigation: Prefer the documented token flow, keep tokens out of command arguments and logs, and use the configured credential directory with restrictive file permissions.

## Reference(s):

- [Xiaoyuzhou single-episode transcription reference](references/xiaoyuzhou.md)
- [VoiceFlow dashboard](https://audioflow123.com/dashboard)
- [yt-dlp installation documentation](https://github.com/yt-dlp/yt-dlp/wiki/Installation)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text transcript or JSON transcript payload, with brief Markdown guidance for authorization or failure handling.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns obtained transcript text verbatim and removes at most the trailing command-output newline.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
