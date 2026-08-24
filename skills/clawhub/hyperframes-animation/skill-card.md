## Description:

HyperFrames Animation gives agents motion-design rules, scene blueprints, transitions, runtime adapter guidance, and animation-map auditing patterns for deterministic HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to author, compose, and audit deterministic HyperFrames motion work across GSAP, Lottie, Three.js, Anime.js, CSS keyframes, Web Animations API, and TypeGPU.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples and snippets may fetch browser animation libraries from CDNs.

Mitigation: Use vendored or integrity-pinned dependencies for production, and avoid opening example HTML in sensitive browser contexts.

Risk: Optional dependency bootstrap may need to resolve HyperFrames helper packages when the skill runs outside a bundled install.

Mitigation: Set HYPERFRAMES_SKILL_PKG_VERSION when using the bootstrap path outside a bundled install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Skill overview](artifact/SKILL.md)
- [Motion rules index](artifact/rules-index.md)
- [Scene blueprints index](artifact/blueprints-index.md)
- [Transition overview](artifact/transitions/overview.md)
- [Animation techniques](artifact/techniques.md)
- [Animation map script](artifact/scripts/animation-map.mjs)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Anime.js v4 documentation](https://animejs.com/documentation/)
- [Lottie web](https://github.com/airbnb/lottie-web)
- [Three.js WebGLRenderer documentation](https://threejs.org/docs/pages/WebGLRenderer.html)
- [MDN Web Animations API guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HTML, CSS, JavaScript, animation timing recipes, runtime-specific configuration, and JSON animation-map artifacts.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
