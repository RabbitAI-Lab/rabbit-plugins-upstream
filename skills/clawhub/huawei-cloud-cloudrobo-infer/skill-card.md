## Description:

Manage CloudRobo inference services by deploying models, querying services and logs, starting or stopping services, updating or deleting services, and polling deployment completion with wait-deploy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and platform operators use this skill to manage Huawei Cloud CloudRobo model-serving services, from resolving workspace, model, and compute inputs through deployment, monitoring, log diagnosis, and lifecycle operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included verification script can start, stop, update, or delete a real CloudRobo inference service when SERVICE_ID is set, and those actions can consume compute resources or remove service state.

Mitigation: Review the script before running it, keep SERVICE_ID unset unless the target service is disposable, use least-privilege Huawei Cloud credentials, and require explicit user confirmation before mutating operations.

Risk: CloudRobo operations depend on Huawei Cloud AK/SK credentials and downloaded model configuration that may contain sensitive or untrusted values.

Mitigation: Load AK/SK values from protected environment or user config only, avoid logging credentials or generated environment values, and treat downloaded model configuration as untrusted input before using it in deployment commands.

## Reference(s):

- [CLI Installation Guide](references/cli-installation-guide.md)
- [Authentication & Access Control](references/iam-policies.md)
- [Dataflow Diagram](references/dataflow-diagram.md)
- [Service Config Reference](references/service-config-catalog.md)
- [Validation Rules](references/validation-rules.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline CLI commands and JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational cautions for credentials, workspace scope, mutating service actions, compute consumption, and log timestamp units.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
