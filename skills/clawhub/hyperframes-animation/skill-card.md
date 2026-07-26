## Description: <br>
Provides HyperFrames animation authoring guidance, including atomic motion rules, multi-phase blueprints, scene transitions, runtime adapters, and choreography audit support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[heygen-com](https://clawhub.ai/user/heygen-com) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and designers use this skill to select and compose deterministic HyperFrames motion patterns, scene blueprints, transitions, and runtime-specific animation code for web and video compositions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example HTML loads JavaScript from public CDNs. <br>
Mitigation: Review CDN sources and use pinned or locally hosted dependencies when running examples in controlled environments. <br>
Risk: The animation-map helper can bootstrap HyperFrames packages when they are not bundled in the local environment. <br>
Mitigation: Set HYPERFRAMES_SKILL_PKG_VERSION to an exact version before running the helper when deterministic dependency resolution is required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation) <br>
- [Skill overview](artifact/SKILL.md) <br>
- [Rules index](artifact/rules-index.md) <br>
- [Blueprints index](artifact/blueprints-index.md) <br>
- [Transitions overview](artifact/transitions/overview.md) <br>
- [Motion techniques](artifact/techniques.md) <br>
- [GSAP documentation](https://gsap.com/docs/v3/) <br>
- [Anime.js documentation](https://animejs.com/documentation/) <br>
- [Lottie-web project](https://github.com/airbnb/lottie-web) <br>
- [MDN CSS animation reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce deterministic HyperFrames animation recipes, runtime adapter guidance, and animation-map audit commands.] <br>

## Skill Version(s): <br>
1.0.12 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
