## Description:

The HyperFrames composition contract for building one renderable project: composition structure, data-* timing attributes, class="clip", tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to create or modify HyperFrames HTML video compositions with correct timing, media, sub-composition, variable, and validation patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated or copied workflows may rely on unpinned npm commands or remote browser scripts.

Mitigation: Prefer reviewed, pinned local HyperFrames dependencies and lockfiles; vendor or integrity-pin browser scripts used in generated compositions.

Risk: Preview or render commands execute project code and media processing in the local workspace.

Mitigation: Run HyperFrames previews and renders in a constrained workspace and review generated composition files before execution.

Risk: Incorrect timing, media, or deterministic-render patterns can produce blank, silent, or misleading video output.

Mitigation: Run HyperFrames check and snapshots before rendering; keep timelines seekable, media IDs present, and avoid render-time clocks, unseeded randomness, network fetches, and input state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal Composition](references/minimal-composition.md)
- [Composition Patterns](references/composition-patterns.md)
- [Data Attributes](references/data-attributes.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Creator Editing Recipes](references/creator-editing-recipes.md)
- [Sub-Compositions](references/sub-compositions.md)
- [Variables and Media](references/variables-and-media.md)
- [Determinism Rules](references/determinism-rules.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [HyperFrames Tailwind](references/tailwind.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance is scoped to one renderable HyperFrames project at a time.]

## Skill Version(s):

1.0.28 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
