## Description: <br>
Collect operator-level performance data on Ascend NPU using msopprof, supporting device and simulator modes and generating performance analysis reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[changhui123456](https://clawhub.ai/user/changhui123456) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and performance engineers use this skill to profile Ascend NPU operators, choose device or simulator profiling modes, generate msprof/msopprof commands, interpret profiling outputs, and prepare performance reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Troubleshooting guidance may include commands that weaken host protections or broaden file permissions. <br>
Mitigation: Review every command before execution, avoid disabling SELinux or using chmod 777 unless the operational risk is explicitly accepted, and prefer least-privilege directory permissions. <br>
Risk: Profiling outputs and database exports may contain operational performance details or environment information. <br>
Mitigation: Run the skill in a controlled Ascend profiling environment, choose an approved output location, restrict access to generated artifacts, and confirm export destinations before persisting data. <br>
Risk: Incorrect device or simulator mode selection can produce misleading performance conclusions. <br>
Mitigation: Verify msprof/msopprof availability, CANN version, NPU or simulator readiness, target executable behavior, and mode-specific parameter support before relying on generated reports. <br>


## Reference(s): <br>
- [Acceptance Criteria](artifact/references/acceptance-criteria.md) <br>
- [Device Tuning Guide](artifact/references/device-tuning-guide.md) <br>
- [Simulator Tuning Guide](artifact/references/simulator-tuning-guide.md) <br>
- [Troubleshooting](artifact/references/troubleshooting.md) <br>
- [Verification Methods](artifact/references/verification-method.md) <br>
- [Simulator-Compatible Build Experience](artifact/demo/simulator-needs-sim-build.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Analysis] <br>
**Output Format:** [Markdown with inline shell command blocks and profiling report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Ascend profiling outputs such as CSV files, trace.json, visualize_data.bin, and profiling database exports.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
