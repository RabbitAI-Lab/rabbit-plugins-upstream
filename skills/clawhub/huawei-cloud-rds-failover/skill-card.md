## Description:

Automates a Huawei Cloud RDS high-availability failover exercise by preparing instance and IAM checks, executing the failover when explicitly confirmed, collecting logs and CES metrics, and generating an HTML report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations teams use this skill to rehearse Huawei Cloud RDS primary-standby failover, verify HA readiness, and produce an operational report for MySQL, PostgreSQL, SQL Server, or MariaDB RDS instances.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the execute phase with --yes can perform a real Huawei Cloud RDS primary-standby failover and may interrupt service.

Mitigation: Use dry-run mode first, verify config/config.json points to the intended instance, and run --yes only for an approved non-production test or maintenance window.

Risk: A broadly privileged hcloud profile could allow the skill to affect more resources than needed.

Mitigation: Use a least-privilege Huawei Cloud profile limited to the required RDS and CES actions documented in references/iam-policies.md.

## Reference(s):

- [hcloud CLI Installation and Authentication Guide](references/cli-installation-guide.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Verification Method](references/verification-method.md)
- [Huawei Cloud RDS Product Documentation](https://support.huaweicloud.com/productdesc-rds/zh-cn_topic_dashboard.html)
- [RDS API Reference: StartFailover](https://support.huaweicloud.com/api-rds/rds_05_0013.html)
- [CES Monitoring Metrics for RDS](https://support.huaweicloud.com/usermanual-rds-mysql/rds_06_0001.html)
- [Huawei Cloud Region Endpoints](https://support.huaweicloud.com/regionendpoints/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands plus generated JSON, Markdown, and HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generates experiment configuration, execution results, readiness reports, and a standalone failover HTML report.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
