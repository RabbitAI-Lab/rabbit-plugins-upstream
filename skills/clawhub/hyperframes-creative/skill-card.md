## Description:

Provides creative direction for HyperFrames videos, including design specifications, palettes, typography, narration, composition, and beat planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan the visual style, storytelling, narration, and frame composition of HyperFrames videos while respecting an existing project design specification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The interactive design picker can expose project files through an unauthenticated web server.

Mitigation: Bind the server to 127.0.0.1, serve only the .hyperframes directory, and stop it promptly after selection.

Risk: Optional local creative tools can invoke ffmpeg, Node, browser capture, or npm package bootstrapping.

Mitigation: Review and approve local tool execution and any package installation before running these workflows.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/hyperframes-creative)
- [Design specification guide](artifact/references/design-spec.md)
- [Visual styles](artifact/references/visual-styles.md)
- [Design picker](artifact/references/design-picker.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Configuration instructions]

**Output Format:** [Markdown creative direction and design specifications, with optional HTML/CSS examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose frame presets, palettes, typography, and narration; does not render video by itself.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
