## Description:

Routes industrial and operational technology tasks to appropriate protocol-specific workflows for governed monitoring, troubleshooting, and analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Industrial operators and engineers use this skill to select appropriate workflows for monitoring PLCs, equipment, and industrial data, diagnosing faults, and analyzing downtime. It directs users to the relevant edition and requires authorization and approval for production-impacting writes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable workflows can change production control systems.

Mitigation: Restrict use to authorized operators and retain dry-run and named, double-confirmed approval gates before writes.

Risk: Misreading Chinese routing or safety instructions can lead to unsafe operation.

Mitigation: Install only where operators understand those instructions and are authorized to work with the connected OT systems.

Risk: Substation or utility SCADA workflows are outside this server's scope.

Mitigation: Use the separate energy package rather than routing those tasks through this server.

## Reference(s):

- [iaiops on ClawHub](https://clawhub.ai/zw008/skills/iaiops)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inline commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes to edition-specific workflows; does not itself define tools.]

## Skill Version(s):

0.32.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
