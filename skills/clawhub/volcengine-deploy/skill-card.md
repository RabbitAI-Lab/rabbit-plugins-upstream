## Description: <br>
Deploys a local project directory or Git repository to Volcengine as a running, reachable cloud service. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[volc-sdk-team](https://clawhub.ai/user/volc-sdk-team) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan, approve, provision, deploy, and verify applications on Volcengine targets including ECS, VKE, and veFaaS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or mutate Volcengine cloud resources, which may affect cost, exposure, and cleanup responsibilities. <br>
Mitigation: Require a reviewed deployment plan, validation proof, explicit approval evidence, and resource ledger or Terraform state before provisioning. <br>
Risk: The deployment workflow handles secrets and runtime configuration for applications and managed dependencies. <br>
Mitigation: Keep secrets out of logs, summaries, and ledgers; write local secret files with restrictive permissions and resolve Kubernetes Secrets before applying workloads. <br>
Risk: Public endpoints, VKE LoadBalancers, EIPs, and temporary artifact transfer can expose services or deployment artifacts. <br>
Mitigation: Review public exposure in the resource plan, restrict SSH when enabled, prefer private dependency endpoints, and avoid printing or persisting pre-signed artifact URLs. <br>


## Reference(s): <br>
- [Deployment Plan Template](artifact/references/deployment-plan-template.md) <br>
- [Dockerfile Templates](artifact/references/dockerfile-templates.md) <br>
- [ECS Deployment Details](artifact/references/ecs-deploy-steps.md) <br>
- [veFaaS Skill Execution](artifact/references/faas-deploy-steps.md) <br>
- [Kubernetes Manifest Templates](artifact/references/k8s-manifests.md) <br>
- [Deployment Service-Linked Roles](artifact/references/service-linked-roles.md) <br>
- [Supported Runtime Dependencies](artifact/references/supported-dependencies.md) <br>
- [VKE Deployment Details](artifact/references/vke-deploy-steps.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, JSON state files, deployment plans, and generated configuration/templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create .volcengine deployment state, resource ledgers, Docker/Kubernetes/systemd artifacts, and cleanup commands during use.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
