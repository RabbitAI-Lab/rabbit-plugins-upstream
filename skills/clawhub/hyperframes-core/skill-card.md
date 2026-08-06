## Description: <br>
The HyperFrames composition contract: build one renderable HTML video project with declared timing, seekable animation, framework-owned media playback, deterministic render rules, validation guidance, and storyboard/script planning formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and video-production agents use this skill to author, edit, validate, and review HyperFrames HTML video compositions. It defines the composition structure, timing attributes, clip and track behavior, sub-composition wiring, variables, media handling, deterministic rendering constraints, Tailwind usage, and planning document formats needed to produce a renderable project. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to edit local HyperFrames project files. <br>
Mitigation: Review generated file changes before accepting them, especially timing, media, variables, and project configuration. <br>
Risk: The workflow may run HyperFrames CLI commands during validation and production. <br>
Mitigation: Run commands in the intended project workspace and inspect validation output before rendering. <br>
Risk: Background workers may produce frame files in parallel. <br>
Mitigation: Keep worker outputs scoped to assigned frame files and rely on the orchestrator's assembled-project validation before delivery. <br>
Risk: Render and publish actions can create or distribute final video artifacts. <br>
Mitigation: Require explicit approval before render or publish steps. <br>
Risk: Confirmed preferences may be remembered through related media-use tooling. <br>
Mitigation: Record only confirmed preferences and avoid storing project-specific sensitive details as reusable preferences. <br>


## Reference(s): <br>
- [Minimal Composition](references/minimal-composition.md) <br>
- [Composition Patterns](references/composition-patterns.md) <br>
- [Data Attributes Reference](references/data-attributes.md) <br>
- [Tracks and Clips](references/tracks-and-clips.md) <br>
- [Sub-Compositions](references/sub-compositions.md) <br>
- [Variables and Media](references/variables-and-media.md) <br>
- [Determinism, Animation Runtime, and Layout](references/determinism-rules.md) <br>
- [Full-Screen Motion Pattern](references/full-screen-motion.md) <br>
- [Storyboard Format](references/storyboard-format.md) <br>
- [Review Loop](references/review-loop.md) <br>
- [Production Loop](references/production-loop.md) <br>
- [Brief Contract](references/brief-contract.md) <br>
- [Brief Format](references/brief-format.md) <br>
- [Script Format](references/script-format.md) <br>
- [Subagent Dispatch](references/subagent-dispatch.md) <br>
- [Frame Worker Core](references/frame-worker-core.md) <br>
- [HyperFrames Tailwind](references/tailwind.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with code, HTML, JavaScript, configuration, and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are intended to be applied to local HyperFrames project files and checked with HyperFrames validation commands before render.] <br>

## Skill Version(s): <br>
1.0.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
