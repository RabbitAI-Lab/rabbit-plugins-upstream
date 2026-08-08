## Description: <br>
Huawei Cloud CCI Instance Management helps agents manage Huawei Cloud CCI namespaces, networks, workloads, EIPPools, logs, and status through hcloud CLI guidance and helper-script workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[erickeyhu-hug](https://clawhub.ai/user/erickeyhu-hug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to plan and execute Huawei Cloud CCI serverless container lifecycle operations, including namespace setup, network creation, workload deployment, status checks, log review, public IP configuration, and cleanup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables high-impact administration of Huawei Cloud CCI resources, including operations that can delete namespaces, workloads, networks, EIPPools, and other cloud resources. <br>
Mitigation: Use least-privilege temporary credentials, avoid broad CCI FullAccess unless necessary, and require explicit confirmation before destructive operations. <br>
Risk: The bundled helper script has a concrete command-injection weakness in shell command construction when region values are untrusted. <br>
Mitigation: Do not use the helper with untrusted region values until the shell command construction is fixed. <br>
Risk: Logs, events, EIP details, Secrets, RBAC operations, and pod exec are sensitive or high-impact actions. <br>
Mitigation: Treat these actions as sensitive, limit who can request them, and avoid exposing credentials or sensitive output in conversations. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/erickeyhu-hug/skills/huawei-cloud-cci-instance-management) <br>
- [Acceptance Criteria: Correct vs Error Patterns for CCI Operations](artifact/references/acceptance-criteria.md) <br>
- [CCI Operation Catalog](artifact/references/cci-operation-catalog.md) <br>
- [CCI Common Workflows](artifact/references/common-workflows.md) <br>
- [Credential Configuration for hcloud CLI](artifact/references/credential-configuration.md) <br>
- [IAM Permission Policies for CCI Operations](artifact/references/iam-policies.md) <br>
- [CCI Parameter Format Rules](artifact/references/parameter-format.md) <br>
- [Deployment Lifecycle Management](artifact/references/task-deployment-management.md) <br>
- [EIPPool Management](artifact/references/task-eippool-management.md) <br>
- [Logs and Status Queries](artifact/references/task-logs-and-status.md) <br>
- [Namespace Lifecycle Management](artifact/references/task-namespace-management.md) <br>
- [Network Lifecycle Management](artifact/references/task-network-management.md) <br>
- [Pod Management](artifact/references/task-pod-management.md) <br>
- [StatefulSet Management](artifact/references/task-statefulset-management.md) <br>
- [Troubleshooting Guide for CCI hcloud CLI Issues](artifact/references/troubleshooting.md) <br>
- [Step-by-Step Verification Process for CCI Skill Functionality](artifact/references/verification-method.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, code] <br>
**Output Format:** [Markdown guidance with inline hcloud CLI commands, JSON output expectations, and Python helper usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose high-impact cloud administration commands that require explicit user confirmation before destructive operations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
