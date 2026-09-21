## Description:

Huawei Cloud LTS Manage helps agents administer Huawei Cloud LTS log groups, streams, indexes, transfers, alarms, and log searches through hcloud CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to query, configure, and troubleshoot Huawei Cloud LTS logging resources with generated hcloud CLI commands and verification guidance.

### Deployment Geography for Use:

Global, subject to Huawei Cloud LTS regional availability.

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Huawei Cloud LTS logging resources.

Mitigation: Prefer the read-only IAM policy for search and diagnostics, and grant write or delete permissions only when those operations are required.

Risk: Delete operations can remove log groups, streams, transfers, or alarm rules.

Mitigation: Require explicit user confirmation, use single-resource IDs, and prohibit batch deletion of all LTS resources.

Risk: Installing and authenticating hcloud introduces local CLI and credential handling risk.

Mitigation: Review the hcloud installer before running it, configure credentials with hcloud configure, and avoid hardcoded regions or credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-lts-manage)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [LTS Alarm Rule Configuration Reference](references/lts-alarm-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with hcloud CLI command blocks and JSON response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires hcloud CLI credentials and region-specific Huawei Cloud LTS parameters.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
