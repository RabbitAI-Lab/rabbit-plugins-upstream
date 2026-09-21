## Description:

The HyperFrames composition contract - build one renderable project. Use for composition structure, the data-* timing attributes, class="clip", tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, and validation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to author, edit, and validate HyperFrames HTML video compositions with deterministic timing, media handling, tracks, clips, variables, sub-compositions, and render checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated commands may invoke HyperFrames tooling from an unpinned package version.

Mitigation: Use a reviewed project-local dependency or pin the hyperframes package version in the project lockfile before running automation.

Risk: The preview --background workflow can leave a local preview server running after the command returns.

Mitigation: Track the preview process during review and stop it when validation is complete.

Risk: Non-deterministic composition code can produce inconsistent video frames.

Mitigation: Follow the skill's determinism rules, avoid render-time clocks, unseeded random values, network fetches, and input-state-dependent visuals, then run HyperFrames validation before rendering.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Publisher profile](https://clawhub.ai/user/heygen-com)
- [Composition Patterns](references/composition-patterns.md)
- [Creator Editing Recipes](references/creator-editing-recipes.md)
- [Data Attributes Reference](references/data-attributes.md)
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [Minimal Composition](references/minimal-composition.md)
- [Sub-Compositions](references/sub-compositions.md)
- [HyperFrames Tailwind](references/tailwind.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Variables and Media](references/variables-and-media.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces authoring guidance for HyperFrames projects; it does not render video directly.]

## Skill Version(s):

1.0.35 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
