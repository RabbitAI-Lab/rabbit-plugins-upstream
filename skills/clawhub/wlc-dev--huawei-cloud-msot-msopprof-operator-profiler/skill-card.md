## Description:

Guides operator-level performance profiling on Ascend NPUs in device or simulator mode and helps interpret profiling results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and performance engineers use this skill to collect and analyze Ascend NPU operator profiling data, compare device and simulator results, and identify bottlenecks for optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting guidance may disable SELinux and weaken host security.

Mitigation: Do not run setenforce 0 on a normal host; review security implications before using troubleshooting commands.

Risk: World-writable profiling directories may expose collected data.

Mitigation: Replace chmod 777 /tmp/profiling with a private, user-owned output directory and control access to profiling reports and database exports.

Risk: Profiling reports and database exports may persist beyond their intended use.

Mitigation: Decide where profiling outputs will be stored and clean them up when no longer needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-msot-msopprof-operator-profiler)
- [Device Tuning Guide](artifact/references/device-tuning-guide.md)
- [Simulator Tuning Guide](artifact/references/simulator-tuning-guide.md)
- [Troubleshooting](artifact/references/troubleshooting.md)
- [Verification Methods](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Shell commands, Analysis, Markdown reports, Guidance]

**Output Format:** [Markdown with shell commands and profiling report summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Device and simulator workflows; four-section report with bottleneck and optimization summaries.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
