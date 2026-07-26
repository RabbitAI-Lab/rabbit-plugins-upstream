## Description: <br>
Configure Kubernetes autoscaling with HPA, VPA, and KEDA for horizontal and vertical pod autoscaling, event-driven scaling, and capacity management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rohitg00](https://clawhub.ai/user/rohitg00) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and platform engineers use this skill to design, inspect, and troubleshoot Kubernetes autoscaling with HPA, VPA, and KEDA for workload capacity and cost management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated autoscaling manifests or commands could affect the wrong cluster, namespace, or workload. <br>
Mitigation: Confirm the active cluster context, namespace, target workload, and rollback plan before applying changes. <br>
Risk: Incorrect min/max replica limits or scale-to-zero settings can create capacity, latency, or availability problems. <br>
Mitigation: Review replica bounds, activation thresholds, cold-start impact, and stabilization settings before production use. <br>


## Reference(s): <br>
- [KEDA Trigger Reference](KEDA-TRIGGERS.md) <br>
- [ClawHub skill page](https://clawhub.ai/rohitg00/skills/k8-autoscaling) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML manifests and command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review generated Kubernetes changes before applying them to a cluster.] <br>

## Skill Version(s): <br>
1.0.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
