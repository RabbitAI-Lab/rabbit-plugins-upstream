## Description:

Collects operator-level performance data on Ascend NPUs with msopprof in device or simulator mode and generates performance analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to profile Ascend NPU operators, choose device or simulator collection modes, interpret profiling outputs, and produce optimization reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting guidance includes commands that can weaken host security, including disabling SELinux and broadening directory permissions.

Mitigation: Review commands before use, avoid copying setenforce 0 or chmod 777 as written, and prefer least-privilege fixes scoped to the profiling executable and output directory.

Risk: Profiling outputs may contain sensitive model, operator, environment, or performance data.

Mitigation: Use private user-owned output directories, restrict access to generated artifacts, and handle profiling data as sensitive project data.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-msot-msopprof-operator-profiler)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Device Tuning Guide](references/device-tuning-guide.md)
- [Simulator Tuning Guide](references/simulator-tuning-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification Methods](references/verification-method.md)
- [Some Projects Require Simulator-Compatible Build](demo/simulator-needs-sim-build.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and profiling report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference msprof or msopprof commands, profiling output paths, CSV files, and visualization artifacts.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
