## Description: <br>
Provides HyperFrames animation rules, scene blueprints, transitions, techniques, runtime adapter guidance, and animation-map auditing support for deterministic, seek-safe motion work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and motion designers use this skill to author, adapt, and audit HyperFrames animation compositions across GSAP, Lottie, Three.js, Anime.js, CSS animations, WAAPI, and TypeGPU. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example files can fetch JavaScript from public CDNs when run. <br>
Mitigation: Review example dependencies before execution and use approved, pinned, or locally mirrored assets where the deployment environment requires that control. <br>
Risk: The animation-map tooling may bootstrap a HyperFrames package version when local packages are unavailable. <br>
Mitigation: Set HYPERFRAMES_SKILL_PKG_VERSION to an exact trusted version or run the tooling in a project with local HyperFrames packages installed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/heygen-com/skills/hyperframes-animation) <br>
- [GSAP Documentation](https://gsap.com/docs/v3/) <br>
- [Three.js WebGLRenderer Documentation](https://threejs.org/docs/pages/WebGLRenderer.html) <br>
- [Anime.js Documentation](https://animejs.com/documentation/) <br>
- [MDN Web Animations API Guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API) <br>
- [lottie-web](https://github.com/airbnb/lottie-web) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce deterministic animation recipes, runtime-specific implementation guidance, and local audit commands.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
