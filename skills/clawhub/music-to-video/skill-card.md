## Description:

Turn a music track from audio, video, or a generated mood brief into a beat-synced lyric video, slideshow, or kinetic promo, with optional user media cut to the same beat grid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, developers, and video production agents use this skill to convert music into beat-synced HyperFrames videos. It guides setup, audio analysis, storyboard planning, frame composition, assembly, verification, and MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable tool and package execution may update global HyperFrames skills or run npm/PyPI code with behavior that changes over time.

Mitigation: Run the skill in an isolated workspace and Python environment, and review package/tool actions before using it for important projects.

Risk: Project-file handling, path confinement, and generated HTML escaping issues may affect projects or media bundles from untrusted sources.

Mitigation: Review existing STORYBOARD.md, frame.md, project files, and media inputs before execution, and avoid untrusted inputs until those issues are fixed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Frame skeleton](references/frame-skeleton.md)
- [Planning](references/planning.md)
- [Storyboard format](references/storyboard-format.md)
- [Template catalog](references/template-catalog.md)
- [Motion-primitive catalog](references/motion-primitive-catalog.md)
- [Montage](references/montage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON analysis files, HTML composition files, project configuration, and MP4 render outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces staged project files such as audiomap.json, STORYBOARD.md, frame.md, compositions/frames/*.html, index.html, and renders/video.mp4.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
