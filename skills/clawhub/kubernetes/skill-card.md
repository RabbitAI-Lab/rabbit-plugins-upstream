## Description: <br>
Kubernetes Agent Swarm is an instruction-only multi-agent skill for Kubernetes and OpenShift platform operations, coordinating Orchestrator, Cluster Ops, GitOps, Security, Observability, Artifacts, and Developer Experience agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kcns008](https://clawhub.ai/user/kcns008) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to coordinate Kubernetes and OpenShift operations, including cluster health checks, GitOps deployments, security review, observability triage, artifact management, and developer onboarding. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide an agent operating with live Kubernetes/OpenShift, cloud, registry, GitOps, and incident-response authority. <br>
Mitigation: Scope credentials to least privilege and require explicit human approval before production changes, deletes, secret reads or writes, alert silences, external notifications, git writes, and deployment approvals. <br>
Risk: Generated shell commands may affect cluster state if executed without review. <br>
Mitigation: Review proposed commands before execution, prefer read-only checks first, and apply environment-specific change controls for state-changing operations. <br>
Risk: Action logs or broad git persistence could capture sensitive operational details. <br>
Mitigation: Use path-limited commits and redacted logs; avoid storing secrets, tokens, kubeconfig data, or incident payloads in persisted files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kcns008/skills/kubernetes) <br>
- [Kubernetes Agent Swarm README](artifact/README.md) <br>
- [Quick Reference - Agent Operating Rules](artifact/QUICKREF.md) <br>
- [Troubleshooting Knowledge Base](artifact/troubleshooting/TROUBLESHOOTING.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only skill; requires KUBECONFIG and kubectl, with optional cluster, cloud, registry, GitOps, and incident-response tooling depending on task.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
