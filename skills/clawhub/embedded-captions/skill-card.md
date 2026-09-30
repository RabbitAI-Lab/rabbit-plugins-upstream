## Description:

Adds styled captions or subtitles to a single-subject talking-head video while preserving the source footage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to transcribe a talking-head clip, choose a caption style, and produce a captioned video with optional behind-subject typography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow processes the source video and audio locally and may download transcription or matting models.

Mitigation: Use only clips approved for local processing and allow model downloads only when acceptable.

Risk: Setup installs project dependencies and approved initialization or update steps may change HyperFrames skills.

Mitigation: Review and approve setup or update actions, and keep the project's dependency lockfile.

Risk: Transcription or subject matting can produce inaccurate captions or visual artifacts.

Mitigation: Review the transcript and preview frames, then check the finished video before publishing.

## Reference(s):

- [Embedded Captions release](https://clawhub.ai/heygen-com/skills/embedded-captions)
- [Caption style catalog](artifact/CATALOG.md)
- [Theme guidance](artifact/themes/README.md)

## Skill Output:

**Output Type(s):** [Configuration, Shell commands, Video]

**Output Format:** [JSON caption plans and styling configuration; captioned MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports standard, cinematic, and themed captions; source footage is preserved.]

## Skill Version(s):

1.0.20 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
