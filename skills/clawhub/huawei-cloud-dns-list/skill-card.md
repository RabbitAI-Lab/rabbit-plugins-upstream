## Description:

Lists Huawei Cloud DNS zones and record sets with filters and table, JSON, or name-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and operations engineers use it to inspect public or private DNS zones and record sets, filter inventories, and retrieve zone details for follow-on work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unchecked region value can redirect authenticated requests outside Huawei Cloud.

Mitigation: Restrict regions to approved Huawei endpoints, remove the unchecked endpoint fallback, and use credentials limited to DNS listing.

Risk: Live cloud behavior and the remote installer remain unverified.

Mitigation: Install through verified Huawei vendor instructions and validate behavior in a controlled account before wider use.

## Reference(s):

- [Least-Privilege IAM Policies](artifact/references/iam-policies.md)
- [KooCLI Installation and Credential Guide](artifact/references/cli-installation-guide.md)
- [Verification Method](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [ClawHub Skill Release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-dns-list)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Tabular text, a JSON array, or a newline-separated domain-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports public or private zones, record sets, filters, and paginated results.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
