## Description:

The HyperFrames composition contract: build one renderable project using composition structure, data timing attributes, clips, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, validation, Tailwind projects, and STORYBOARD.md / SCRIPT.md plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to author, edit, and validate HyperFrames HTML video compositions with deterministic timing, media handling, sub-compositions, and production review workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included packet workflow can read unintended Markdown files when storyboard blueprint values are crafted maliciously.

Mitigation: Validate blueprint IDs against a strict allowlist, verify resolved paths remain inside the blueprint directory, and avoid untrusted STORYBOARD.md inputs until that boundary check exists.

Risk: Documented commands can run unpinned npm packages through bare npx hyperframes.

Mitigation: Run HyperFrames through a project-local, lockfile-pinned binary before using preview, check, or render commands.

Risk: The workflow can spawn workers, run previews or renders, and rely on related media-use preference memory.

Mitigation: Review the skill before installation and execute it in a controlled project workspace with expected worker, render, and media-use behavior.

## Reference(s):

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
- [GSAP CDN](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, CSS, JavaScript, JSON, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides one HyperFrames project at a time and expects validation before preview or render.]

## Skill Version(s):

1.0.25 (source: server evidence release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
