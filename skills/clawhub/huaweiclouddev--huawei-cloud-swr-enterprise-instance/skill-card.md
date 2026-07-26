## Description: <br>
Huawei Cloud SWR enterprise instance management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud administrators use this skill to manage Huawei Cloud SWR enterprise instances, namespaces, registries, repositories, artifacts, credentials, endpoints, domains, statistics, and job status through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose powerful Huawei Cloud registry administration actions, including irreversible deletion of instances, namespaces, repositories, artifacts, credentials, endpoints, domains, or job records. <br>
Mitigation: Use least-privilege IAM permissions and require explicit confirmation before running destructive commands. <br>
Risk: Credential-related workflows can expose AK/SK values, security tokens, registry access secrets, or returned authentication tokens if output is shared or logged carelessly. <br>
Mitigation: Prefer temporary credentials, redact returned tokens and secrets, check credential presence without printing values, and store long-term credentials only in secure secret stores. <br>
Risk: Public access, anonymous access, insecure TLS, and broad IP allowlists can unintentionally expose registry resources. <br>
Mitigation: Keep anonymous access and insecure TLS disabled unless explicitly required, use narrow IP allowlists, and review endpoint and domain settings before applying changes. <br>


## Reference(s): <br>
- [Credential Configuration](references/credential-configuration.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md) <br>
- [Task: Instance Lifecycle](references/task-instance-lifecycle.md) <br>
- [Task: Instance Namespaces](references/task-instance-namespaces.md) <br>
- [Task: Instance Registries and Repositories](references/task-instance-registries.md) <br>
- [Task: Instance Artifacts](references/task-instance-artifacts.md) <br>
- [Task: Instance Credentials](references/task-instance-credentials.md) <br>
- [Task: Instance Endpoints](references/task-instance-endpoints.md) <br>
- [Task: Instance Domains](references/task-instance-domains.md) <br>
- [Output Format](references/output-format.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls and Solutions](references/common-pitfalls.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with hcloud CLI commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON response examples and cautions for credentials, public access, and destructive cloud operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
