## Description:

Establishes CPU/GPU baselines before resource-intensive operations, including builds, training runs, or tasks that pin CPU cores or GPUs for over a minute.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to check CPU and GPU utilization, choose an appropriately narrow validation scope, instrument expensive work, and document resource costs before or after heavy builds, tests, or training runs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inspecting local CPU/GPU usage can expose process or workload details on shared machines.

Mitigation: Run utilization checks only where authorized, and avoid sharing process details beyond the people who need them.

Risk: Changing scheduler quotas, priority, batch sizes, or test scope can disrupt shared infrastructure or reduce validation coverage.

Mitigation: Use existing project and cluster policies for throttling, keep targeted runs proportional to the change, and document when wider validation is deferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conserve-cpu-gpu-performance)
- [OpenClaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conserve)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown checklist with inline shell commands and concise summary notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Expected summaries cover baseline metrics, selected scope, instrumentation, throttling tactics, and follow-up items.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter lists 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
