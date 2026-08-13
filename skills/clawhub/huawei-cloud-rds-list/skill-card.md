## Description:

Lists Huawei Cloud RDS instances for the current tenant or project, returning instance names by default and optional read-only details such as IDs, status, engine, flavor, private IPs, and created time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and FinOps reviewers use this skill to inventory Huawei Cloud RDS instances, check their basic status, and retrieve instance names or IDs for follow-up work without performing write operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Default quality reporting may send execution data, including cloud inventory details, errors, or stack traces, to an external endpoint.

Mitigation: Set SKILL_QUALITY_DISABLE=1 before use or require an audited SKILL_QUALITY_ENDPOINT that satisfies the deployment's data-handling requirements.

Risk: The skill accesses Huawei Cloud inventory data and may expose RDS names, IDs, VPC IDs, regions, and status information in local output or reports.

Mitigation: Use a dedicated Huawei Cloud IAM identity with only rds:instance:list or RDS ReadOnlyAccess, and avoid using credentials with write permissions.

Risk: The installation guidance includes a curl-to-bash path for installing the Huawei Cloud CLI.

Mitigation: Verify the installer source through the normal software supply-chain review process or use an approved package manager path before running it.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-rds-list)
- [Publisher Profile](https://clawhub.ai/user/erickeyhu-hug)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; runtime output is plain text, TSV, or JSON depending on flags.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only RDS listing; names-only output is one instance name per line, compact output is TSV, and full output is JSON.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
