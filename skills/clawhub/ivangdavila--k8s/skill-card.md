## Description: <br>
Helps agents debug Kubernetes workloads, review manifests, plan safe rollouts, tune resources, inspect cluster networking, storage, RBAC, security, autoscaling, backup, and node behavior. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, platform engineers, and operators use this skill to triage Kubernetes failures, review manifests and Helm or kustomize changes, propose safer kubectl workflows, and record durable operational findings without storing credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local operational notes may contain sensitive cluster topology, hostnames, RBAC gaps, incident history, and runbooks. <br>
Mitigation: Keep ~/Clawic/data/ private, review it periodically, and avoid pasting secrets into notes. <br>
Risk: Generated kubectl commands or manifests can affect live Kubernetes resources if applied without review. <br>
Mitigation: Review proposed commands, context, namespace, and blast radius; prefer kubectl diff or server-side dry-run before applying changes. <br>
Risk: The skill relies on local configuration and memory paths for cluster context, so stale notes can lead to poor operational guidance. <br>
Mitigation: Refresh recorded cluster facts after incidents, upgrades, topology changes, and accepted security exceptions. <br>


## Reference(s): <br>
- [Kubernetes Skill on ClawHub](https://clawhub.ai/ivangdavila/skills/k8s) <br>
- [Kubernetes Skill Homepage](https://clawic.com/skills/k8s) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with kubectl commands, Kubernetes manifest snippets, checklists, and concise operational guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write local operational notes under configured ~/Clawic/data paths; requires kubectl for cluster-facing commands.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
