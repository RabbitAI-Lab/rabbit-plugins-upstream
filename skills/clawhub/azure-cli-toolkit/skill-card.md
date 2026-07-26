## Description: <br>
Azure Cli Toolkit helps agents guide Azure CLI authentication, batch resource operations, scripted deployments, multi-subscription management, cost analysis, and policy compliance checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, cloud engineers, and operations teams use this skill to ask an agent for Azure CLI command guidance, automation patterns, and review steps for managing Azure resources across environments and subscriptions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bulk Azure CLI commands can delete, stop, or deallocate cloud resources at scale. <br>
Mitigation: Require the agent to list exact target resources, subscription, resource group, and environment before proposing destructive commands, and require a separate approval before execution. <br>
Risk: Cross-subscription automation can affect the wrong tenant, subscription, or environment. <br>
Mitigation: Confirm the active account and subscription before each scoped operation, and prefer explicit subscription and resource group arguments over ambient CLI state. <br>
Risk: Service principal credentials and tokens may be exposed through logs, shell history, or transcripts. <br>
Mitigation: Store credentials in approved secret managers, avoid echoing secret values, and redact authentication material from shared outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-cli-toolkit) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure CLI commands, environment variable setup, operational checks, and structured result examples.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
