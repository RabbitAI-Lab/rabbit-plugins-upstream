## Description:

Packages an existing talking-head video with transcript-timed graphic overlays and renders the composition as an MP4.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add timed titles, quotes, callouts, and picture-in-picture graphics to existing talking-head, interview, or podcast footage while retaining the source video and audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned HyperFrames CLI commands may produce different results across versions.

Mitigation: Pin the HyperFrames CLI version for reproducible runs.

Risk: The default English Whisper model may mis-transcribe non-English footage.

Mitigation: Select an appropriate Whisper model and review the transcript before rendering.

## Reference(s):

- [Talking Head Recut on ClawHub](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Design index](references/DESIGN_INDEX.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands]

**Output Format:** [Markdown guidance, JSON storyboard, HTML composition, and rendered MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates transcript and media project files under videos/<project-name>/; the source clip's audio is preserved.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
