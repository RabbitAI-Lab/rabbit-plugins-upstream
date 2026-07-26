## Description: <br>
K8s Aiops helps agents operate kubeconfig-reachable Kubernetes clusters by listing and inspecting resources, reading logs, running read-only diagnostics, and performing governed write operations such as scaling, rollouts, deletes, namespace changes, and node cordon, uncordon, or drain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, platform engineers, and SREs use this skill to inspect Kubernetes state, diagnose unhealthy workloads, review pod logs and events, and execute governed operational changes through CLI or MCP tools. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform high-impact cluster writes using the privileges of the configured kubeconfig. <br>
Mitigation: Use a dedicated least-privilege kubeconfig, prefer read-only RBAC by default, and grant delete, drain, rollout undo, or namespace mutation verbs only when explicitly needed. <br>
Risk: MCP write tools can mutate real cluster state without an internal approval gate. <br>
Mitigation: Review production or shared-cluster use before installation, scope targets and namespaces tightly, use dry-run previews where supported, and rely on Kubernetes RBAC as the enforcement boundary. <br>
Risk: Insecure kubeconfig TLS settings can weaken the cluster connection. <br>
Mitigation: Check kubeconfig TLS settings before use and avoid contexts that rely on insecure-skip-tls-verify for production or shared clusters. <br>


## Reference(s): <br>
- [k8s-aiops homepage](https://github.com/AIops-tools/K8s-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text with inline shell commands, CLI examples, and MCP tool guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe Kubernetes API results, dry-run previews, audit behavior, undo guidance, and RBAC or kubeconfig troubleshooting.] <br>

## Skill Version(s): <br>
0.8.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
