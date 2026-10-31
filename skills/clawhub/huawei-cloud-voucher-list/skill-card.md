## Description:

Lists Huawei Cloud BSS vouchers with filtering and table, JSON, or name-only output through KooCLI or the Huawei SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud account administrators and developers use this skill to review Huawei Cloud voucher inventory and retrieve voucher details for billing workflows.

### Deployment Geography for Use:

Global (Huawei Cloud BSS uses a global endpoint; the default region is cn-north-1).

## Known Risks and Mitigations:

Risk: Unchecked execution overrides may weaken the advertised safeguards.

Mitigation: Remove or constrain execution overrides and use dedicated read-only BSS credentials in a controlled environment.

Risk: The SDK fallback reads credential values directly, and agent output can contain voucher codes and billing fields.

Mitigation: Keep credentials in a controlled environment and limit access to voucher output. Verify the installer against Huawei's official instructions.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Read-only IAM Policy](references/iam-policies.md)
- [Verification Method](references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Voucher table, JSON array, or voucher-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include voucher codes, balances, and other billing fields.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
