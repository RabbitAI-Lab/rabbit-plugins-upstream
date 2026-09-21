## Description:

Manages Huawei Cloud DEW secrets and encryption keys with CSMS/KMS metadata queries, rotation and key-usage analysis, and confirmation-gated KMS/CSMS management commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and security engineers use this skill to inspect Huawei Cloud CSMS secret metadata, review DEW/KMS rotation and key usage, and prepare confirmation-gated commands for key or secret lifecycle operations without exposing secret values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad secret-management triggers may activate the skill during generic conversations about secrets or credentials.

Mitigation: Install it only for deliberate Huawei Cloud DEW/CSMS/KMS work and do not allow generic secrets conversations to trigger it automatically.

Risk: The skill can prepare write actions that affect KMS keys, CSMS rotation, and secret versions.

Mitigation: Use a dedicated least-privilege cloud principal, restrict regions and resources where possible, avoid production for write actions unless explicitly approved, and preserve preview plus confirmation gates.

Risk: Automatic quality telemetry can report execution metadata through SKILL_QUALITY_* settings.

Mitigation: Disable or tightly control SKILL_QUALITY_* telemetry settings unless reporting is explicitly needed.

## Reference(s):

- [ClawHub Skill Release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-dew-key-management)
- [CLI Installation Guide](artifact/references/cli-installation-guide.md)
- [CSMS Usage Guide](artifact/references/csms-usage.md)
- [KMS Usage Guide](artifact/references/kms-usage.md)
- [IAM Policies](artifact/references/iam-policies.md)
- [Verification Method](artifact/references/verification-method.md)
- [Data Flow Diagram](artifact/references/dataflow-diagram.md)
- [Huawei Cloud DEW Documentation](https://support.huaweicloud.com/dew/)
- [Huawei Cloud DEW API Explorer](https://console.huaweicloud.com/apiexplorer/#/openapi/DEW/doc)
- [Huawei Cloud KooCLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with inline hcloud shell commands and JSON summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Metadata-only secret handling; management actions require preview and explicit confirmation.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
