## Description:

HyperFrames Creative provides non-animation creative direction for HyperFrames videos, including design specs, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand and style decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and creative technologists use this skill to turn HyperFrames video requests into brand-aware visual direction, frame design specs, palettes, typography choices, narration structure, beat plans, and composition guidance. It is intended for non-animation creative planning after the HyperFrames technical contract is already in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creative preview files may contact third-party font or script services such as Google Fonts or jsDelivr when opened.

Mitigation: For offline or stricter environments, vendor fonts and GSAP locally before using the preview files.

Risk: Optional helper workflows may start a local web server or bootstrap npm packages after confirmation.

Mitigation: Review helper commands before running them and avoid dynamic font-discovery or package-bootstrap workflows where external network access is not acceptable.

## Reference(s):

- [House Style](references/house-style.md)
- [Video Composition](references/video-composition.md)
- [Design Spec](references/design-spec.md)
- [Visual Style Library](references/visual-styles.md)
- [Beat Direction](references/beat-direction.md)
- [Typography](references/typography.md)
- [Composition Patterns](references/composition-patterns.md)
- [Design Adherence](references/design-adherence.md)
- [Audio-Reactive Animation](references/audio-reactive.md)
- [Design Picker](references/design-picker.md)
- [Prompt Expansion](references/prompt-expansion.md)
- [Story Spine](references/story-spine.md)
- [Narration and Script](references/narration.md)
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-creative)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets, design-token references, shell commands, and optional generated JSON or preview files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce frame-spec guidance, palette and typography recommendations, contrast reports, audio-band JSON, and design-picker previews when helper workflows are used.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
