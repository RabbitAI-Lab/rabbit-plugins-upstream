## Description: <br>
Huawei Cloud SWR enterprise instance management skill using hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud platform engineers, and registry administrators use this skill to manage Huawei Cloud SWR enterprise instances, namespaces, registries, repositories, artifacts, credentials, endpoints, domains, statistics, and jobs through hcloud CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential and registry secret exposure during SWR authentication, credential creation, or registry synchronization workflows. <br>
Mitigation: Use least-privilege IAM credentials, avoid displaying returned secrets in chat or logs, and confirm target registry credentials before storing or updating them. <br>
Risk: Public access, anonymous access, or disabled certificate verification can expose registry resources beyond the intended audience. <br>
Mitigation: Prefer private namespaces, keep --insecure=false, use IP allowlists for public endpoints, and require explicit confirmation before enabling public or anonymous access. <br>
Risk: Delete operations can permanently remove instances, namespaces, repositories, artifacts, credentials, endpoints, domains, or job records. <br>
Mitigation: Require explicit user confirmation for destructive operations and verify affected resources before executing deletion commands. <br>
Risk: Instance creation can incur ongoing cloud charges, and installer commands can introduce supply-chain risk if fetched from an untrusted source. <br>
Mitigation: Confirm billing impact before creating paid instances and verify the hcloud installer through a trusted Huawei source before running it. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/huaweiclouddev/skills/huawei-cloud-swr-enterprise-instance) <br>
- [SWR Instance API Reference Guide](references/swr-instance-api-guide.md) <br>
- [Task: Instance Lifecycle](references/task-instance-lifecycle.md) <br>
- [Task: Instance Namespaces](references/task-instance-namespaces.md) <br>
- [Task: Instance Registries and Repositories](references/task-instance-registries.md) <br>
- [Task: Instance Artifacts](references/task-instance-artifacts.md) <br>
- [Task: Instance Credentials](references/task-instance-credentials.md) <br>
- [Task: Instance Endpoints](references/task-instance-endpoints.md) <br>
- [Task: Instance Domains](references/task-instance-domains.md) <br>
- [IAM Permission Policies](references/iam-policies.md) <br>
- [Credential Configuration for hcloud CLI](references/credential-configuration.md) <br>
- [CLI Installation Guide - hcloud (KooCLI)](references/cli-installation-guide.md) <br>
- [KooCLI Command Format Guide](references/cli-format-guide.md) <br>
- [Common Pitfalls & Solutions](references/common-pitfalls.md) <br>
- [Huawei Cloud SWR Documentation](https://support.huaweicloud.com/swr/index.html) <br>
- [hcloud CLI Documentation](https://support.huaweicloud.com/cli/index.html) <br>
- [Huawei Cloud API Explorer](https://apiexplorer.developer.huaweicloud.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline hcloud and docker command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON-shaped CLI parameters, IAM policy snippets, verification steps, and safety confirmations for sensitive operations.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
