## Description: <br>
Cluster API lifecycle management for provisioning, scaling, and upgrading Kubernetes clusters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and platform engineers use this skill to inspect and manage Kubernetes Cluster API resources, including provisioning clusters, retrieving kubeconfigs, scaling machine deployments, upgrading clusters, and troubleshooting machine or provisioning failures. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mutating Cluster API examples can provision, scale, upgrade, or otherwise change Kubernetes infrastructure with cost, quota, or availability impact. <br>
Mitigation: Before running mutating examples, verify the kubeconfig context, namespace, target cluster, provider account, manifest contents, quota, and expected cost or availability impact. <br>
Risk: Returned kubeconfigs may grant access to workload clusters if exposed in chat, logs, tickets, or shared outputs. <br>
Mitigation: Do not expose kubeconfigs unless intentionally authorized, and handle them as sensitive access material. <br>


## Reference(s): <br>
- [Kubernetes Skills on ClawHub](https://clawhub.ai/rohitg00/skills/k8s-capi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with Python tool-call examples and Kubernetes YAML manifests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Cluster API resource status, Kubernetes manifests, and kubeconfig material when used with connected tools.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
