## Description: <br>
Govern multi-agent Codex work by converting parallel or speed-first requests into bounded lanes, context capsules, deterministic gates, freshness checks, and concise usage reporting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinadu-ai](https://clawhub.ai/user/tinadu-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to plan and govern bounded multi-agent Codex work, including delegation limits, context-capsule creation, QA freshness checks, and run metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can activate on broad requests about saving time, parallelism, or using many agents. <br>
Mitigation: Confirm the task has independent reasoning lanes before spawning agents, and keep work local or use one sidecar when fewer than two lanes exist. <br>
Risk: Helper scripts create temporary run records under /tmp. <br>
Mitigation: Review the generated manifest path, keep user deliverables outside the run directory, and remove temporary run records when they are no longer needed. <br>
Risk: The optional usage collection script can read local Codex telemetry for registered threads. <br>
Mitigation: Run usage collection only when metrics are needed, restrict it to registered thread ids, and leave thread titles omitted unless explicitly required. <br>


## Reference(s): <br>
- [Agent Contracts](references/agent-contracts.md) <br>
- [Orchestration Policy](references/orchestration-policy.md) <br>
- [Quality Gates](references/quality-gates.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON run-manifest/context-capsule files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [When helper scripts are used, temporary run manifests and capsules are written under /tmp/multi-agent-runs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
