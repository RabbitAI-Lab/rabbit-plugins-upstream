## Description:

Collects operator-level performance data on Ascend NPUs with msopprof in device or simulator mode and helps generate performance analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to choose msprof op device or simulator workflows, generate profiling commands, interpret operator-level CSV and visualization outputs, and produce bottleneck analysis reports for Ascend NPU workloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Some troubleshooting examples weaken host security more than the profiling task requires.

Mitigation: Avoid following setenforce 0 and chmod 777 examples as written; use least-privilege permissions, user-owned output directories, and SELinux label or policy troubleshooting instead.

Risk: Generated profiling reports and CSV files may contain confidential model, operator, or performance information.

Mitigation: Store profiling outputs in private directories, restrict access before sharing, and treat exported reports as confidential engineering artifacts.

Risk: The skill can propose shell commands that run local profilers or target executables.

Mitigation: Review commands, executable paths, output locations, and environment variables before execution, especially on shared or production hosts.

## Reference(s):

- [Acceptance Criteria](references/acceptance-criteria.md)
- [Device Tuning Guide](references/device-tuning-guide.md)
- [Simulator Tuning Guide](references/simulator-tuning-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification Methods](references/verification-method.md)
- [Simulator-Compatible Build Experience](demo/simulator-needs-sim-build.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include profiling command examples, mode-selection rationale, CSV interpretation, and structured report sections.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
