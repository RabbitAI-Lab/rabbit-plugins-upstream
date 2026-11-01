## Description:

Lists Huawei Cloud bare-metal server instances with filtering and table, JSON, names-only, or Markdown inventory output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators can inventory Huawei Cloud Bare Metal Server instances in a tenant region, filter results, and export an inventory report. The skill is strictly read-only and can also provide server IDs for follow-up tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled installation guide asks users to run a downloaded script whose source could not be verified.

Mitigation: Use Huawei's official KooCLI installation instructions instead of the bundled download command until its source is verified.

Risk: Huawei credentials and exported server inventory can expose sensitive account or infrastructure information.

Mitigation: Grant only BMS read access, expose only the intended Huawei credentials, and protect exported inventory reports.

## Reference(s):

- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM policy guidance](references/iam-policies.md)
- [Verification method](references/verification-method.md)
- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-bms-list)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Console table or server-name list, raw JSON, or a Markdown inventory file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only inventory results with optional region, name, server ID, and status filters; Markdown exports include region, query time, total count, and a fixed inventory table.]

## Skill Version(s):

1.0.1 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
