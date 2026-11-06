## Description:

Lists Huawei Cloud CCE clusters through KooCLI, with an official SDK fallback, filters, and table, JSON, or names-only output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use it to inspect Huawei Cloud CCE cluster inventory by region and retrieve cluster IDs for follow-on CCE tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required telemetry wrapper's data collection is insufficiently explained, and the wrapper and downloaded installer were outside the reviewed artifact evidence.

Mitigation: Verify the wrapper and its data collection before installing, or disable reporting with SKILL_QUALITY_REPORT=0.

Risk: CCE_LIST_HCLOUD_BIN and CCE_LIST_HCLOUD_ARGS environment overrides can weaken the read-only guarantee.

Mitigation: Remove or tightly control these overrides and use a project-scoped read-only cloud identity.

## Reference(s):

- [Read-only IAM policy](references/iam-policies.md)
- [KooCLI installation and credential guide](references/cli-installation-guide.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Huawei Cloud KooCLI documentation](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Huawei Cloud KooCLI installer](https://cn-north-4-res.huaweicloud.com/cli/latest/install.sh)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text cluster table, JSON array, or cluster-name list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports region selection and client-side name or ID filtering.]

## Skill Version(s):

1.0.7 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
