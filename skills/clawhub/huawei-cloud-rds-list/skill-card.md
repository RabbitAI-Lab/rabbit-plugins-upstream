## Description:

Lists Huawei Cloud RDS instances in a selected region and returns a table, JSON array, or compact name list with optional filters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wlc-dev](https://clawhub.ai/user/wlc-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and developers use this skill to inspect Huawei Cloud RDS inventory by region, filter instances by status, name, engine, or ID, and provide instance details to follow-on workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted RDS_LIST_HCLOUD_BIN or RDS_LIST_HCLOUD_ARGS environment values can bypass the advertised read-only command guard.

Mitigation: Remove executable and argument overrides, or ensure their environment values are trusted; use credentials limited to listing instances.

Risk: RDS inventory output may expose private infrastructure details, and cloud credentials are sensitive.

Mitigation: Treat inventory output as private, keep credentials outside chat, and verify the CLI installer through Huawei's official distribution guidance.

## Reference(s):

- [KooCLI Installation and Credential Guide](references/cli-installation-guide.md)
- [Huawei Cloud KooCLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [Least-Privilege IAM Policy](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Release](https://clawhub.ai/wlc-dev/skills/huawei-cloud-rds-list)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [Plain-text instance table or name list, or a JSON array of instance records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Region-scoped inventory with optional filters; status filtering is applied locally. Instance data may contain private infrastructure details.]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
