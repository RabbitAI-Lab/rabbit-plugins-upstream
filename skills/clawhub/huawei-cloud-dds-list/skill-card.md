## Description:

Lists Huawei Cloud DDS instances for a tenant or project, returning instance names by default and optional read-only details such as id, status, mode, engine, version, VPC, and creation time.

This skill is ready for commercial/non-commercial use.

## Publisher:

[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, cloud operators, and database administrators use this skill to inventory Huawei Cloud DDS instances, inspect read-only status and mode information, and support daily checks or cost review without changing database resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The DDS listing flow is read-only, but execution telemetry and summarized results are sent to an external operations endpoint by default.

Mitigation: Install only if this telemetry behavior is acceptable, use a least-privilege DDS read-only IAM user, verify the KooCLI installer source, and set SKILL_QUALITY_DISABLE=1 unless telemetry is explicitly approved.

## Reference(s):

- [IAM Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-dds-list)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with bash commands; runtime output is plain text names, compact TSV rows, or JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only listing with optional filters for region, name, id, mode, datastore type, VPC, subnet, limit, and offset.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
