## Description:

Recommends a model tier based on task complexity, with an illustrative cost comparison and fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); All rights reserved (documentation and theory)

## Use Case:

Developers and agent operators use this skill to select a cost-conscious model tier for a task and plan when to escalate or seek human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Heuristic routing advice may be unsuitable for regulated, high-risk, or expensive decisions.

Mitigation: Have a person review consequential model choices and conclusions.

Risk: The requested agent tool permissions are broader than the local routing script needs.

Mitigation: Run the script directly or use a constrained agent environment when tighter control is needed.

## Reference(s):

- [ClawHub model-router release](https://clawhub.ai/zhaoxinghua09-cell/skills/model-router)
- [LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Text, JSON]

**Output Format:** [Plain text or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommended tier, illustrative cost index and flagship comparison, and fallback guidance.]

## Skill Version(s):

1.0.3 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
