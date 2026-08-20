## Description:

HyperFrames Core provides the composition contract for building one renderable HyperFrames project, covering structure, timing attributes, clips, tracks, sub-compositions, variables, framework-owned media playback, deterministic rendering, validation, Tailwind projects, and STORYBOARD.md/SCRIPT.md planning formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill when an agent needs to create or edit a renderable HyperFrames video project with deterministic HTML composition, timeline, media, and validation contracts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agents using this skill may create or modify HyperFrames project files and run preview, check, or render commands.

Mitigation: Review generated project files and HyperFrames CLI actions before deployment, especially for production or sensitive renders.

Risk: The artifact includes CDN script examples that may be unsuitable for locked-down production rendering.

Mitigation: Prefer locally managed dependencies or pinned internal assets for production and sensitive rendering workflows.

Risk: The skill may coordinate worker agents and background preview, publish, or recipe-memory actions.

Mitigation: Review and approve worker dispatch, background preview, publish, and recipe-memory actions before allowing them to run.

## Reference(s):

- [Brief Contract](references/brief-contract.md)
- [Brief Format](references/brief-format.md)
- [Composition Patterns](references/composition-patterns.md)
- [Creator Editing Recipes](references/creator-editing-recipes.md)
- [Data Attributes Reference](references/data-attributes.md)
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md)
- [Frame Worker Core Contract](references/frame-worker-core.md)
- [Full-Screen Motion Pattern](references/full-screen-motion.md)
- [Minimal Composition](references/minimal-composition.md)
- [Production Loop](references/production-loop.md)
- [Review Loop](references/review-loop.md)
- [SCRIPT.md Format](references/script-format.md)
- [Storyboard Format](references/storyboard-format.md)
- [Sub-Compositions](references/sub-compositions.md)
- [Subagent Dispatch](references/subagent-dispatch.md)
- [HyperFrames Tailwind](references/tailwind.md)
- [Tracks and Clips](references/tracks-and-clips.md)
- [Variables and Media](references/variables-and-media.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, and CLI command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deterministic render constraints, validation steps, and frame-packet generation helpers.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
