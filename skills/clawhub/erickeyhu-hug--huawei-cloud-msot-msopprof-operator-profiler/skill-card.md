## Description: <br>
Collects operator-level performance data on Ascend NPU with msopprof in device or simulator mode and helps generate performance analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to choose device or simulator profiling mode, generate msprof op commands, interpret profiler artifacts, and create reports for Ascend NPU operator bottleneck analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Troubleshooting guidance includes privileged host changes and broad permissions such as disabling SELinux or using permissive output directories. <br>
Mitigation: Review generated commands before execution, avoid disabling SELinux except in isolated test environments with a rollback plan, and use dedicated user-owned output directories with restrictive permissions. <br>
Risk: Profiling reports, dumps, traces, and database exports can expose sensitive operational or model performance data. <br>
Mitigation: Treat profiler artifacts as sensitive data, restrict access to generated outputs, and avoid sharing traces or exports outside the intended analysis workflow. <br>
Risk: Incorrect mode or parameter selection can lead to invalid profiling runs or misleading bottleneck analysis. <br>
Mitigation: Confirm device versus simulator mode, validate generated msprof parameters against local msprof help and project build requirements, and review reports against the documented acceptance criteria. <br>


## Reference(s): <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Device Tuning Guide](references/device-tuning-guide.md) <br>
- [Simulator Tuning Guide](references/simulator-tuning-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Some Projects Require Simulator-Compatible Build](demo/simulator-needs-sim-build.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and structured report guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference msprof output files such as CSV reports, trace.json, visualize_data.bin, dumps, and profiling database exports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
