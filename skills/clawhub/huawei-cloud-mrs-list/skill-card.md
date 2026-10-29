## Description:

Lists Huawei Cloud MapReduce Service clusters in a tenant region through KooCLI, with filters, paging, and table, JSON, or name-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use the skill to inspect MRS cluster inventory, filter by state or name, and retrieve cluster identifiers for follow-on work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The MRS_LIST_HCLOUD_BIN and MRS_LIST_HCLOUD_ARGS environment overrides are identified as able to bypass the advertised read-only safeguard.

Mitigation: Remove or tightly control both overrides, and use a dedicated read-only cloud identity.

Risk: The bundled installation instructions use a script source that the security review has not verified.

Mitigation: Obtain KooCLI through Huawei's verified distribution instructions and check the installer integrity before running it.

## Reference(s):

- [KooCLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Least-privilege MRS IAM policy](artifact/references/iam-policies.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [A full-field table, JSON array, or cluster-name list.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region, cluster-state, and cluster-name filters; results are paged automatically.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
