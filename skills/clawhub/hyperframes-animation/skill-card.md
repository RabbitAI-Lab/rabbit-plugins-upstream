## Description:

HyperFrames Animation provides motion rules, scene blueprints, transitions, techniques, runtime adapters, and animation-map auditing guidance for deterministic HyperFrames compositions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to author and audit deterministic HyperFrames animations, including GSAP-based timelines, scene transitions, runtime-specific adapter patterns, and animation-map checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency bootstrap can download npm packages from unpinned paths, including an @latest fallback.

Mitigation: Preinstall reviewed HyperFrames packages or set HYPERFRAMES_SKILL_PKG_VERSION to an exact version before using bootstrap behavior.

Risk: Examples and adapter guidance can reference CDN-hosted runtime scripts.

Mitigation: Pin or vendor CDN scripts before production use.

Risk: The animate-text adapter recommends installing a separate third-party agent skill.

Mitigation: Review and scan the external animate-text skill before placing it under .agents/skills.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Anime.js v4 documentation](https://animejs.com/documentation/)
- [Three.js WebGLRenderer documentation](https://threejs.org/docs/pages/WebGLRenderer.html)
- [Lottie web project](https://github.com/airbnb/lottie-web)
- [MDN Web Animations API guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code snippets and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to produce HyperFrames composition code, runtime-specific animation snippets, and animation-map audit commands.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
