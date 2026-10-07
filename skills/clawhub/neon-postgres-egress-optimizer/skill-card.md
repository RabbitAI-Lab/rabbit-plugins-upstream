## Description:

Guides developers through diagnosing and reducing excessive PostgreSQL data transfer caused by inefficient application queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[andrelandgraf](https://clawhub.ai/user/andrelandgraf)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to identify costly PostgreSQL query patterns, reduce database egress through targeted code changes, and verify the results. It also describes optional Neon configuration for controlling non-production compute costs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Resetting query statistics or creating an extension on the wrong database can affect production diagnostics or settings.

Mitigation: Confirm the target database or Neon branch and review the proposed SQL before execution.

Risk: Applying optional Neon configuration can change compute behavior or expire future ephemeral branches through the TTL setting.

Mitigation: Review configuration and branch scope before installing @neon/config or running neon config apply; confirm TTL is appropriate.

Risk: Column selection and pagination changes can alter API responses expected by clients.

Mitigation: Run existing tests, check response shapes, and compare database transfer metrics after changes.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/andrelandgraf/skills/neon-postgres-egress-optimizer)
- [Neon parent skill](https://neon.com/docs/ai/skills/neon/SKILL.md)
- [Neon network transfer documentation](https://neon.com/docs/introduction/network-transfer.md)
- [Neon cost optimization documentation](https://neon.com/docs/introduction/cost-optimization.md)

## Skill Output:

**Output Type(s):** [Text, Code, Shell commands, Configuration guidance]

**Output Format:** [Markdown with SQL, code, and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations and proposed changes should be verified against application behavior and database metrics.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
