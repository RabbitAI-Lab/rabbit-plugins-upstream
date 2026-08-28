## Description:

The HyperFrames composition contract - build one renderable project with composition structure, data-* timing attributes, class="clip", tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, validation, Tailwind projects, and STORYBOARD.md / SCRIPT.md plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation agents use this skill to build and edit one renderable HyperFrames HTML video composition with deterministic timing, media handling, storyboard/script planning artifacts, and validation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Project-local file mutation can change composition, storyboard, script, or frame-packet files.

Mitigation: Review generated plans and diffs before accepting changes, and keep work in a version-controlled project directory.

Risk: Background preview and render tooling can run local services or longer-lived processes.

Mitigation: Start preview/render commands only in trusted projects, stop background processes after review, and run the documented HyperFrames checks before rendering.

Risk: Worker fan-out can delegate frame work with bounded but project-derived packets.

Mitigation: Inspect the storyboard and packet inputs before dispatch, and keep worker output constrained to the intended project files.

Risk: Public publish actions can expose generated video or project outputs.

Mitigation: Require explicit human approval before any render delivery or public publishing step.

## Reference(s):

- [HyperFrames Core Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal Composition](references/minimal-composition.md)
- [Composition Patterns](references/composition-patterns.md)
- [Data Attributes Reference](references/data-attributes.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Creator Editing Recipes](references/creator-editing-recipes.md)
- [Sub-Compositions](references/sub-compositions.md)
- [Variables and Media](references/variables-and-media.md)
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [Storyboard Format](references/storyboard-format.md)
- [Review Loop](references/review-loop.md)
- [Production Loop](references/production-loop.md)
- [Brief Contract](references/brief-contract.md)
- [Brief Format](references/brief-format.md)
- [Script Format](references/script-format.md)
- [Subagent Dispatch](references/subagent-dispatch.md)
- [Frame Worker Core Contract](references/frame-worker-core.md)
- [HyperFrames Tailwind](references/tailwind.md)
- [GSAP CDN](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with HTML, JavaScript, shell command, and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update project-local HyperFrames files and frame-packet artifacts.]

## Skill Version(s):

1.0.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
