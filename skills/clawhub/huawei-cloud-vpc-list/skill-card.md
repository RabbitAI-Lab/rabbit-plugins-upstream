## Description:

Query Huawei Cloud VPCs for a tenant or project with filters and full pagination, returning VPC IDs, names, CIDR blocks, status, enterprise-project metadata, and total counts without creating, modifying, or deleting resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and network engineers use this skill to inventory and inspect Huawei Cloud VPCs for planning, troubleshooting, and enterprise-project audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The credential discovery logic may pick up unrelated Huawei Cloud environment secrets from the shell.

Mitigation: Run the skill in a dedicated environment with a single intended AK/SK pair and read-only VPC permissions.

Risk: Using credentials with broader permissions than needed increases blast radius if the runtime environment is misconfigured.

Mitigation: Scope IAM access to the documented read-only `vpc:vpcs:list` permission for the target project or enterprise project.

Risk: Temporary security-token variables may be matched by the script's broad environment scan.

Mitigation: Review the environment-variable matching before using temporary tokens and clear unrelated cloud secrets from the session.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-vpc-list)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, plus JSON VPC inventory or a plain-text table from the helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Huawei Cloud VPC query output; requires scoped AK/SK credentials, project ID, and region.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
