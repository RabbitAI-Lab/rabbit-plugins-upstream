## Description:

Loop Engineering is a guide for designing autonomous agent loop systems with goals, feedback, self-verification, reusable patterns, configuration examples, and anti-patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openlark](https://clawhub.ai/user/openlark)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to learn and apply Loop Engineering patterns for autonomous agent systems, including scheduled loops, goal-driven workflows, sub-agent orchestration, feedback mechanisms, and termination controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long-running loops can consume excessive tokens or compute when termination conditions are vague or absent.

Mitigation: Set explicit max rounds, objective completion checks, timeouts, and early-exit rules for no-progress rounds before adopting loop examples.

Risk: Scheduling, auto-fix, deployment, dependency, or broad write-access examples could be adapted into workflows with unintended side effects.

Mitigation: Require explicit approvals for deployment, dependency changes, broad write access, and long-running automated loops.

Risk: Automated remediation or scheduled tasks can overlap, cascade, or repeat ineffective actions if feedback signals are ignored.

Mitigation: Use preconditions, backoff, verification checks, monitoring logs, and escalation paths when implementing the documented patterns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/openlark/skills/loop-engineering)
- [Common Loop Patterns](references/patterns.md)
- [Configuration Examples](references/config-examples.md)
- [Anti-Patterns and Corrections](references/anti-patterns.md)
- [Platform Integration Guide](references/integration.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration, shell commands, code]

**Output Format:** [Markdown guidance with pseudo-code, YAML, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only skill; it provides design guidance and examples rather than executing runtime actions.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
