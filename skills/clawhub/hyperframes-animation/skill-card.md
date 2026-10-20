## Description:

Provides HyperFrames animation recipes, scene blueprints, transition guidance, runtime adapters, and a tool for auditing composition choreography.

This skill is ready for commercial/non-commercial use.

## Publisher:

[heygen-com](https://clawhub.ai/user/heygen-com)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and motion designers use this skill to compose deterministic HyperFrames animations, select runtime-specific patterns, and audit the timing of existing compositions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional animation-map audit runs local composition code in a browser-like capture session and may download missing HyperFrames packages.

Mitigation: Review the composition and dependencies before running the audit; allow package fetching only when intended.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/heygen-com/skills/hyperframes-animation)
- [Animation rules index](artifact/rules-index.md)
- [Scene blueprints index](artifact/blueprints-index.md)
- [Transitions overview](artifact/transitions/overview.md)
- [HyperFrames GSAP adapter](artifact/adapters/gsap.md)

## Skill Output:

**Output Type(s):** [Code, Markdown, JSON, Guidance]

**Output Format:** [Animation recipes and code examples; JSON choreography audit when the helper is run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Animation-map audits can produce animation-map.json.]

## Skill Version(s):

1.0.40 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
