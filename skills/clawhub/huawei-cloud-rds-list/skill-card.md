## Description:

Query Huawei Cloud RDS instances for the current tenant or project and return instance names by default, with optional read-only details such as ID, status, engine, flavor, private IPs, and creation time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dev-skills-operator](https://clawhub.ai/user/dev-skills-operator)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and cloud administrators use this skill to inventory and inspect Huawei Cloud RDS instances without performing write operations. It supports database inventory, daily inspection, cost review, and lookup of instance names or IDs for follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reports RDS query details and result snippets to an external telemetry endpoint by default.

Mitigation: Set SKILL_QUALITY_DISABLE=1 or remove the telemetry helper unless external reporting is explicitly approved.

Risk: Cloud inventory queries can expose sensitive resource names and metadata if run with broad account permissions.

Mitigation: Use a dedicated read-only RDS IAM principal with rds:instance:list or RDS ReadOnlyAccess, and avoid RDS FullAccess for this skill.

Risk: The installation guide includes piping a remote KooCLI installer script directly to bash.

Mitigation: Install KooCLI through a verified package manager or inspect the installer before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dev-skills-operator/skills/huawei-cloud-rds-list)
- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Huawei Cloud RDS Console](https://console.huaweicloud.com/rds)
- [KooCLI Installer](https://cn-north-4-hcli-cloud.obs.cn-north-4.myhuaweicloud.com/hcli/install.sh)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Plain text, TSV, or JSON results with Markdown guidance and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Names-only output prints one instance name per line; compact output prints TSV rows; full output is JSON containing instance metadata.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
