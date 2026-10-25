## Description:

Lists Huawei Cloud BSS vouchers for a tenant account and presents the results as a detailed table, JSON, or a compact name list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Huawei Cloud account operators can review tenant voucher inventory for billing and cost-management tasks. The skill supports read-only listing with optional status, name, coupon ID, and region filters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags conflicting credential assurances and ambiguous account selection.

Mitigation: Use credentials limited to voucher listing, expose only the intended account's credential pair, and confirm the target account and region before querying.

Risk: The CLI installation steps have not been verified.

Mitigation: Verify the installer through Huawei's documentation before execution.

Risk: Displayed voucher codes and account details are private.

Mitigation: Treat command output as confidential and share only with intended recipients.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-voucher-list)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [CLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM policies](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Tabular text, raw JSON, or a compact voucher and plan-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports status, name, coupon ID, and region filters; voucher codes and account details may be sensitive.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
