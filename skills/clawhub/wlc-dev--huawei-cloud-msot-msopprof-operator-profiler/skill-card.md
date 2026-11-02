## Description:

Collects operator-level performance data on Ascend NPUs with msopprof in device or simulator mode and supports performance analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to collect and interpret operator-level performance data for Ascend NPU workloads, choose device or simulator profiling workflows, and prepare reports that help identify bottlenecks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting suggests disabling SELinux or making directories world-writable.

Mitigation: Keep SELinux enforcing and use a private output directory with least-privilege permissions.

Risk: A verification example recursively deletes the existing output_npu directory.

Mitigation: Choose a fresh, dedicated output path and confirm its contents before any cleanup.

Risk: Profiling executes the supplied operator program.

Mitigation: Run trusted operator code with ordinary user privileges.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-msot-msopprof-operator-profiler)
- [Device tuning guide](artifact/references/device-tuning-guide.md)
- [Simulator tuning guide](artifact/references/simulator-tuning-guide.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Verification methods](artifact/references/verification-method.md)
- [Acceptance criteria](artifact/references/acceptance-criteria.md)
- [Simulator-compatible build experience](artifact/demo/simulator-needs-sim-build.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and profiling report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides device and simulator workflows, output interpretation, and bottleneck investigation guidance.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
