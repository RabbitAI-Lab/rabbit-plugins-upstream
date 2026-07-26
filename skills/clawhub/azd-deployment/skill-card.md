## Description: <br>
Deploy containerized applications to Azure Container Apps using Azure Developer CLI (azd), Bicep infrastructure, remote ACR builds, managed identity, and troubleshooting guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegovind](https://clawhub.ai/user/thegovind) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and cloud engineers use this skill to configure azd projects, azure.yaml files, and Bicep modules for Azure Container Apps deployments. It is most useful when preparing or troubleshooting multi-service container deployments with environment variables, RBAC hooks, remote builds, and managed identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill includes cloud-changing azd and Azure CLI commands that can provision, deploy, modify, or delete Azure resources. <br>
Mitigation: Review the target tenant, subscription, resource group, environment name, deployment cost, and every generated command before running azd up, azd provision, azd deploy, azd env delete, or manual reset commands. <br>
Risk: Deployment hooks may create RBAC assignments and change access to Azure OpenAI, Azure AI Search, Container Registry, or Container Apps resources. <br>
Mitigation: Confirm each role, assignee, and scope before running hooks, and prefer least-privilege managed identity assignments. <br>
Risk: Some artifact examples include persistent registry credential patterns or commands that can expose environment values in logs. <br>
Mitigation: Prefer managed identity with AcrPull over ACR admin passwords or listCredentials, avoid sharing azd env get-values output, and keep secrets in azd-managed values or Key Vault references. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thegovind/skills/azd-deployment) <br>
- [Azure Developer CLI Deployment Acceptance Criteria](references/acceptance-criteria.md) <br>
- [azure.yaml Complete Schema Reference](references/azure-yaml-schema.md) <br>
- [Bicep Patterns for Azure Container Apps](references/bicep-patterns.md) <br>
- [Azure Developer CLI Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML, JSON, Bicep, shell command, and troubleshooting examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance may propose cloud-changing azd and Azure CLI commands that should be reviewed before execution.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
