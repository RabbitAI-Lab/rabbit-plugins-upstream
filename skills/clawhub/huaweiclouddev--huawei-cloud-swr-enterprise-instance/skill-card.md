## Description:

Huawei Cloud SWR enterprise instance management skill using hcloud CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to manage Huawei Cloud SWR enterprise instances and related namespaces, registries, repositories, artifacts, credentials, endpoints, domains, statistics, and jobs. It helps agents provide hcloud CLI workflows, configuration guidance, prerequisite checks, IAM policy guidance, and verification steps for SWR enterprise instance administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide broad administration of Huawei Cloud SWR enterprise resources.

Mitigation: Use least-privilege IAM policies and grant write permissions only for the specific operations the user intends to perform.

Risk: Instance creation, deletion, public access, anonymous access, and credential issuance can create cost, exposure, or irreversible changes.

Mitigation: Require explicit user confirmation before these operations and verify target instance, namespace, endpoint, and credential identifiers before execution.

Risk: Huawei Cloud AK/SK values, security tokens, and registry secrets may be exposed if handled carelessly.

Mitigation: Prefer temporary credentials where possible, never echo or paste real secrets into chat or command output, and verify credential presence with masked CLI/profile checks.

Risk: The Python helper performs SDK-backed instance creation and depends on the user's local IAM and hcloud configuration.

Mitigation: Review the helper behavior before use and run it only in an environment configured for the intended Huawei Cloud account, region, VPC, and subnet.

## Reference(s):

- [Command Reference](references/command-reference.md)
- [Parameter Reference](references/parameter-reference.md)
- [SWR Instance API Guide](references/swr-instance-api-guide.md)
- [Credential Configuration](references/credential-configuration.md)
- [IAM Permission Policies](references/iam-policies.md)
- [Verification Method](references/verification-method.md)
- [Common Pitfalls](references/common-pitfalls.md)
- [Instance Lifecycle](references/task-instance-lifecycle.md)
- [Instance Namespaces](references/task-instance-namespaces.md)
- [Instance Registries](references/task-instance-registries.md)
- [Instance Artifacts](references/task-instance-artifacts.md)
- [Instance Credentials](references/task-instance-credentials.md)
- [Instance Endpoints](references/task-instance-endpoints.md)
- [Instance Domains](references/task-instance-domains.md)
- [Huawei Cloud SWR Enterprise Instance Console](https://console.huaweicloud.com/swr-instance)
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-enterprise-instance)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include hcloud CLI commands, Python helper invocation guidance, IAM policy JSON, credential handling guidance, and verification checklists.]

## Skill Version(s):

1.0.3 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
