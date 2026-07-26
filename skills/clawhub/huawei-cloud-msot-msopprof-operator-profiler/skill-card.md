## Description: <br>
Collects operator-level performance data on Ascend NPU with msopprof in device or simulator mode and generates performance analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to profile Ascend NPU operators, choose device or simulator profiling mode, collect msopprof data, and turn performance metrics into optimization guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Suggested troubleshooting commands can weaken host security if used without review. <br>
Mitigation: Avoid disabling SELinux except as a last-resort diagnostic step, prefer least-privilege permissions over chmod 777, and review each command before running it. <br>
Risk: Profiling outputs may expose sensitive performance data or files on shared systems. <br>
Mitigation: Store profiling outputs in a private approved location and review cleanup commands before executing them. <br>


## Reference(s): <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Methods](references/verification-method.md) <br>
- [Device Tuning Guide](references/device-tuning-guide.md) <br>
- [Simulator Tuning Guide](references/simulator-tuning-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Simulator-Compatible Build Experience](demo/simulator-needs-sim-build.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with command examples and report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include host command suggestions that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
