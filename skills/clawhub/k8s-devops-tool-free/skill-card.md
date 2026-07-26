## Description: <br>
Helps developers generate and lightly validate Kubernetes YAML manifests for common resources such as Deployments, Services, ConfigMaps, Secrets, Ingresses, Jobs, PVCs, and Namespaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and DevOps engineers use this skill to draft Kubernetes YAML manifests, create common application-stack resources, and review generated manifests before applying them to a cluster. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Kubernetes manifests may be incorrect, incomplete, or unsuitable for a target cluster. <br>
Mitigation: Review generated manifests, keep outputs in a clean or version-controlled directory, and run dry-run validation before applying them. <br>
Risk: Secret manifests can expose sensitive values if generated or stored carelessly. <br>
Mitigation: Inspect Secret manifests carefully and avoid committing real credentials or applying them without review. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/k8s-devops-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with YAML and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or write Kubernetes manifest files when the agent has file-write access.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
