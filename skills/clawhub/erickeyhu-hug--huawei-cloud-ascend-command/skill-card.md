## Description: <br>
Huawei Ascend NPU natural language management skill for local and SSH remote execution of npu-smi workflows, including device queries, configuration management, firmware upgrade, vNPU virtualization, certificate management, and FLOPS testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to translate natural-language Ascend NPU administration requests into local or remote npu-smi operations for monitoring, configuration, firmware, virtualization, certificate, and compute-power workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad local and remote command authority for Ascend NPU administration. <br>
Mitigation: Install and run it only in controlled admin environments, and restrict direct npu-smi, execute_batch, and remote SSH execution before production use. <br>
Risk: SSH password and root-account workflows can expose credentials or overprivileged access. <br>
Mitigation: Prefer key-based or secret-store SSH authentication, avoid root accounts where possible, and do not pass reusable passwords through broad prompts. <br>
Risk: Firmware, ECC, fan, vNPU, and certificate operations can change hardware or service state. <br>
Mitigation: Require explicit operator confirmation, review the generated command before execution, and test high-impact changes on a limited target before broad rollout. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-ascend-command) <br>
- [Huawei Ascend documentation](https://www.hiascend.com/document) <br>
- [npu-smi command reference](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/260RC1/re/npu/npusmi_007.html) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Certificate Management Reference](references/certificate-management.md) <br>
- [Configuration Management Reference](references/configuration.md) <br>
- [Device Queries Reference](references/device-queries.md) <br>
- [Firmware Upgrade Reference](references/firmware-upgrade.md) <br>
- [Troubleshooting and Practical Experience](references/troubleshooting.md) <br>
- [Verification Steps and Methods](references/verification-method.md) <br>
- [Virtualization Reference](references/virtualization.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Plain text with JSON-style command summaries and error messages] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include npu-smi or ascend-dmi command output from local or SSH remote Ascend NPU systems.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
