## Description:

Write MIND source for deterministic agentic systems, with canonical MIC@3 artifacts, supported native ELF compilation, and feature-aware guidance for MIND v0.10.2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[star-ga](https://clawhub.ai/user/star-ga)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to draft, port, and explain MIND v0.10.2 source for deterministic agentic and numerical systems. It helps keep generated examples aligned with documented compiler capabilities, feature flags, MIC@3 output, and signing boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated MIND code can be incorrect for a user's exact compiler version, feature flags, or deployment target.

Mitigation: Compile and test generated code with the intended MIND compiler and enabled features before deployment.

Risk: The skill discusses experimental or feature-gated compiler paths, including native ELF, MLIR, autodiff, tensor, float, GPU, and signing workflows.

Mitigation: State the required compiler release and cargo features, and avoid presenting unsupported or feature-gated behavior as generally available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/star-ga/skills/mind)
- [Publisher profile](https://clawhub.ai/user/star-ga)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown with MIND code fences and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated MIND code should be compiled and tested with the intended compiler version before deployment.]

## Skill Version(s):

1.0.4 (source: frontmatter, metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
