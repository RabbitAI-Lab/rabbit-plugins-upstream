## Description: <br>
Execute and manage Kubernetes clusters through kubectl commands for querying resources, deploying applications, debugging containers, managing configurations, and monitoring cluster health. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ddevaal](https://clawhub.ai/user/ddevaal) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and platform engineers use this skill to generate kubectl commands and operational guidance for inspecting, updating, debugging, and maintaining Kubernetes clusters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-impact Kubernetes commands can modify, delete, or disrupt cluster workloads. <br>
Mitigation: Use a least-privilege kubeconfig, avoid production contexts by default, and require explicit approval for write, delete, drain, scale, rollout, taint, exec, cp, and credential-related commands. <br>
Risk: Commands may run against the wrong cluster context or namespace. <br>
Mitigation: Verify the active kubeconfig context and namespace before each command, and prefer explicit --context and --namespace flags for operational changes. <br>
Risk: Diagnostic commands and logs can expose secrets, tokens, or sensitive cluster data. <br>
Mitigation: Do not paste live tokens into chat or recorded command logs, and review log or manifest output before sharing it. <br>


## Reference(s): <br>
- [kubectl Command Reference](references/REFERENCE.md) <br>
- [Official kubectl Docs](https://kubernetes.io/docs/reference/kubectl/) <br>
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/) <br>
- [Kubernetes API Reference](https://kubernetes.io/docs/reference/generated/kubernetes-api/) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Code] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include kubectl commands and helper script usage that require an installed kubectl binary and an active kubeconfig.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
