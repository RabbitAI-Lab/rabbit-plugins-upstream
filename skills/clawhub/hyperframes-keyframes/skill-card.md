## Description:

Use when a HyperFrames composition needs seek-safe 2D/3D keyframes, GSAP timelines, CSS keyframes, Anime.js, WAAPI, FLIP, paths, masks, SVG morph/draw, text trails, 3D depth, or `hyperframes keyframes` diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video engineers use this skill to author and verify deterministic HyperFrames keyframes for 2D, 3D, SVG, text, mask, path, and timeline-based animation work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may edit composition keyframes in ways that produce inaccurate, misleading, or poorly seekable animation.

Mitigation: Review generated animation code and verify first frame, proof poses, final-minus-hold, and exact final with HyperFrames diagnostics before rendering.

Risk: `npx` diagnostics may invoke local project tooling.

Mitigation: Run commands only in trusted project workspaces and review CLI output before accepting final animation changes.

Risk: Animation behavior can become nondeterministic if runtime motion depends on timers, autoplay, random values, or asynchronous timeline construction.

Mitigation: Use finite, synchronously registered timelines or animations and avoid Date.now, performance.now, unseeded Math.random, timers, hover or scroll triggers, and infinite loops for render-critical motion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-keyframes)
- [Keyframe Mechanism Reference](references/keyframe-patterns.md)
- [GSAP keyframes](https://gsap.com/resources/keyframes/)
- [GSAP timeline](https://gsap.com/docs/v3/GSAP/Timeline/)
- [Anime.js documentation](https://animejs.com/documentation/)
- [MDN CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
- [Three.js AnimationMixer](https://threejs.org/docs/#api/en/animation/AnimationMixer)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces seek-safe animation implementation guidance and HyperFrames diagnostic commands for local verification.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
