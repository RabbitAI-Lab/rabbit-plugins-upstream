## Description:

Provides HyperFrames motion rules, scene blueprints, transitions, runtime-specific animation guidance, and choreography-audit tooling for deterministic, seekable animations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to build seekable HyperFrames animations from motion recipes, scene blueprints, and runtime adapters, or to audit an existing composition's choreography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional animation-map audit helper may bootstrap dependencies outside a bundled HyperFrames installation.

Mitigation: Review dependency bootstrap prompts before running the helper and pin HYPERFRAMES_SKILL_PKG_VERSION when using it outside a bundled installation.

## Reference(s):

- [HyperFrames Animation release](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Motion rules index](artifact/rules-index.md)
- [Scene blueprints index](artifact/blueprints-index.md)
- [Transitions catalog](artifact/transitions/catalog.md)
- [GSAP documentation](https://gsap.com/docs/v3/)

## Skill Output:

**Output Type(s):** [Code, Guidance, Shell commands]

**Output Format:** [Markdown with code examples and optional audit commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Animation guidance emphasizes deterministic, seek-safe compositions.]

## Skill Version(s):

1.0.33 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
