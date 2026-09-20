## Description:

All animation knowledge for HyperFrames: atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, and runtime adapters for GSAP, Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, and TypeGPU.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative engineers use this skill to design deterministic HyperFrames motion, choose animation rules or scene blueprints, and look up runtime-specific implementation patterns. It also provides a local animation-map helper for auditing choreography after authoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional animation-map script may invoke npm to fetch HyperFrames helper packages if they are not already available.

Mitigation: Run the script only when the package source is trusted, review the install prompt, and prefer pinning HYPERFRAMES_SKILL_PKG_VERSION outside bundled installs.

Risk: The animation-map helper writes analysis output for a local composition and may expose project structure or choreography details if shared carelessly.

Mitigation: Choose the output directory deliberately and review generated files before publishing or sharing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [HyperFrames animation overview](artifact/SKILL.md)
- [Motion blur reference](artifact/references/motion-blur.md)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Anime.js documentation](https://animejs.com/documentation/)
- [Three.js AnimationMixer documentation](https://threejs.org/docs/pages/AnimationMixer.html)
- [lottie-web](https://github.com/airbnb/lottie-web)
- [MDN Web Animations API guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code snippets, HTML examples, shell commands, and optional JSON reports from the animation-map helper]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Designed for seek-safe, deterministic HyperFrames animation authoring and review.]

## Skill Version(s):

1.0.23 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
