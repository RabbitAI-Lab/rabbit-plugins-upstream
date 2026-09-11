## Description:

The HyperFrames composition contract: build one renderable project with composition structure, data attributes, clips, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, validation, Tailwind support, and STORYBOARD.md / SCRIPT.md plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation agents use this skill to author, edit, and validate HyperFrames HTML video compositions with deterministic timing, media, sub-composition, and storyboard conventions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can steer agents into delegated worker execution.

Mitigation: Approve delegated worker workflows before allowing them to run, and keep worker scope limited to trusted HyperFrames project files.

Risk: The skill can use mutable external tooling such as on-demand npx commands.

Mitigation: Prefer a locally installed, pinned HyperFrames CLI over on-demand npx execution.

Risk: Untrusted STORYBOARD.md content can influence generated compositions and worker packets.

Mitigation: Review STORYBOARD.md and related project inputs before executing build, preview, render, or delegated worker steps.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
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
- [The Review Loop](references/review-loop.md)
- [Production Loop](references/production-loop.md)
- [Brief Contract](references/brief-contract.md)
- [Brief Format](references/brief-format.md)
- [SCRIPT.md Locked Narration](references/script-format.md)
- [Subagent Dispatch](references/subagent-dispatch.md)
- [Frame Worker Core Contract](references/frame-worker-core.md)
- [HyperFrames Tailwind](references/tailwind.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with HTML, JavaScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create HyperFrames project files, storyboard documents, render commands, and validation steps.]

## Skill Version(s):

1.0.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
