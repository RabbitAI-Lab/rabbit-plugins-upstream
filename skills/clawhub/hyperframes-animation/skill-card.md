## Description:

HyperFrames Animation provides motion rules, scene blueprints, transitions, techniques, runtime adapters, and animation-map auditing guidance for deterministic HyperFrames composition work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to build, adapt, and audit deterministic HyperFrames animations by selecting atomic rules, blueprints, transitions, and runtime-specific adapter patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser examples may load third-party CDN scripts.

Mitigation: Vendor dependencies or use SRI-pinned CDN URLs before opening, reusing, or publishing generated examples.

Risk: Glitch, jitter, flash-heavy, or intense motion effects can create accessibility concerns.

Mitigation: Provide reduced-motion or reduced-flash alternatives and review generated animations against accessibility requirements.

Risk: Generated animation code or shell commands can alter project files or introduce unsuitable runtime dependencies.

Mitigation: Review generated code and commands in an isolated project, then scan and test before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [HyperFrames Animation skill overview](artifact/SKILL.md)
- [Rules Index](artifact/rules-index.md)
- [Blueprints Index](artifact/blueprints-index.md)
- [Visual Techniques Reference](artifact/techniques.md)
- [Transitions Catalog](artifact/transitions/catalog.md)
- [GSAP Documentation](https://gsap.com/docs/v3/)
- [Anime.js Documentation](https://animejs.com/documentation/)
- [Lottie Web](https://github.com/airbnb/lottie-web)
- [MDN CSS Animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code blocks, file references, and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create runnable browser examples and to run animation-map analysis that emits JSON artifacts.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
