## Description:

Huawei Cloud DDS (Document Database Service) and DCS (Distributed Cache Service) unified management skill for querying, analyzing, creating, modifying, backing up, deleting, and restarting DDS/DCS resources through hcloud CLI commands and Huawei Cloud SDK fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operations engineers use this skill to manage Huawei Cloud DDS and DCS instances, review deployment and security posture, and generate safe command or SDK-based workflows for routine database and cache operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide destructive or billable Huawei Cloud DDS and DCS operations, including deletes, restarts, new instances, and added nodes.

Mitigation: Require explicit user confirmation for mutating operations, recommend backups before destructive changes, and prefer least-privilege IAM policies over wildcard admin permissions.

Risk: The security evidence notes opt-out quality reporting that can send run inputs, outputs, errors, stack traces, and an auth token to a configurable endpoint.

Mitigation: Disable quality reporting when telemetry is not desired, or configure SKILL_QUALITY_ENDPOINT only to a trusted endpoint.

Risk: The artifact includes hcloud CLI installation steps that download a binary and move it into a system path with elevated privileges.

Mitigation: Verify the hcloud binary source and checksum before installing it with sudo or adding it to a privileged path.

Risk: Huawei Cloud AK/SK credentials are required for CLI profiles or environment variables.

Mitigation: Keep AK/SK secrets out of shell history and source control, and use scoped credentials with only the permissions needed for the requested operation.

## Reference(s):

- [IAM Policies for DDS and DCS](references/iam-policies.md)
- [Detailed Command Reference](references/related-commands.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Verification Method](references/verification-method.md)
- [Data Flow Diagram](references/dataflow-diagram.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash commands, Python snippets, and JSON policy examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes confirmation guidance for mutating operations and may produce cloud resource management commands or security analysis recommendations.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
