## Description:

Turns a music track into a beat-synced lyric video, slideshow, or kinetic promo, with optional user-supplied images and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketing teams use this skill to plan and produce music-paced videos from a track, with optional images or footage; it can also build a typography-led video without supplied visuals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation and updates may change globally installed skills or bring in unpinned dependencies.

Mitigation: Use an isolated project or container, pin the HyperFrames CLI and Python dependencies where possible, and confirm before skill updates.

Risk: Provider authorization may grant access beyond the current video project.

Mitigation: Confirm before any provider authorization action.

Risk: Rendered visuals may include flashing or strobe effects.

Mitigation: Review the finished video for flashing before sharing it.

## Reference(s):

- [Music to Video skill release](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Frame planning](artifact/references/planning.md)
- [Storyboard format](artifact/references/storyboard-format.md)
- [Asset treatments](artifact/references/montage.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Files]

**Output Format:** [Storyboard and project files, HTML compositions, and a rendered MP4 video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Timing follows the analyzed music; final rendering requires user approval.]

## Skill Version(s):

1.0.25 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
