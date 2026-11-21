## Description:

Retrieves watermark-free video download links from Douyin share URLs, downloads videos, and can extract spoken content to files.

This skill is for research and development only.

## Publisher:

[yzfly](https://clawhub.ai/user/yzfly)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users processing Douyin links can retrieve video details, download clips, or transcribe speech into Markdown files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unchecked share link may lead to an unintended network destination.

Mitigation: Use trusted Douyin share links, check where they lead before running the skill, and stop if the destination is unexpected.

Risk: The transcription feature sends downloaded audio to SiliconFlow for speech recognition.

Mitigation: Only transcribe videos you are authorized to share, and avoid submitting sensitive content.

## Reference(s):

- [SiliconFlow speech transcription API](https://api.siliconflow.cn/v1/audio/transcriptions)
- [SiliconFlow API key portal](https://cloud.siliconflow.cn/)
- [Douyin Video on ClawHub](https://clawhub.ai/yzfly/skills/douyin-video)

## Skill Output:

**Output Type(s):** [Text, Markdown, Video files]

**Output Format:** [Video details as text, transcripts as Markdown, and downloaded videos as MP4 files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Transcription requires a SiliconFlow API key and FFmpeg; video details and downloads do not require the API key.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
