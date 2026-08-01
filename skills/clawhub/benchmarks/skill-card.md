## Description: <br>
Benchmark storage routing for agent memory/benchmark stacks: use when running BEAM-style evaluations, locomo benchmarks, calibration probes, or any benchmark that produces .db run databases. Tells you exactly what goes where - run databases OUTSIDE the repo, scripts and result JSONs in the repo. Now includes the run-resilience ladder: how long benchmark runs survive provider flaps. Load before creating any benchmark .db file or setting an output path. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[minopop](https://clawhub.ai/user/minopop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill when configuring benchmark evaluations, choosing database output locations, and hardening long LLM-driven benchmark runs against transient provider failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can influence where benchmark databases and retained checkpoints are written, which may create storage, cleanup, or data-retention issues if the scratch path is unsuitable. <br>
Mitigation: Review the configured scratch root and cleanup expectations before use; keep run databases outside the repository and use a .gitignore backstop for database files. <br>
Risk: Failed work units or partial checkpoint state can lead to benchmark results that look complete but are not publication-grade. <br>
Mitigation: Require failed work-unit counts in run reports, flag any run with failures, and verify checkpoint manifests against actual database state before resuming. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Directs agents to keep benchmark run databases outside the repository, keep scripts and result summaries in the repository, and use retry, circuit, checkpoint, and data-quality practices for resilient runs.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
