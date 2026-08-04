## Description: <br>
k8s-aiops helps agents inspect, diagnose, and operate kubeconfig-reachable Kubernetes clusters with governed read and write workflows, audit records, dry-run support, and undo metadata for reversible writes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zw008](https://clawhub.ai/user/zw008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and SREs use this skill to query Kubernetes resources, review logs and events, run read-only diagnostics, and perform governed operational changes such as scaling, rollouts, deletion, namespace operations, and node maintenance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform destructive Kubernetes changes using the permissions available in the configured kubeconfig. <br>
Mitigation: Install it only for agents that should operate Kubernetes and prefer a narrowly scoped or read-only ServiceAccount by default. <br>
Risk: Production admin credentials would allow the agent to delete workloads or namespaces, drain nodes, change images, and apply stored undo actions. <br>
Mitigation: Do not connect production admin kubeconfigs unless those actions are intended and governed by the operator. <br>
Risk: The local k8s-aiops state directory contains audit history and undo metadata. <br>
Mitigation: Protect the state directory, relocate it only when needed, and keep it accessible only to trusted users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zw008/skills/k8s-aiops) <br>
- [Project homepage](https://github.com/AIops-tools/K8s-AIops) <br>
- [Capabilities](references/capabilities.md) <br>
- [CLI Reference](references/cli-reference.md) <br>
- [Setup Guide](references/setup-guide.md) <br>
- [Agent Guardrails](references/agent-guardrails.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands, configuration snippets, and structured Kubernetes operation guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke read and write Kubernetes operations through the k8s-aiops CLI or MCP server, subject to the permissions of the configured kubeconfig.] <br>

## Skill Version(s): <br>
0.10.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
