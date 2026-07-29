## Description: <br>
Huawei Cloud SWR enterprise instance management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operations teams use this skill to administer Huawei Cloud SWR enterprise instances, namespaces, registries, repositories, artifacts, credentials, endpoints, domains, statistics, and jobs through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can administer Huawei Cloud SWR enterprise registries, including credential creation, public access changes, and deletion of registry resources. <br>
Mitigation: Use least-privilege IAM, require explicit confirmation for destructive operations, and review planned hcloud commands before execution. <br>
Risk: Cloud access keys, security tokens, registry passwords, or generated credentials could be exposed in chat or logs. <br>
Mitigation: Prefer temporary credentials or secure hcloud profiles, check credential presence without printing values, and never paste real AK/SK, tokens, or passwords into prompts or logs. <br>
Risk: Network or TLS settings could broaden registry exposure, such as public access from 0.0.0.0/0 or insecure TLS use. <br>
Mitigation: Restrict public access with narrow IP allowlists and avoid insecure TLS except for tightly controlled troubleshooting. <br>


## Reference(s): <br>
- [SWR Enterprise Instance Console](https://console.huaweicloud.com/swr-instance) <br>
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md) <br>
- [CLI Installation Guide - hcloud (KooCLI)](references/cli-installation-guide.md) <br>
- [Credential Configuration for hcloud CLI](references/credential-configuration.md) <br>
- [IAM Permission Policies - SWR Enterprise Instance Skill](references/iam-policies.md) <br>
- [Task: Instance Lifecycle](references/task-instance-lifecycle.md) <br>
- [Task: Instance Namespaces](references/task-instance-namespaces.md) <br>
- [Task: Instance Registries and Repositories](references/task-instance-registries.md) <br>
- [Task: Instance Artifacts](references/task-instance-artifacts.md) <br>
- [Task: Instance Credentials](references/task-instance-credentials.md) <br>
- [Task: Instance Endpoints](references/task-instance-endpoints.md) <br>
- [Task: Instance Domains](references/task-instance-domains.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [SWR Enterprise Instance Output Format](references/output-format.md) <br>
- [Verification Method - SWR Enterprise Instance Skill](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with hcloud CLI commands, configuration snippets, IAM policy JSON, and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include region names, resource identifiers, credential-handling guidance, and confirmation prompts for destructive or cost-incurring operations.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
