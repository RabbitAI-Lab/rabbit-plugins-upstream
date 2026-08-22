## Description:

Huawei Cloud RDS Smart Service helps agents answer RDS questions, inspect and troubleshoot database instances, optimize SQL performance, tune parameters, and guide backup and recovery workflows across supported Huawei Cloud RDS engines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, DBAs, SREs, and cloud operations teams use this skill to operate Huawei Cloud RDS instances, diagnose database issues, optimize slow SQL, tune parameters, and plan backup or recovery actions with human review for changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions with broad database-changing authority, including restart, resize, failover, restore, delete, session-kill, and security-policy changes.

Mitigation: Use least-privilege Huawei Cloud IAM roles scoped to specific intended RDS instances and require manual review before any mutating operation.

Risk: Credential handling for Huawei Cloud AK/SK authentication can expose secrets if users paste keys into chat or command lines.

Mitigation: Use controlled admin environments and environment-variable or managed credential handling; do not paste real secrets into prompts or shell history.

Risk: Installer and helper scripts may execute cloud administration commands in environments with privileged credentials.

Mitigation: Inspect scripts before installation or execution and test with read-only or non-production permissions before granting production access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-rds-smart-service)
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html)
- [IAM Policies for RDS Smart Service](references/iam-policies.md)
- [RDS REST API Paths](references/api-paths.md)
- [RDS Troubleshooting Guide](references/rds-troubleshooting-guide.md)
- [SQL Performance Optimization Guide](references/sql-optimization-guide.md)
- [Verification Method](references/verification-method.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured tables, JSON-oriented command output, and inline shell or Python examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Mutating RDS actions are expected to require explicit user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
