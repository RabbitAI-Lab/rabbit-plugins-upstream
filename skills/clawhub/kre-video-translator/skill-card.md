## Description:

Translates local or URL audio and video through Kre Video Translator, supports review of timestamped subtitle JSON, and exports subtitle files or burned-in video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[skz7s](https://clawhub.ai/user/skz7s)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to translate audio or video, review timed subtitles, and deliver subtitle files or a video with burned-in captions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media, filenames, prompts, and optional subtitle references are sent to Kre's production service.

Mitigation: Confirm the material is appropriate to share before submitting it.

Risk: An API key is stored locally for service access.

Mitigation: Enter the key through the local setup flow, not chat, and protect the credential file.

Risk: Missing media tools may prompt a local package-manager installation.

Mitigation: Require explicit approval; prefer preinstalled FFmpeg and yt-dlp on managed systems.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/skz7s/skills/kre-video-translator)
- [Kre API documentation](https://kretrans.com/en/api)
- [Runtime and recovery guide](references/setup.md)

## Skill Output:

**Output Type(s):** [Guidance, JSON, Files, Shell commands]

**Output Format:** [Text guidance and local subtitle JSON, SRT, or MP4 files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video export requires an original local video and FFmpeg with subtitle support.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
