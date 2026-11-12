## Description:

Uses msopprof to profile operator performance on Ascend NPUs in device or simulator mode and guide data collection, reporting, and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to collect and interpret operator-level performance data for Ascend NPU workloads. It helps select device or simulator profiling, prepare commands, identify bottlenecks, and summarize optimization options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting instructions include SELinux-disabling and world-writable-directory workarounds; a verification example deletes the prior output directory. Profiling runs an operator, and a referenced analysis script is not included.

Mitigation: Remove the security and permission workarounds, use a private output directory and a fresh directory per run, run only a trusted operator with ordinary user permissions, and separately review any supplied analysis script.

## Reference(s):

- [Device Tuning Guide](references/device-tuning-guide.md)
- [Simulator Tuning Guide](references/simulator-tuning-guide.md)
- [Troubleshooting](references/troubleshooting.md)
- [Verification Methods](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with profiling commands and performance summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include metrics, bottleneck findings, and optimization suggestions based on supplied profiling data.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
