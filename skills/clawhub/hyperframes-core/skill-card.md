## Description:

The HyperFrames Core skill guides agents in building one renderable HyperFrames video project with correct composition structure, timing attributes, media handling, deterministic rendering rules, validation, and related plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create, edit, validate, and render HyperFrames HTML video compositions, including storyboard, script, brief, sub-composition, Tailwind, and frame-worker workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A modified or third-party STORYBOARD.md can cause frame-packet generation to include unintended local Markdown content.

Mitigation: Use this skill with trusted HyperFrames projects, verify blueprint values against the expected catalog, and inspect generated .hyperframes/frame-packets before dispatch or rendering.

Risk: Subagent or background worker execution can proceed beyond the user's intended scope if it is not explicitly controlled.

Mitigation: Keep subagent/background worker use and final rendering as explicit user-controlled actions.

## Reference(s):

- [Brief contract](references/brief-contract.md)
- [Brief format](references/brief-format.md)
- [Composition Patterns](references/composition-patterns.md)
- [Data Attributes Reference](references/data-attributes.md)
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md)
- [Frame worker core contract](references/frame-worker-core.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [Minimal Composition](references/minimal-composition.md)
- [Production loop](references/production-loop.md)
- [Review loop](references/review-loop.md)
- [SCRIPT.md format](references/script-format.md)
- [Storyboard format](references/storyboard-format.md)
- [Sub-Compositions](references/sub-compositions.md)
- [Subagent dispatch](references/subagent-dispatch.md)
- [HyperFrames Tailwind](references/tailwind.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Variables and Media](references/variables-and-media.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, HTML snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce HyperFrames composition files, project plan files, validation commands, and bounded frame-packet guidance.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
