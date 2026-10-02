## Description:

Guides agents in creating and auditing deterministic HyperFrames animations using motion rules, scene blueprints, transitions, and runtime adapters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative teams use this skill to design seek-safe motion for HyperFrames compositions, choose animation techniques and runtimes, and audit choreography.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Examples may load animation libraries from external CDNs.

Mitigation: Review external dependencies and use approved or locally hosted versions before deploying.

Risk: Optional text effects may install another skill, and animation auditing may install missing packages and run local browser capture.

Mitigation: Run these optional workflows only in projects where dependency installation and local browser capture are permitted.

## Reference(s):

- [HyperFrames animation techniques](techniques.md)
- [HyperFrames scene blueprints](blueprints-index.md)
- [HyperFrames transition catalog](transitions/catalog.md)
- [GSAP documentation](https://gsap.com/docs/v3/)

## Skill Output:

**Output Type(s):** [Code, Configuration instructions, Guidance]

**Output Format:** [Markdown with code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Animation guidance is designed for deterministic, seek-safe HyperFrames timelines.]

## Skill Version(s):

1.0.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
