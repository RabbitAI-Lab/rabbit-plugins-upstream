## Description:

When a constraint is treated as fixed, separate physics from convention, keep only independently supported primitives, and rebuild the simplest solution that satisfies real constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and other external users use this skill to challenge unsupported constraints, separate binding facts from convention, and rebuild a simpler solution from independently supported primitives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-principles framework may be over-applied when a proven standard solution already satisfies verified constraints.

Mitigation: Apply the skill's when-not-to-use and over-application guards before starting a rebuild.

Risk: An agent could discard a constraint that is actually binding, such as physics, regulation, contract, or measured capacity.

Mitigation: Require each primitive and residual constraint to cite a measurement, derivation, or primary requirement before treating assumptions as discardable.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown structured analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces claimed constraints, primitives, discarded assumptions, a rebuild, binding residuals, and a kill test.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
