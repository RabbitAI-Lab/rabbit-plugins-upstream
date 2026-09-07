## Description:

Huawei Cloud LTS (Log Tank Service) log traffic statistics, log context query, host group and access config inspection, collection status patrol, and OBS transfer management for batch log export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to inspect Huawei Cloud LTS traffic anomalies, retrieve concise log context, patrol collection health, and manage scoped OBS transfer exports for troubleshooting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags setup and credential guidance as weak for a skill that can read and export logs and manage transfer tasks.

Mitigation: Review the CLI installer source through a trusted Huawei channel, use least-privilege and preferably short-lived credentials, and avoid placing AK/SK secrets in persistent shell profiles.

Risk: OBS transfer creation or deletion can incur storage and transfer costs or affect exported log availability.

Mitigation: Require explicit user confirmation before CreateTransfer or DeleteTransfer and scope every transfer to a specified log group and log stream.

Risk: The skill operates on potentially sensitive operational logs.

Mitigation: Use read-only IAM permissions when export is not needed and limit context retrieval to concise fragments during troubleshooting.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [IAM Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [LTS API Reference](references/lts-api-reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline hcloud CLI commands and structured diagnostic checklists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Concise log context fragments are capped by the artifact guidance at 500 lines before or after the target log.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
