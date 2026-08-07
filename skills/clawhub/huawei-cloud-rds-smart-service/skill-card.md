## Description: <br>
Huawei Cloud RDS Smart Service helps agents answer RDS questions, inspect and manage database instances, optimize SQL, troubleshoot faults, tune parameters, and guide backup or recovery workflows across supported Huawei Cloud RDS engines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DBAs, SREs, and operations teams use this skill to administer Huawei Cloud RDS instances, diagnose database issues, review logs and metrics, tune parameters, and plan backup or recovery tasks. The skill is intended for assisted RDS operations where mutating actions require explicit user confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide database-changing RDS operations such as restore, delete, failover, resize, parameter changes, security changes, and session termination. <br>
Mitigation: Use read-only IAM permissions first, scope access to specific projects or instances, and require explicit confirmation plus maintenance-window planning before mutating actions. <br>
Risk: Broad Huawei Cloud RDS permissions and AK/SK credentials could expose production database administration capabilities if mishandled. <br>
Mitigation: Protect AK/SK credentials, avoid full-access roles except for break-glass use, and grant only the least privileges needed for the intended workflow. <br>
Risk: Remote CLI installation scripts may introduce supply-chain risk if run without review. <br>
Mitigation: Inspect remote install scripts before execution and install the Huawei Cloud CLI only from trusted Huawei Cloud sources. <br>


## Reference(s): <br>
- [Huawei Cloud hcloud CLI Quick Start](https://support.huaweicloud.com/qs-hcli/hcli_02_003.html) <br>
- [RDS REST API Paths](references/api-paths.md) <br>
- [IAM Policies for RDS Smart Service](references/iam-policies.md) <br>
- [RDS Troubleshooting Guide](references/rds-troubleshooting-guide.md) <br>
- [SQL Performance Optimization Guide](references/sql-optimization-guide.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Dataflow Diagram](references/dataflow-diagram.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples, shell commands, Python snippets, checklists, and operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Structured command output is expected as JSON where CLI, SDK, or API calls are executed.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
