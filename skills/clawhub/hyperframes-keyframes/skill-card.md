## Description:

Author seek-safe 2D/3D keyframes for HyperFrames compositions, including zooms, reframes, camera moves, visual handoffs, masks, SVG motion, text trails, and runtime diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and video automation engineers use this skill to author and verify seek-safe HyperFrames animation keyframes while preserving clip timing boundaries, subject identity, and final visual states.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated animation edits may introduce incorrect motion, unreadable text, or wrong final visual states.

Mitigation: Review generated keyframes and verify them with the HyperFrames diagnostics recommended by the skill before rendering.

Risk: The skill may propose local HyperFrames verification commands.

Mitigation: Run proposed commands only in trusted project workspaces and review command intent before execution.

## Reference(s):

- [Keyframe Mechanism Reference](references/keyframe-patterns.md)
- [GSAP Keyframes](https://gsap.com/resources/keyframes/)
- [GSAP Timeline](https://gsap.com/docs/v3/GSAP/Timeline/)
- [Anime.js Documentation](https://animejs.com/documentation/)
- [MDN CSS Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations)
- [Three.js AnimationMixer](https://threejs.org/docs/#api/en/animation/AnimationMixer)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HyperFrames verification command suggestions and runtime keyframe snippets.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
