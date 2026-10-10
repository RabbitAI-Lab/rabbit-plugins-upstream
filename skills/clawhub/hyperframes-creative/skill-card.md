## Description:

Provides non-animation creative direction for HyperFrames videos, including design specs, palettes, typography, narration, beat planning, and composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators and developers use this skill to plan visual style, brand-consistent frames, narration, and pacing for HyperFrames video projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media helpers and project writes can change files or run resource-intensive processing.

Mitigation: Run helpers and ffmpeg only at the user's direction; review output paths and commands first.

Risk: Optional helper-package or font downloads introduce external dependencies.

Mitigation: Approve downloads explicitly and pin HYPERFRAMES_SKILL_PKG_VERSION when bootstrapping outside a bundled install.

Risk: The interactive design picker may temporarily serve a local page.

Mitigation: Start it only when needed and stop the local server after use.

## Reference(s):

- [HyperFrames Creative release](https://clawhub.ai/heygen-com/skills/hyperframes-creative)
- [Design spec guidance](references/design-spec.md)
- [House style](references/house-style.md)
- [Video composition](references/video-composition.md)
- [Beat direction](references/beat-direction.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions, Shell commands]

**Output Format:** [Markdown guidance and project-specific design specifications or frame code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include palettes, storyboards, narration, and layout recommendations.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
