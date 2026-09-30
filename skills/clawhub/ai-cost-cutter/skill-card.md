## Description:

Helps agents assess AI API costs and suggest savings through batching, caching, model routing, and local-model fallback, with a local cost estimator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theoretical text: all rights reserved

## Use Case:

Developers and teams estimating monthly AI inference costs can compare model-routing, batch-processing, and local-fallback scenarios and get guidance on reducing repeat API spending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing from a repository link without confirming its identity and release tag could fetch unintended content.

Mitigation: Verify the repository and tag before using the optional installation commands.

Risk: The bundled documentation and theory are not covered by the Python code's MIT license, and release metadata reports a different license identifier.

Mitigation: Review the bundled split license terms and confirm reuse rights before redistribution.

Risk: Estimated savings may differ from actual bills when pricing or workload assumptions change.

Mitigation: Supply current prices and representative usage data, and check decisions against actual billing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-cost-cutter)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands]

**Output Format:** [Markdown guidance and a plain-text cost comparison table from the local calculator]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cost estimates depend on user-supplied task volumes, token counts, and model prices.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata; bundled SKILL.md says 1.2.0 and manifest says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
