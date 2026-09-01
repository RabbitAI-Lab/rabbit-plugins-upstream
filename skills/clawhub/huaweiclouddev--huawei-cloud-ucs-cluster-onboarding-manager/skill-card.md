## Description:

Manages Huawei Cloud UCS cluster onboarding, lifecycle operations, fleet grouping, kubeconfig access, and quota checks through hcloud CLI guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud platform engineers use this skill to onboard CCE or self-managed Kubernetes clusters into Huawei Cloud UCS, organize them into fleet groups, retrieve access configuration, and verify quotas and permissions. It is intended for operational UCS administration where generated commands are reviewed before execution.

### Deployment Geography for Use:

Global, subject to Huawei Cloud UCS regional availability

## Known Risks and Mitigations:

Risk: The skill may guide an agent through operations that require powerful Huawei Cloud UCS and Kubernetes credentials.

Mitigation: Use least-privilege IAM permissions, prefer temporary credentials, avoid exposing AK/SK, security tokens, or kubeconfig contents in chats or logs, and store kubeconfigs with restrictive permissions.

Risk: Registration, deregistration, fleet reassignment, and federation kubeconfig operations can change service state, incur costs, or remove management capabilities.

Mitigation: Require explicit human review and confirmation before executing any registration, deletion, update, fleet association, or federation kubeconfig command.

Risk: Incorrect UCS category or Kubernetes version assumptions can cause failed onboarding or misleading authentication-style errors.

Mitigation: Query supported UCS versions dynamically, verify the cluster category before choosing the kubeconfig workflow, and consult the documented pitfalls before retrying failed operations.

## Reference(s):

- [UCS Cluster Onboarding API Reference Guide](references/ucs-cluster-onboarding-api-guide.md)
- [Task: Cluster Registration](references/task-cluster-registration.md)
- [Task: Fleet Management](references/task-fleet-management.md)
- [Task: Access Management](references/task-access-management.md)
- [IAM Permission Policies](references/iam-policies.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [KooCLI Command Format Standard](references/kocli-command-format.md)
- [Parameter Reference](references/parameter-reference.md)
- [UCS Cluster Onboarding Manager Output Format](references/output-format.md)
- [Verification Method](references/verification-method.md)
- [Acceptance Criteria](references/acceptance-criteria.md)
- [Common Pitfalls and Solutions](references/common-pitfalls.md)
- [Huawei Cloud CLI Documentation](https://support.huaweicloud.com/cli/index.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON policy snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes hcloud CLI commands, IAM policy examples, kubeconfig handling guidance, and verification checklists.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
