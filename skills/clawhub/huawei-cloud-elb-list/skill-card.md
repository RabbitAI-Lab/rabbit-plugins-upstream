## Description:

Lists Huawei Cloud ELB load balancers through KooCLI or the Huawei Cloud SDK fallback, with filters and table, JSON, or Markdown output; the API operation is read-only.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect tenant ELB inventories by region, filter load balancers, and retrieve IDs or VIP addresses for follow-on tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional setup helper weakens download security while installing SDK dependencies.

Mitigation: Use a trusted existing KooCLI installation, or retain certificate verification and install pinned dependencies in an isolated environment.

Risk: Environment settings can replace the hcloud command or add arguments to it.

Mitigation: Leave ELB_LIST_HCLOUD_BIN and ELB_LIST_HCLOUD_ARGS unset.

Risk: Default list modes write inventory data to elb-list.md.

Mitigation: Choose a safe destination with --md-out or disable the file output with --no-md.

## Reference(s):

- [KooCLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Huawei Cloud KooCLI official quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-privilege read-only IAM policy](artifact/references/iam-policies.md)
- [Verification method](artifact/references/verification-method.md)
- [Data flow diagram](artifact/references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [ID and name table, raw JSON, compact name list, or Markdown inventory table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default table and name-list modes write an inventory Markdown file; use --no-md to disable. JSON mode does not write the file.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
