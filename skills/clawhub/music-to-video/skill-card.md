## Description:

Turns a music track or generated mood brief into a beat-synced HyperFrames video such as a lyric video, slideshow, or kinetic promo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to create beat-synced videos from music, optional user media, and generated or supplied visual plans. It guides an agent through audio analysis, storyboard planning, per-frame composition, assembly, verification, and rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow runs HyperFrames commands and local scripts, may install Python audio libraries, writes project files under videos/<project>/, copies user-selected media, and may update related HyperFrames skills.

Mitigation: Review the proposed commands, project path, media sources, and skill-update prompt before execution; run in a dedicated workspace when handling sensitive media.

Risk: Some available visual templates and motion primitives can create flash or strobe effects that may be unsuitable for photosensitive viewers.

Mitigation: Avoid flash and strobe templates for sensitive audiences, or add a safe-mode review before rendering and sharing the video.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/music-to-video)
- [Publisher Profile](https://clawhub.ai/user/heygen-com)
- [Frame Skeleton Reference](references/frame-skeleton.md)
- [Storyboard Format Reference](references/storyboard-format.md)
- [Planning Reference](references/planning.md)
- [Template Catalog](references/template-catalog.md)
- [Motion Primitive Catalog](references/motion-primitive-catalog.md)
- [Asset Treatments Reference](references/montage.md)
- [Frame Worker Reference](sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands, storyboard specifications, JSON analysis files, HTML composition files, and rendered video project artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent workflow guidance and local project files under videos/<project>, including audiomap.json, STORYBOARD.md, per-frame HTML compositions, index.html, and renders/video.mp4.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
