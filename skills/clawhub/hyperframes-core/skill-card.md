## Description: <br>
HyperFrames Core provides the composition contract for building one renderable HyperFrames project, covering DOM timing attributes, clips, tracks, sub-compositions, variables, media playback, deterministic rendering, validation, Tailwind projects, and plan formats. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to author, edit, and validate HyperFrames video compositions and related planning files. It helps agents produce renderable HTML/CSS/JavaScript compositions, storyboard and script documents, validation commands, and project-scoped guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to edit composition, storyboard, brief, and script files and run local HyperFrames commands. <br>
Mitigation: Use it only in intended HyperFrames projects, review project-scoped changes, and run the documented HyperFrames validation commands before rendering or delivery. <br>
Risk: Non-Latin or multilingual visible text can render incorrectly if the project lacks matching shipped fonts. <br>
Mitigation: Provide project-shipped fonts with the needed script coverage before rendering non-Latin text. <br>
Risk: Incorrect timing, media ownership, duplicate IDs, or non-deterministic animation behavior can produce blank, inconsistent, or misleading video frames. <br>
Mitigation: Follow the deterministic-rendering, media, and ID rules in the references and verify output with snapshots, preview, and HyperFrames checks. <br>


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
- [The Review Loop](references/review-loop.md) <br>
- [Production Loop](references/production-loop.md) <br>
- [Brief Contract](references/brief-contract.md) <br>
- [Brief Format](references/brief-format.md) <br>
- [Script Format](references/script-format.md) <br>
- [Subagent Dispatch](references/subagent-dispatch.md) <br>
- [Frame Worker Core Contract](references/frame-worker-core.md) <br>
- [HyperFrames Tailwind](references/tailwind.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce project-scoped HyperFrames composition files, planning documents, frame-worker packets, and validation commands.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
