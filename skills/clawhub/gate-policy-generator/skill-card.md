## Description:

Generates and checks agent tool-permission policies with allow, review, and deny boundaries, four approval gates, and usage budgets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (code only); all rights reserved (documentation and theory); release metadata lists MIT-0

## Use Case:

Developers and agent operators use this skill to draft and check tool-permission policies from an agent capability list before deploying agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated policies may not match an agent's actual permissions or approval process.

Mitigation: Review the generated policy and validate it against real tool permissions before relying on it.

Risk: The release's license metadata and included license terms differ, and the code license does not cover documentation or theory.

Mitigation: Confirm the applicable terms for each component before reuse or redistribution.

## Reference(s):

- [Gate Policy Generator on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/gate-policy-generator)
- [LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Configuration, Text]

**Output Format:** [JSON policy and human-readable validation findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Policies specify tool allow/review/deny lists, four gates, and iteration and token budgets.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
