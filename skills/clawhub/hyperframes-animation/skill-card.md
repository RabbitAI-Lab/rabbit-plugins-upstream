## Description:

Helps developers compose seek-safe HyperFrames animations using motion rules, scene blueprints, transitions, runtime guidance, and an optional choreography audit.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to author deterministic HyperFrames compositions, choose animation patterns and browser runtimes, and optionally audit existing choreography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional animation-map audit may prompt to install npm dependencies when they are unavailable locally.

Mitigation: Review the proposed install and pin HYPERFRAMES_SKILL_PKG_VERSION when using the skill outside a bundled HyperFrames install.

Risk: The optional audit reads and renders the selected composition directory.

Mitigation: Run it only on composition directories intended for local HyperFrames capture and review.

## Reference(s):

- [Motion rules index](rules-index.md)
- [Scene blueprints index](blueprints-index.md)
- [Scene transitions overview](transitions/overview.md)
- [GSAP adapter](adapters/gsap.md)
- [GSAP documentation](https://gsap.com/docs/v3/)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, JSON]

**Output Format:** [Markdown with HTML, CSS, and JavaScript examples; optional JSON animation map]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Animation patterns target deterministic, seek-safe playback; the optional audit reports choreography flags.]

## Skill Version(s):

1.0.35 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
