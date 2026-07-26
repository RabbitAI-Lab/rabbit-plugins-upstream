## Description: <br>
Huawei Cloud CCI instance management helps agents operate Cloud Container Instance namespaces, networks, deployments, statefulsets, pods, EIPPools, logs, and status queries through the hcloud CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[huaweiclouddev](https://clawhub.ai/user/huaweiclouddev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud operators, and site reliability engineers use this skill to create, update, inspect, troubleshoot, and clean up Huawei Cloud CCI serverless container resources from an agent-assisted command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled network helper has a local command-injection risk when auto-detecting the Huawei Cloud project ID. <br>
Mitigation: Do not use the helper until its shell=True project lookup is replaced with validated argument-list subprocess usage, or pass an already verified project ID and review the script before execution. <br>
Risk: The skill can guide agents through mutating and destructive Huawei Cloud CCI operations, including deleting namespaces and workloads. <br>
Mitigation: Use least-privilege temporary credentials, verify region, project, namespace, and resource names before every mutating command, and keep the documented two-step confirmation requirement for deletes. <br>
Risk: Credential mishandling could expose Huawei Cloud AK/SK or security tokens in agent conversation or command output. <br>
Mitigation: Configure credentials through profiles or environment variables, check only credential presence, and avoid printing, echoing, logging, or pasting secret values. <br>


## Reference(s): <br>
- [Acceptance Criteria: Correct vs Error Patterns for CCI Operations](references/acceptance-criteria.md) <br>
- [CCI Operation Catalog](references/cci-operation-catalog.md) <br>
- [CCI Common Workflows](references/common-workflows.md) <br>
- [Credential Configuration for hcloud CLI](references/credential-configuration.md) <br>
- [IAM Permission Policies for CCI Operations](references/iam-policies.md) <br>
- [CCI Parameter Format Rules](references/parameter-format.md) <br>
- [Deployment Lifecycle Management](references/task-deployment-management.md) <br>
- [EIPPool Management](references/task-eippool-management.md) <br>
- [Logs and Status Queries](references/task-logs-and-status.md) <br>
- [Namespace Lifecycle Management](references/task-namespace-management.md) <br>
- [Network Lifecycle Management](references/task-network-management.md) <br>
- [Pod Management](references/task-pod-management.md) <br>
- [StatefulSet Management](references/task-statefulset-management.md) <br>
- [Troubleshooting Guide for CCI hcloud CLI Issues](references/troubleshooting.md) <br>
- [Step-by-Step Verification Process for CCI Skill Functionality](references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown with inline bash and Python command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent responses should preserve credential secrecy, verify hcloud parameters with help output, and require explicit confirmation before destructive cloud operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
