## Description:

Guides agents in building deterministic HyperFrames animations with motion rules, scene blueprints, transitions, runtime adapters, and choreography audits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to design and implement seek-safe HyperFrames motion, choose animation runtimes, and audit existing scene choreography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the animation-map helper can launch browser capture tooling and install temporary npm dependencies.

Mitigation: Review the helper before execution and pin the HyperFrames package version when reproducible dependency resolution is needed.

Risk: Separately installed companion skills may have different security properties.

Mitigation: Review companion skills such as animate-text independently before installing them.

## Reference(s):

- [Motion blur reference](references/motion-blur.md)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Anime.js documentation](https://animejs.com/documentation/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, JSON audit reports]

**Output Format:** [Markdown guidance and code examples; optional JSON animation map]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Animation recipes target deterministic, seek-safe playback.]

## Skill Version(s):

1.0.39 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
