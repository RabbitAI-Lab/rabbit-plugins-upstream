## Description:

Lists Huawei Cloud CCE clusters by region and formats results as a table, JSON, or cluster names, with optional name and ID filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud administrators and engineers use it to inspect a region's CCE cluster inventory, filter clusters by name or ID, and obtain cluster IDs for follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI telemetry wrapper's reporting contents and destination are not clearly explained.

Mitigation: Clarify what is reported and where before use, or disable reporting with SKILL_QUALITY_REPORT=0.

Risk: Executable overrides can undermine the read-only safeguard, which is not an authorization boundary.

Mitigation: Use a trusted execution environment without executable overrides and credentials limited to CCE cluster listing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/wlc-dev/skills/huawei-cloud-cce-list)
- [KooCLI installation and credential guide](artifact/references/cli-installation-guide.md)
- [Least-privilege IAM policy](artifact/references/iam-policies.md)
- [Verification method and API details](artifact/references/verification-method.md)
- [Huawei Cloud KooCLI quick start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain-text cluster table or names list, or JSON array]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only cluster inventory with optional region, name, and ID filters.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
