## Description:

Packages an existing talking-head video with transcript-timed graphic overlays while preserving the underlying clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and editors use this skill to add timed titles, callouts, quotes, and picture-in-picture graphics to an existing interview or talking-head clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live npx resolution may run a changed HyperFrames version.

Mitigation: Use a pinned or locally installed HyperFrames version before processing videos.

Risk: Rendering generated HTML alongside sensitive video may expose content to unreviewed code.

Mitigation: Review generated HTML before rendering sensitive videos.

## Reference(s):

- [Talking Head Recut release](https://clawhub.ai/heygen-com/skills/talking-head-recut)
- [Design index](references/DESIGN_INDEX.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown guidance with HTML, JSON, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides creation of transcript-aligned graphics and a rendered MP4 from a supplied video.]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
