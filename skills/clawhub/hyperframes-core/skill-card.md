## Description:

HyperFrames Core is a technical contract for building one renderable HyperFrames project, covering composition structure, timing attributes, clips, tracks, sub-compositions, media playback, deterministic rendering, validation, Tailwind projects, and plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video workflow agents use this skill to build or edit HyperFrames HTML video compositions with deterministic timelines, media playback rules, validation steps, and supporting brief, storyboard, and script files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video workflows may create or modify project files and produce frame-worker packets.

Mitigation: Review generated files before deployment and run the documented HyperFrames validation checks before rendering.

Risk: External media-generation tools may receive prompts or project assets.

Mitigation: Confirm which providers are used for sensitive projects and avoid sending confidential prompts or assets to providers that are not approved.

Risk: Missing font support can alter non-Latin text during video generation.

Mitigation: Supply fonts that support the required language and verify snapshots or previews before final render.

## Reference(s):

- [HyperFrames Core](SKILL.md)
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
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-core)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON/YAML, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide creation of HyperFrames project files, storyboard and script documents, frame packets, validation commands, previews, and render commands.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
