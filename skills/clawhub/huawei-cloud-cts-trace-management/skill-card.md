## Description:

Helps agents query and analyze Huawei Cloud CTS audit traces, manage trackers and notifications, and assess trace retention using the hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Cloud operators, security engineers, and developers use this skill to inspect CTS audit activity, assess retention, and manage trackers and notifications. It previews changes and requires explicit confirmation before create or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The required reporting wrapper reads local agent session context and sends telemetry to an external service by default.

Mitigation: Review the reporting data flow before installation; use SKILL_QUALITY_DISABLE=1 or remove the wrapper where possible if external reporting is unacceptable.

Risk: The bundled reporting wrapper installs persistent local files and modifies shell startup configuration.

Mitigation: Review the installation script and its local changes before running it.

Risk: Creating or deleting CTS resources can change audit coverage.

Mitigation: Preview the exact command and its effects, then require explicit user confirmation before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/huaweicloudskill/skills/huawei-cloud-cts-trace-management)
- [CTS IAM policies](references/iam-policies.md)
- [CLI installation guide](references/cli-installation-guide.md)
- [Verification method](references/verification-method.md)
- [Data flow diagram](references/dataflow-diagram.md)

## Skill Output:

**Output Type(s):** [Analysis, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and structured audit results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only queries may run automatically; changes require preview and explicit confirmation.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
