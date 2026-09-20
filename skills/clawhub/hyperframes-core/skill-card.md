## Description:

The HyperFrames composition contract: build one renderable project using composition structure, timing attributes, clips, tracks, sub-compositions, variables, framework-owned media playback, deterministic render rules, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to author, edit, and validate HyperFrames HTML compositions for video rendering. It helps produce composition code, timing structures, media wiring, deterministic animation patterns, and validation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bare npx command examples can resolve an unpinned HyperFrames CLI version.

Mitigation: Use a lockfile-managed local HyperFrames CLI or pin the npm package version before running examples.

Risk: The preview --background command leaves a local preview server running after the command returns.

Mitigation: Stop the background preview server after review or run preview in a managed terminal session.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal Composition](references/minimal-composition.md)
- [Composition Patterns](references/composition-patterns.md)
- [Data Attributes Reference](references/data-attributes.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Creator Editing Recipes](references/creator-editing-recipes.md)
- [Sub-Compositions](references/sub-compositions.md)
- [Variables and Media](references/variables-and-media.md)
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [HyperFrames Tailwind](references/tailwind.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HyperFrames composition structure, data attributes, media wiring, validation steps, and editing recipes.]

## Skill Version(s):

1.0.34 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
