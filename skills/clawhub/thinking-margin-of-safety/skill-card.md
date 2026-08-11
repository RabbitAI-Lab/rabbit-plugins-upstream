## Description:

When provisioning, setting a limit, or committing an estimate under uncertainty, size a buffer to residual error and breach cost, not to the optimistic edge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and planning teams use this skill to size buffers for capacity, timelines, budgets, SLAs, and other commitments where uncertainty and asymmetric breach costs matter.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat the margin as a substitute for measurement or domain-specific review when commitments are financially or operationally important.

Mitigation: Use the skill as decision support, measure real requirements when practical, and seek domain review for high-stakes commitments.

Risk: Over-applying buffers can waste resources or hide a design that cannot safely absorb ruin-level failures.

Mitigation: Compare margin cost against expected breach cost, monitor whether the buffer is thin or excessive, and redesign when an affordable buffer cannot cover the worst plausible miss.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with a structured margin-of-safety estimate template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces decision-support guidance for estimating, challenging, committing, and monitoring a buffered number.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
