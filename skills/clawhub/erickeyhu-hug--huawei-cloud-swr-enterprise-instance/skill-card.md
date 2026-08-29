## Description: <br>
Huawei Cloud SWR enterprise instance management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud platform engineers use this skill to administer Huawei Cloud SWR enterprise registry instances, including lifecycle, namespace, registry, repository, artifact, credential, endpoint, domain, statistics, and job workflows. <br>

### Deployment Geography for Use: <br>
Global, subject to Huawei Cloud SWR enterprise service availability by region. <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help administer cloud registry resources, including create, update, delete, credential, endpoint, domain, and artifact operations. <br>
Mitigation: Use least-privilege IAM, prefer temporary credentials, and require explicit user confirmation before executing create, update, delete, credential, public access, or domain changes. <br>
Risk: Registry credentials and Huawei Cloud AK/SK or security token values could be exposed if pasted into chat or shell history. <br>
Mitigation: Avoid pasting real secrets into chat, use environment variables or secure credential stores, and display only credential presence when verifying configuration. <br>
Risk: Public access, anonymous access, or broad IP allowlists can expose registry content more widely than intended. <br>
Mitigation: Review public access settings carefully, avoid 0.0.0.0/0 allowlists unless explicitly required, and keep production namespaces private with vulnerability controls enabled. <br>
Risk: Deleting instances, namespaces, repositories, artifacts, domains, or credentials can remove access or data permanently. <br>
Mitigation: Confirm the exact target identifiers, review deletion impact with the user, and verify backups or recovery plans before running destructive commands. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-swr-enterprise-instance) <br>
- [SWR Enterprise Instance Console](https://console.huaweicloud.com/swr-instance) <br>
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md) <br>
- [CLI Installation Guide](references/cli-installation-guide.md) <br>
- [Credential Configuration](references/credential-configuration.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Verification Method](references/verification-method.md) <br>
- [Common Pitfalls and Solutions](references/common-pitfalls.md) <br>
- [Task: Instance Lifecycle](references/task-instance-lifecycle.md) <br>
- [Task: Instance Namespaces](references/task-instance-namespaces.md) <br>
- [Task: Instance Registries and Repositories](references/task-instance-registries.md) <br>
- [Task: Instance Artifacts](references/task-instance-artifacts.md) <br>
- [Task: Instance Credentials](references/task-instance-credentials.md) <br>
- [Task: Instance Endpoints](references/task-instance-endpoints.md) <br>
- [Task: Instance Domains](references/task-instance-domains.md) <br>
- [Acceptance Criteria](references/acceptance-criteria.md) <br>
- [Output Format](references/output-format.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline hcloud CLI command examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose create, update, delete, credential, network access, and vulnerability scan operations that require user review before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
