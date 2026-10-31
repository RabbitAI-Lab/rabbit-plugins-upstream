## Description:

Guides operators through assessing and converting a Huawei Cloud RDS for MySQL single instance to primary/standby high availability, including prechecks, cost review, backup options, and post-conversion verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators and database engineers use this skill to evaluate and guide a Huawei Cloud RDS for MySQL single-to-primary/standby conversion, from precondition and cost checks through result verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Verification examples may delete existing database data.

Mitigation: Create a unique database exclusively for each run and clean up only that database.

Risk: Setup examples may expose cloud credentials.

Mitigation: Configure credentials through interactive hcloud setup and use limited cloud permissions.

Risk: The single-to-HA conversion is irreversible and may incur prepaid charges.

Mitigation: Keep a usable backup and obtain explicit approval of the target, conversion, and prepaid charges before invoking the conversion.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-rds-mysql-replica-promotion)
- [Huawei Cloud RDS Single-to-HA API](https://support.huaweicloud.com/api-rds/rds_01_0103.html)
- [Huawei Cloud RDS Single-to-HA User Guide](https://support.huaweicloud.com/usermanual-rds-mysql/rds_05_0023.html)
- [KooCLI Installation Guide](https://support.huaweicloud.com/qs-hcli/hcli_02.html)
- [KooCLI Usage Guide](https://support.huaweicloud.com/usermanual-hcli/hcli_05_01.html)
- [Risks and Impact](references/risks-and-impact.md)
- [Cost Estimation](references/cost-estimation.md)
- [Backup Time](references/backup-time.md)
- [Monitoring Comparison](references/monitoring-comparison.md)
- [Verification Method](references/verification-method.md)
- [IAM Policies](references/iam-policies.md)
- [Business Verification](references/business-verification.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance, shell commands, and JSON workflow reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports cover prechecks, cost estimates, monitoring, and conversion results.]

## Skill Version(s):

1.0.0 (source: frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
