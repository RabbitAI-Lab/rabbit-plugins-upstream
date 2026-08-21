## Description:

The HyperFrames composition contract - build one renderable project with composition structure, timing attributes, clips, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, validation, Tailwind projects, and STORYBOARD.md / SCRIPT.md plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build, edit, validate, and render HyperFrames video projects from HTML compositions. It provides the technical contract for deterministic timelines, media handling, project planning documents, review loops, and production handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create or update project-local video files during normal HyperFrames work.

Mitigation: Run it in the intended project workspace and review generated file diffs before accepting or rendering final output.

Risk: The skill may propose local HyperFrames preview, check, or render commands.

Mitigation: Review commands before execution and use the documented check workflow before render.

Risk: Autonomous or background workflows can make broader changes in sensitive workspaces.

Mitigation: Review before enabling autonomous or background workflows where workspace contents are sensitive.

## Reference(s):

- [Minimal Composition](artifact/references/minimal-composition.md)
- [Composition Patterns](artifact/references/composition-patterns.md)
- [Data Attributes Reference](artifact/references/data-attributes.md)
- [Tracks and Clips](artifact/references/tracks-and-clips.md)
- [Creator Editing Recipes](artifact/references/creator-editing-recipes.md)
- [Sub-Compositions](artifact/references/sub-compositions.md)
- [Variables and Media](artifact/references/variables-and-media.md)
- [Determinism, Animation Runtime, and Layout](artifact/references/determinism-rules.md)
- [Full-Screen Motion Pattern](artifact/references/full-screen-motion.md)
- [Storyboard Format](artifact/references/storyboard-format.md)
- [Review Loop](artifact/references/review-loop.md)
- [Production Loop](artifact/references/production-loop.md)
- [Brief Contract](artifact/references/brief-contract.md)
- [Brief Format](artifact/references/brief-format.md)
- [Script Format](artifact/references/script-format.md)
- [Subagent Dispatch](artifact/references/subagent-dispatch.md)
- [Frame Worker Core Contract](artifact/references/frame-worker-core.md)
- [HyperFrames Tailwind](artifact/references/tailwind.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, configuration snippets, project document formats, and local shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update project files and frame-packet markdown in a HyperFrames workspace when used by an agent.]

## Skill Version(s):

1.0.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
