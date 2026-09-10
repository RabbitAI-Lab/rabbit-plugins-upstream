## Description:

Agent Loop Engineering guides agents through authorized, bounded autonomous coding loops with persistent state, evidence-driven repair, staged review, safe workspace boundaries, and resumable handoffs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[englandtong](https://clawhub.ai/user/englandtong)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to execute already-authorized software work in bounded loops, repair failures with evidence, maintain compact project state, and hand off work for independent acceptance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables bounded autonomous project-local coding loops that can change code and record state.

Mitigation: Install it only in repositories where that behavior is acceptable, review the Active Packet before long runs, and keep hard stops for secrets, production data, paid resources, destructive Git, and out-of-workspace writes in place.

Risk: Repeated failed repair attempts can waste time or widen scope without producing evidence.

Mitigation: Stop after two consecutive attempts with the same failure signature unless there is new evidence, a narrower scope, a root cause, or passing behavior.

Risk: A claim may be overstated if weaker evidence is treated as proof of a stronger runtime or acceptance outcome.

Mitigation: Keep the weaker result when evidence conflicts, record unrun checks as not executed, and require independent final acceptance for Standard and Full governance work.

## Reference(s):

- [Quickstart](QUICKSTART.md)
- [Security](SECURITY.md)
- [Execution Loop 2.1](references/en/execution-loop.md)
- [Evidence And Completion 2.1](references/en/evidence-and-completion.md)
- [Safety And Context 2.1](references/en/safety-and-context.md)
- [Automation And Handoff 2.1](references/en/automation-and-handoff.md)
- [Isolated Delegation 2.1.1](references/en/isolated-delegation.md)
- [Legacy State Migration 2.1](references/en/migration.md)
- [Host Cost Controls 2.1.1](references/en/host-cost-controls.md)
- [Anti-Patterns 2.2](references/en/anti-patterns.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with optional shell commands, JSON state records, and project-local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are bounded by the active work packet, workspace write scope, stop conditions, and required evidence.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
