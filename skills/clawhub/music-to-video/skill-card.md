## Description:

Turn a music track into a beat-synced video, including a lyric video, slideshow, or kinetic promo, with pacing driven by the analyzed music and optional user-supplied media cut to the same beat grid.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative operators use this skill to turn a music source, optional visual assets, and a brief into a beat-synced HyperFrames video workflow. The skill guides setup, audio analysis, storyboard planning, frame composition, assembly, verification, and MP4 rendering.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Runtime package fetching and HyperFrames skill updates can change the code or dependencies used during execution.

Mitigation: Pin the HyperFrames CLI and Python dependencies, review updates separately, and run the workflow in a project-scoped sandbox.

Risk: Asset staging has a path weakness that could affect where input assets are copied.

Mitigation: Use only the documented --into public staging path until the traversal issue is fixed, and review staged files before rendering.

## Reference(s):

- [Planning](artifact/references/planning.md)
- [Frame Skeleton](artifact/references/frame-skeleton.md)
- [Storyboard Format](artifact/references/storyboard-format.md)
- [Template Catalog](artifact/references/template-catalog.md)
- [Motion Primitive Catalog](artifact/references/motion-primitive-catalog.md)
- [Montage](artifact/references/montage.md)
- [Frame Worker](artifact/sub-agents/frame-worker.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, storyboard files, HTML compositions, JSON audio analysis, and rendered video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a project workflow that culminates in an assembled HyperFrames video and MP4 render.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
