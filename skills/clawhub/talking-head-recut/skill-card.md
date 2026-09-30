## Description:

Packages existing talking-head, interview, or podcast videos with transcript-timed graphic overlays while preserving the original clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video editors and content creators use this skill to add designed, transcript-synchronized titles, quotes, and data callouts to existing footage and render a finished video.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running video tools and HyperFrames through npx can execute software in the local environment.

Mitigation: Review commands and use a pinned or pre-vetted HyperFrames version where reproducible builds are required.

Risk: Missing referenced font assets may change the appearance of rendered overlays.

Mitigation: Check available font assets and inspect a snapshot before the final render.

Risk: The skill may update itself when requested.

Mitigation: Confirm any skill update explicitly before running it.

## Reference(s):

- [Talking Head Recut on ClawHub](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Visual design library](references/DESIGN_INDEX.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Files]

**Output Format:** [Markdown guidance, HTML composition and cards, JSON storyboard and transcript, and rendered MP4]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates intermediate files and a rendered video in videos/<project>.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
