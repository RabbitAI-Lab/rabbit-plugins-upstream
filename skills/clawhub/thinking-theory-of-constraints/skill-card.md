## Description:

When throughput or latency is pipeline-limited, this skill helps identify the single binding constraint and apply exploit, subordinate, elevate, then recheck steps while ignoring non-constraints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tjboudreaux](https://clawhub.ai/user/tjboudreaux)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and process owners use this skill to analyze throughput- or latency-limited workflows, identify the single binding constraint with evidence, and produce an ordered improvement plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can influence the agent to recommend incorrect bottleneck-focused changes if the binding constraint is misidentified.

Mitigation: Require measured utilization, queue, wait, or throughput evidence, and falsify the chosen constraint by checking whether improving it would raise end-to-end throughput.

Risk: The method can be over-applied to problems without one stable binding stage, such as correctness faults or coupled contention.

Mitigation: Use the skill's explicit exit criteria: if no single stage dominates, route the analysis to systems, debugging, or concurrency design instead.

Risk: Optimizing non-constraints can increase work in progress without improving end-to-end output.

Mitigation: Subordinate upstream and downstream work to the constraint rate, and avoid local utilization goals that grow queues before the constraint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tjboudreaux/skills/thinking-theory-of-constraints)
- [ClawHub publisher profile](https://clawhub.ai/user/tjboudreaux)

## Skill Output:

**Output Type(s):** [guidance, text, markdown]

**Output Format:** [Markdown or plain text structured as a bottleneck analysis template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces fields for system goal, flow, constraint, evidence, exploit actions, subordination changes, elevation decision, and next constraint watch.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
