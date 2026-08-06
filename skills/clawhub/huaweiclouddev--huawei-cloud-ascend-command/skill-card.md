## Description: <br>
Huawei Ascend NPU natural language management skill for local or SSH-based device queries, configuration, firmware upgrade, vNPU virtualization, certificate management, and compute power testing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and infrastructure operators use this skill to translate natural-language Ascend NPU administration requests into local or remote npu-smi and ascend-dmi workflows for monitoring, configuration, firmware, virtualization, certificate, and FLOPS tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact local or remote Ascend NPU administration actions. <br>
Mitigation: Install and run it only in controlled Ascend administration environments, and require explicit review before configuration, firmware, virtualization, certificate, or passthrough operations. <br>
Risk: SSH password and privileged account use can expose credentials or expand operational impact. <br>
Mitigation: Avoid command-line SSH passwords and root accounts where possible, and verify the target host before remote execution. <br>
Risk: Raw npu-smi passthrough can execute commands outside the natural-language guardrails. <br>
Mitigation: Use raw passthrough only after reviewing the exact command and its expected hardware impact. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-ascend-command) <br>
- [Ascend Official Documentation](https://www.hiascend.com/document) <br>
- [npu-smi Command Reference](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/260RC1/re/npu/npusmi_007.html) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Device Queries Reference](references/device-queries.md) <br>
- [Configuration Reference](references/configuration.md) <br>
- [Firmware Upgrade Reference](references/firmware-upgrade.md) <br>
- [Virtualization Reference](references/virtualization.md) <br>
- [Certificate Management Reference](references/certificate-management.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with JSON snippets and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include local or SSH command results, status summaries, error messages, and confirmation prompts for sensitive hardware operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
