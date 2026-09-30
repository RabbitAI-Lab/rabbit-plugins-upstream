## Description:

Provides motion-design rules, scene blueprints, transitions, runtime guidance, and composition-audit tooling for HyperFrames animations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to build seek-safe HyperFrames animations, select appropriate motion patterns and runtimes, and audit existing composition choreography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional animation-map helper can inspect a local composition and write an output JSON file.

Mitigation: Review the target composition and output location before running the helper.

Risk: The optional helper can launch the HyperFrames capture stack and install missing packages into a temporary directory when authorized.

Mitigation: Run it only in a trusted environment and review package installation before opting in.

## Reference(s):

- [HyperFrames Animation on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Motion blur reference](references/motion-blur.md)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Web Animations API guide](https://developer.mozilla.org/docs/Web/API/Web_Animations_API/Using_the_Web_Animations_API)

## Skill Output:

**Output Type(s):** [Guidance, Code, Configuration instructions]

**Output Format:** [Markdown with HTML, CSS, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Seek-safe animation recipes and optional composition-audit guidance.]

## Skill Version(s):

1.0.26 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
