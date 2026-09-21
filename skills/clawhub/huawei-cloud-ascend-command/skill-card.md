## Description:

Huawei Ascend NPU natural language management skill for local or SSH-based npu-smi workflows covering device queries, monitoring, configuration, firmware, vNPU virtualization, certificates, and FLOPS testing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure engineers use this skill to inspect and administer Huawei Ascend NPU devices through natural language requests that map to npu-smi and ascend-dmi operations. It supports local host management and remote SSH workflows for health checks, utilization monitoring, configuration changes, firmware operations, vNPU management, certificate tasks, and compute power tests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses high-impact Ascend NPU administration access over local execution or SSH.

Mitigation: Install only where NPU administration is intended, review generated operations before execution, and confirm mutating firmware, vNPU, certificate, ECC, or fan changes only after validating target device scope.

Risk: Server security evidence reports unsafe credential, host-verification, and permission guidance.

Mitigation: Prefer key-based SSH, strict known-host verification, non-root accounts with narrowly scoped sudo, and group or udev-based device permissions instead of broad device permissions.

## Reference(s):

- [Huawei Ascend Documentation](https://www.hiascend.com/document)
- [Huawei Ascend npu-smi Reference](https://www.hiascend.com/document/detail/zh/Atlas%20200I%20A2/260RC1/re/npu/npusmi_007.html)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Steps and Methods](references/verification-method.md)
- [Device Queries Reference](references/device-queries.md)
- [Configuration Management Reference](references/configuration.md)
- [Firmware Upgrade Reference](references/firmware-upgrade.md)
- [Virtualization Reference](references/virtualization.md)
- [Certificate Management Reference](references/certificate-management.md)
- [Troubleshooting and Practical Experience](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration guidance]

**Output Format:** [Plain text and JSON command results, with human-facing status, error, and confirmation prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute local or SSH remote npu-smi and ascend-dmi commands; mutating operations require explicit confirmation.]

## Skill Version(s):

1.0.1 (source: evidence.release.version; artifact frontmatter lists 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
