## Description:

Use when a HyperFrames composition needs seek-safe 2D/3D keyframes for punch-ins, zooms, reframes, Ken Burns treatments, camera moves, visual handoffs, GSAP, CSS keyframes, Anime.js, WAAPI, FLIP, paths, masks, SVG morph/draw, text trails, 3D depth, or keyframe diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to author deterministic, seek-safe visual keyframes for HyperFrames compositions and verify the resulting motion with HyperFrames CLI diagnostics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CLI examples use unpinned npx commands, which can create supply-chain risk in production or sensitive workspaces.

Mitigation: Prefer a project-local or exact-version HyperFrames installation before running the CLI examples.

Risk: Keyframe guidance can produce unseekable or non-deterministic render-critical motion if timers, autoplay, random values, or asynchronous timeline creation are used.

Mitigation: Build animation instances synchronously, keep loops finite, register seekable runtimes, and verify motion with HyperFrames lint, check, keyframes, shot, and snapshot diagnostics.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-keyframes)
- [Keyframe Mechanism Reference](references/keyframe-patterns.md)
- [GSAP keyframes](https://gsap.com/resources/keyframes/)
- [GSAP Timeline](https://gsap.com/docs/v3/GSAP/Timeline/)
- [Anime.js documentation](https://animejs.com/documentation/)
- [MDN CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
- [Three.js AnimationMixer](https://threejs.org/docs/#api/en/animation/AnimationMixer)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be adapted to the actual HyperFrames composition geometry, runtime, and verification targets.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
