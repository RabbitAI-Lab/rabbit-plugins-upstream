## Description:

Queries Huawei Cloud RDS instance lists, single-instance details, and CPU, memory, and disk monitoring metrics through the Huawei Cloud SDK.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yangaiwu](https://clawhub.ai/user/yangaiwu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and database administrators use this skill to inspect Huawei Cloud RDS inventory, troubleshoot individual database instances, and review basic monitoring metrics without performing write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Huawei Cloud credentials broadly by scanning HUAWEI, HW, and HWC-prefixed environment variables.

Mitigation: Run it with a dedicated least-privilege Huawei Cloud IAM user and avoid executing it in environments that contain unrelated Huawei Cloud secrets.

Risk: Authenticated SDK clients disable TLS certificate verification.

Mitigation: Do not use the skill until TLS certificate verification is enabled for IAM, RDS, and CES API calls.

Risk: RDS instance metadata and monitoring results can expose sensitive infrastructure information.

Mitigation: Restrict access to command output, logs, and shared transcripts that include instance IDs, network details, or monitoring data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yangaiwu/skills/huawei-cloud-rds-detail)
- [IAM permissions](artifact/iam-policies.md)
- [Verification method](artifact/verification-method.md)
- [Acceptance criteria](artifact/acceptance-criteria.md)
- [Dataflow diagram](artifact/dataflow-diagram.md)
- [Huawei Cloud RDS API documentation](https://console.huaweicloud.com/apiexplorer/#/openapi/RDS/doc)
- [Huawei Cloud CES API documentation](https://console.huaweicloud.com/apiexplorer/#/openapi/CES/doc)
- [Huawei Cloud SDK Center](https://console.huaweicloud.com/apiexplorer/#/sdkcenter)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output from the skill script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Huawei Cloud AK/SK credentials and may return sensitive infrastructure details such as instance IDs, network addresses, VPC IDs, subnet IDs, security group IDs, and monitoring data.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
