## Description: <br>
Debugs Kubernetes workloads and reviews manifests across pods, rollouts, Services, Ingress, DNS, storage, RBAC, autoscaling, nodes, backups, GPU workloads, and production safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, SREs, and operators use this skill to triage Kubernetes incidents, review workload manifests, generate safer kubectl command sequences, and plan production changes such as rollouts, drains, upgrades, backup, and restore. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can maintain long-lived local Kubernetes memory and shared inventory files that may contain sensitive operational context. <br>
Mitigation: Review or disable automatic writes in sensitive environments and ensure saved notes contain pointers, not credentials or secret-bearing command output. <br>
Risk: Suggested live-cluster actions such as migrations, deletes, drains, applies, or force operations can change production state. <br>
Mitigation: Require explicit confirmation, verify the current kubectl context, and review the blast radius before executing state-changing commands. <br>
Risk: Cluster diagnostics may expose sensitive environment dumps, manifests, secrets references, or operational topology in chat. <br>
Mitigation: Redact credentials and sensitive outputs before sharing them with an agent, and prefer references such as env vars, kubeconfig paths, vault paths, or secret-store item names. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/k8s) <br>
- [Publisher Profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic Skill Homepage](https://clawic.com/skills/k8s) <br>
- [Skill Definition](artifact/SKILL.md) <br>
- [Kubernetes Working File Templates](artifact/memory-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline kubectl commands, YAML snippets, checklists, and concise diagnostic explanations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose file updates for local Kubernetes memory, shared server inventory, and shared domain inventory; requires kubectl for live-cluster workflows.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
