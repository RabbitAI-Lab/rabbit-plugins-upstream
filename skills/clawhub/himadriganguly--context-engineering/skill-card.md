## Description:

Diagnose and improve context usage in AI agent sessions when context grows large, instructions are missed, or token usage rises.

This skill is ready for commercial/non-commercial use.

## Publisher:

[himadriganguly](https://clawhub.ai/user/himadriganguly)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to audit context pressure, identify likely causes of degraded responses, reorganize context, and verify improvements.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing session directories may read sensitive context and create reports containing private information.

Mitigation: Choose session directories deliberately, exclude secrets and private logs unless necessary, and review report destinations before running scripts.

Risk: Heuristic audit metrics or generic context-profile rules may mislead decisions in sensitive projects.

Mitigation: Treat results as decision support, verify changes against task behavior, and tighten profile rules for sensitive projects.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/himadriganguly/skills/context-engineering)
- [Degradation signals](artifact/references/degradation-signals.md)
- [Progressive disclosure patterns](artifact/references/progressive-disclosure-patterns.md)
- [Token budget framework](artifact/references/token-budget-framework.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown guidance; optional JSON audit reports and YAML context profiles]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Token counts and audit metrics are estimates, not direct measurements of model attention or quality.]

## Skill Version(s):

1.1.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
