## Description: <br>
Azure Infra helps agents use a local Azure CLI session to query, diagnose, audit, and manage Azure resources, defaulting to read-only operations and requiring explicit confirmation for write or destructive changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and operators use this skill to inventory Azure resources, review health, audit security posture, analyze cost data, and prepare controlled Azure CLI changes across subscriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Azure CLI commands can change, delete, scale, or alter access to cloud resources when a user deliberately requests write, IAM, billing, or destructive actions. <br>
Mitigation: Keep routine work read-only; before any write action, verify the displayed subscription, target resource, full command, and expected impact, then require explicit user confirmation. <br>
Risk: The skill operates through the user's local Azure CLI session, so results and side effects depend on the currently authenticated account, tenant, and subscription. <br>
Mitigation: Check Azure CLI login state and subscription context before running commands, and clearly label the subscription or tenant used for resource-scope results. <br>
Risk: Azure administration workflows can expose sensitive values if credential-bearing resources are queried too broadly. <br>
Mitigation: Do not print or log access keys, client secrets, tokens, passwords, or raw Key Vault secret values; report only names and metadata for secrets. <br>


## Reference(s): <br>
- [Azure Infra on ClawHub](https://clawhub.ai/thcjp/skills/azure-infra) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline Azure CLI command examples and structured JSON-style result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should identify the active Azure subscription or tenant when relevant and avoid exposing secrets, tokens, passwords, or raw Key Vault secret values.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
