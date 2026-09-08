## Description:

The HyperFrames composition contract builds one renderable project covering composition structure, data-* timing attributes, clip classes, tracks, sub-compositions, variables, framework-owned media playback, deterministic-render rules, validation, Tailwind projects, and STORYBOARD.md / SCRIPT.md plan formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video-building agents use this skill to create or edit a renderable HyperFrames HTML video project. It guides composition structure, timing, media placement, storyboard and script planning, Tailwind setup, validation, and frame-packet generation for worker agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A helper can include Markdown files outside its intended folder.

Mitigation: Run the packet builder only on trusted STORYBOARD.md files until blueprint identifiers are constrained to known files under the blueprint directory.

Risk: The docs encourage mutable npx CLI execution.

Mitigation: Use a pinned, locally installed HyperFrames CLI with a lockfile and review commands before execution.

Risk: The security verdict is suspicious for sensitive workspaces.

Mitigation: Review and scan the skill before installing or using it in sensitive workspaces.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-core)
- [Minimal Composition](artifact/references/minimal-composition.md)
- [Composition Patterns](artifact/references/composition-patterns.md)
- [Data Attributes Reference](artifact/references/data-attributes.md)
- [Tracks and Clips](artifact/references/tracks-and-clips.md)
- [Variables and Media](artifact/references/variables-and-media.md)
- [Determinism, Animation Runtime, and Layout](artifact/references/determinism-rules.md)
- [Sub-Compositions](artifact/references/sub-compositions.md)
- [Storyboard format](artifact/references/storyboard-format.md)
- [Script format](artifact/references/script-format.md)
- [Frame worker core contract](artifact/references/frame-worker-core.md)
- [HyperFrames Tailwind](artifact/references/tailwind.md)
- [GSAP CDN reference](https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with HTML, JavaScript, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate project files and bounded frame-packet Markdown when helper scripts are used.]

## Skill Version(s):

1.0.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
