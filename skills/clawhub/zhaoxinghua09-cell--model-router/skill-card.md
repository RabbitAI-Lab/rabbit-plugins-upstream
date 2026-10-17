## Description:

Recommends a model tier based on task complexity, with a cost comparison and fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (listing); MIT for Python code, documentation rights reserved

## Use Case:

Developers and agent operators use this skill to select a cost-conscious model tier for a task and plan when to escalate or seek review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests edit access even though its local router only needs to read input and print recommendations.

Mitigation: Review before installation and limit edit access unless explicitly needed.

Risk: The instructions describe executing model calls, beyond the supplied router's advisory behavior.

Mitigation: Treat recommendations as advisory; require explicit approval before changing routing or making downstream model calls.

## Reference(s):

- [Model Router release on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/model-router)
- [LGD theory (background)](https://github.com/zhaoxinghua09-cell/lgd-theory)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a recommended tier, relative cost estimate, and fallback advice; the supplied CLI does not call a model.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
