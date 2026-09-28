## Description:

Helps plan lower-cost AI workloads through batching, model routing, caching, and local-model fallback, with a local calculator for comparing estimated monthly costs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory all rights reserved

## Use Case:

Developers and teams evaluating AI API spending can compare monthly cost estimates and plan batching, caching, model routing, and local-model fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may surface the skill for unrelated requests.

Mitigation: Use it only when the user's request calls for AI cost planning.

Risk: Installation commands point to an external repository whose contents should be checked before use.

Mitigation: Verify the publisher, source, and referenced tag before running installation commands.

Risk: Code and documentation have different stated reuse terms, and the listing's license label differs from the included license text.

Mitigation: Review the included license and confirm permissions for each file before reuse or redistribution.

Risk: Estimated savings can mislead budgeting if input prices or workload assumptions are inaccurate.

Mitigation: Check current rates and actual usage before relying on the estimates for spending decisions.

## Reference(s):

- [Publisher's LGD Hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)
- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-cost-cutter)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown guidance and plain-text cost comparison table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimated monthly USD costs and savings for a baseline and three cost-reduction options, based on user-supplied workload and prices.]

## Skill Version(s):

1.0.2 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
