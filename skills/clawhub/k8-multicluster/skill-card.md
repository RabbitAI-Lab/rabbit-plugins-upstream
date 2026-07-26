## Description: <br>
Manage multiple Kubernetes clusters, switch contexts, and perform cross-cluster operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and platform engineers use this skill to inspect, compare, and operate multiple Kubernetes clusters, including context switching, Cluster API lifecycle tasks, Helm deployments, GitOps workflows, and federation patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can help an agent operate across multiple Kubernetes clusters, including production contexts. <br>
Mitigation: Use least-privileged kubeconfigs, keep production contexts read-only by default, and require human approval before write operations. <br>
Risk: The skill includes workflows that may retrieve or move kubeconfigs and secrets. <br>
Mitigation: Treat kubeconfigs and secrets as sensitive credentials; avoid raw manual secret copying and enforce secure storage, auditing, rotation, and cleanup. <br>
Risk: Implicit or incorrect context selection can apply commands to the wrong cluster. <br>
Mitigation: Require explicit Kubernetes context names for operations and review the target cluster and namespace before execution. <br>
Risk: Cluster lifecycle, Helm, GitOps, and manifest operations can change live infrastructure. <br>
Mitigation: Review generated commands and manifests before execution, stage changes in non-production clusters first, and audit cross-cluster operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/rohitg00/skills/k8-multicluster) <br>
- [Kubernetes Context Management](CONTEXT-SWITCHING.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline command and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may include Kubernetes context names, namespace names, manifests, and operational commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
