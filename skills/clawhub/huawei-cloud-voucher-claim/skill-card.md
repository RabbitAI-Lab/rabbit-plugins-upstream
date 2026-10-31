## Description:

Claim Huawei Cloud BSS vouchers for enterprise sub-accounts, preview transfers, and inspect the resulting coupon inventory.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and developers use this skill to transfer a specified amount of a transferable Huawei Cloud BSS coupon from an enterprise master account to a sub-account, then review the resulting coupon inventory.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A transaction ledger placed in a shared directory can overwrite other local files.

Mitigation: Keep the ledger in a private directory you own and avoid the documented /tmp example until a secure temporary-file fix is available.

Risk: A live voucher claim moves value to a sub-account and is normally irreversible.

Mitigation: Use --dry-run to check the customer, coupon, and amount before claiming, confirm the transfer explicitly, and use narrowly scoped BSS permissions.

## Reference(s):

- [CLI installation and credential setup](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM policy](artifact/references/iam-policies.md)
- [API and behavior verification notes](artifact/references/verification-method.md)
- [Huawei Cloud BSS endpoint](https://bss.myhuaweicloud.com)
- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-voucher-claim)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Coupon inventory as a human-readable table or JSON, with request previews and actionable status messages.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The inventory can be skipped; live claims require explicit confirmation.]

## Skill Version(s):

1.0.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
