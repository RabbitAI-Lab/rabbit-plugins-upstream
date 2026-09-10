## Description:

Checks Huawei Cloud MRS Redis nodes-*.conf metadata files for seven integrity issues that can cause Redis startup failures, connection anomalies, or fault alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations engineers use this skill to inspect provided MRS Redis nodes-*.conf files, identify metadata integrity failures, and generate repair-oriented diagnostic reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes production repair steps such as stopping instances, copying metadata files, editing files, and deleting backups.

Mitigation: Treat remediation as a human-reviewed runbook; confirm the affected cluster, target file paths, backup, rollback plan, and operator authorization before executing any production action.

Risk: The referenced IAM policy uses wildcard resources for MRS permissions.

Mitigation: Grant only the minimum read-only MRS permissions needed for diagnosis and scope access as narrowly as the Huawei Cloud environment supports.

Risk: The skill performs static analysis and cannot independently verify live Redis cluster state.

Mitigation: Require operators to provide the relevant nodes-*.conf files and validate any recommended repair against current cluster status before making changes.

## Reference(s):

- [IAM Policies - MRS Redis Meta Check](artifact/references/iam-policies.md)
- [ClawHub skill page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-mrs-redis-meta-check)
- [ClawHub publisher profile](https://clawhub.ai/user/huaweiclouddev)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown diagnostic report with check results and remediation guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports pass/fail status for seven Redis metadata checks and appends repair guidance when failures are found.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
