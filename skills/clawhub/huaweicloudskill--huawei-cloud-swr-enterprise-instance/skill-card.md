## Description:

Huawei Cloud SWR enterprise instance management skill using hcloud CLI for lifecycle, namespace, registry, repository, artifact, credential, endpoint, domain, statistics, and job operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweicloudskill](https://clawhub.ai/user/huaweicloudskill)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to administer Huawei Cloud SWR enterprise registry resources, including instances, namespaces, registries, repositories, artifacts, credentials, endpoints, domains, statistics, and job status. It helps plan and run hcloud CLI or helper-script workflows for SWR enterprise operations.

### Deployment Geography for Use:

Global, subject to Huawei Cloud SWR enterprise regional availability.

## Known Risks and Mitigations:

Risk: Create and delete operations can affect billable SWR enterprise resources or permanently remove registry data.

Mitigation: Require an explicit human-approved plan before create or delete actions, and confirm the exact instance, namespace, repository, artifact, endpoint, or domain target before execution.

Risk: Broad credentials or long-lived secrets can expand the impact of an incorrect command.

Mitigation: Use least-privilege IAM policies, prefer temporary credentials, and avoid exposing AK, SK, or security token values in prompts, logs, or output.

Risk: Network exposure settings can unintentionally open registry access.

Mitigation: Review endpoint and public whitelist changes before applying them, and avoid allow-all whitelist settings unless the operator has explicitly approved that exposure.

## Reference(s):

- [SWR Enterprise Instance Console](https://console.huaweicloud.com/swr-instance)
- [Command Reference](references/command-reference.md)
- [Parameter Reference](references/parameter-reference.md)
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md)
- [Output Format](references/output-format.md)
- [Credential Configuration](references/credential-configuration.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [Task: Instance Lifecycle](references/task-instance-lifecycle.md)
- [Task: Instance Namespaces](references/task-instance-namespaces.md)
- [Task: Instance Registries and Repositories](references/task-instance-registries.md)
- [Task: Instance Artifacts](references/task-instance-artifacts.md)
- [Task: Instance Credentials](references/task-instance-credentials.md)
- [Task: Instance Endpoints](references/task-instance-endpoints.md)
- [Task: Instance Domains](references/task-instance-domains.md)
- [CLI Installation Guide](references/cli-installation-guide.md)
- [Acceptance Criteria](references/acceptance-criteria.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, code, guidance]

**Output Format:** [Markdown with inline shell commands, configuration examples, and JSON output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose hcloud CLI commands or Python helper invocations; cloud-changing actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
