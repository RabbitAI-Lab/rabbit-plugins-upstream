## Description:

Guides Ascend NPU operator profiling in device or simulator mode and helps interpret performance data to identify bottlenecks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to collect Ascend NPU operator metrics, compare device and simulator profiling, and prepare bottleneck analysis and optimization guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting suggests disabling SELinux, weakening host protections.

Mitigation: Do not disable SELinux; ask an administrator to diagnose denials and apply narrow policy changes.

Risk: Troubleshooting suggests making /tmp/profiling world-writable with chmod 777.

Mitigation: Use a user-owned profiling directory with restrictive permissions, and review commands before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-msot-msopprof-operator-profiler)
- [Device Tuning Guide](artifact/references/device-tuning-guide.md)
- [Simulator Tuning Guide](artifact/references/simulator-tuning-guide.md)
- [Acceptance Criteria](artifact/references/acceptance-criteria.md)
- [Verification Methods](artifact/references/verification-method.md)
- [Troubleshooting](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown with shell commands, performance analysis, and report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Profiling commands depend on device or simulator mode and the target operator executable.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
