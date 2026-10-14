## Description:

Helps developers design seek-safe HyperFrames animations using motion rules, scene blueprints, transitions, and runtime-specific examples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to plan and implement deterministic animations in HyperFrames compositions, or audit existing choreography with an animation map.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The animation audit script inspects local composition directories.

Mitigation: Run it only on composition directories you trust.

Risk: Running outside a bundled installation may require temporary package downloads, and some examples load public CDN libraries.

Mitigation: Pin the HyperFrames package version when bootstrapping dependencies and review external libraries before using the examples.

## Reference(s):

- [HyperFrames Animation on ClawHub](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [GSAP documentation](https://gsap.com/docs/v3/)
- [Motion blur reference](artifact/references/motion-blur.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands]

**Output Format:** [Markdown with animation examples and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance favors seek-safe, deterministic timelines; the optional audit produces an animation-map JSON file.]

## Skill Version(s):

1.0.38 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
