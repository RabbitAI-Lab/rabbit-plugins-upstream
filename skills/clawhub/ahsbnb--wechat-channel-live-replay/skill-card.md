## Description:

Downloads WeChat Channels live replay videos by account keyword and optional date, and can transcribe the downloaded replay for follow-up analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ahsbnb](https://clawhub.ai/user/ahsbnb)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to retrieve WeChat Channels live replay media, optionally transcribe it, and prepare inputs for livestream review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports loosely bounded file writing and media download handling.

Mitigation: Run in a contained workspace, prefer a fixed output directory, and review generated file paths before use.

Risk: Path-like keyword values may affect where transcripts and reports are written.

Mitigation: Avoid path-like keyword values and validate keywords before execution.

Risk: Media URLs, redirects, and download sizes may not be sufficiently constrained.

Mitigation: Validate media URLs and redirects, cap download size, and review downloaded content before downstream processing.

Risk: The skill requires a TikHub token and third-party API access.

Mitigation: Use only a TikHub token appropriate for this workflow and rotate or revoke it if exposure is suspected.

Risk: Dependencies and local tools affect execution behavior.

Mitigation: Pin Python dependencies, verify ffmpeg installation, and keep temporary audio cleanup under review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ahsbnb/skills/wechat-channel-live-replay)
- [TikHub API](https://api.tikhub.io/api/v1)
- [FFmpeg Downloads](https://ffmpeg.org/download.html)

## Skill Output:

**Output Type(s):** [Files, Text, JSON]

**Output Format:** [Downloaded MP4 replay, transcript text file, JSON task report, and console status output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a TikHub token and ffmpeg; transcription uses Whisper when not skipped.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
