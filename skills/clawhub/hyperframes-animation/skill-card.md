## Description:

HyperFrames Animation provides motion-design recipes, scene blueprints, transitions, runtime adapter guidance, and an animation-map audit script for deterministic HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion authors use this skill to choose animation patterns and runtime-specific implementation guidance for HyperFrames scenes, then audit generated choreography for timing and lifecycle issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can fetch npm packages at use time and can fall back to @latest.

Mitigation: Review before installing, preinstall needed HyperFrames packages, or set HYPERFRAMES_SKILL_PKG_VERSION to a specific reviewed version.

Risk: HTML examples may load runtime libraries from CDNs.

Mitigation: Open examples only in browser contexts where the referenced CDNs are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Artifact skill definition](artifact/SKILL.md)
- [Animation rules index](artifact/rules-index.md)
- [Scene blueprints index](artifact/blueprints-index.md)
- [Scene transition catalog](artifact/transitions/catalog.md)
- [Motion design techniques](artifact/techniques.md)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Anime.js documentation](https://animejs.com/documentation/)
- [Three.js WebGLRenderer docs](https://threejs.org/docs/pages/WebGLRenderer.html)
- [Lottie web](https://github.com/airbnb/lottie-web)
- [MDN Web Animations API guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)
- [MDN CSS animation documentation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with code and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend running an animation-map script; example compositions may reference CDN-hosted runtime libraries.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
