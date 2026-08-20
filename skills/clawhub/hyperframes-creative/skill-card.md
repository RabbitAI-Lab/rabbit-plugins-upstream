## Description:

HyperFrames Creative provides non-animation creative direction for HyperFrames videos, including design-spec handling, palettes, typography, narration, beat planning, audio-reactive visuals, composition patterns, and brand or style decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative agents use this skill to choose and audit visual direction for HyperFrames video projects, including frame specs, palettes, typography, narration, beat structure, audio-reactive guidance, composition patterns, and brand or style decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled HTML files can contact Google Fonts or jsDelivr when opened.

Mitigation: Review network access requirements before use, and prefer bundled or locally hosted assets for offline, hermetic, or privacy-sensitive environments.

Risk: The optional contrast report can install and execute npm packages after confirmation or an environment override.

Mitigation: Run optional tooling only in trusted projects, review bootstrap prompts and environment overrides, and pin package versions when bootstrapping is needed.

Risk: Creative-direction outputs can introduce incorrect claims, figures, brand choices, or visual guidance if accepted without review.

Mitigation: Review generated specs, frame content, facts, figures, and brand constraints before deployment.

## Reference(s):

- [HyperFrames Creative ClawHub release](https://clawhub.ai/heygen-com/skills/hyperframes-creative)
- [Design Spec](references/design-spec.md)
- [House Style](references/house-style.md)
- [Video Composition](references/video-composition.md)
- [Visual Styles](references/visual-styles.md)
- [Beat Direction](references/beat-direction.md)
- [Typography](references/typography.md)
- [Audio Reactive](references/audio-reactive.md)
- [Design Picker](references/design-picker.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional code, shell commands, design-spec snippets, and generated frame files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose or use local HTML templates, frame presets, palettes, and optional audit outputs such as contrast reports or audio-band data.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
