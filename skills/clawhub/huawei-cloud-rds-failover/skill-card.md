## Description:

Huawei Cloud RDS failover drill skill that guides an agent through prepare, execute, and report phases for HA RDS instances, including IAM checks, controlled failover execution, monitoring collection, and HTML report generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to rehearse Huawei Cloud RDS primary/standby failover on HA database instances and produce readiness, execution, monitoring, and report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger a real Huawei Cloud RDS primary/standby failover.

Mitigation: Run it only for an intended HA RDS instance, confirm the configured region and instance_id, and use a maintenance window or test instance before passing --yes.

Risk: Limited execution-time safeguards may not prevent an operator from targeting the wrong database instance.

Mitigation: Review config/config.json, verify backups and rollback plans, and complete the prepare phase checks before execution.

Risk: Overbroad cloud permissions could expand the blast radius of a failover drill.

Mitigation: Grant only the documented RDS and CES actions needed for the drill and avoid wildcard RDS permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-rds-failover)
- [hcloud CLI installation and authentication guide](references/cli-installation-guide.md)
- [IAM policy guidance](references/iam-policies.md)
- [Acceptance criteria](references/acceptance-criteria.md)
- [Verification method](references/verification-method.md)
- [Huawei Cloud RDS product documentation](https://support.huaweicloud.com/productdesc-rds/)
- [RDS API reference: StartFailover](https://support.huaweicloud.com/api-rds/rds_06_0007.html)
- [CES monitoring metrics for RDS](https://support.huaweicloud.com/usermanual-ces/ces_03_0042.html)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Markdown, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON configuration, generated JSON/Markdown/HTML files, and an HTML failover report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a dry-run default; actual failover requires an explicit --yes flag.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
