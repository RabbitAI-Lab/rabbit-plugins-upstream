## Description: <br>
Helps an agent guide Azure CLI installation, login, subscription selection, resource group creation, resource listing, and related Azure operations from command-line examples. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, DevOps engineers, and cloud operators use this skill to get Azure CLI setup steps, command suggestions, and troubleshooting guidance for Azure resource management. Users should review proposed commands before execution because they can affect cloud resources, credentials, and costs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An agent may propose or run Azure CLI commands against an authenticated subscription. <br>
Mitigation: Require the agent to show the exact az command, target subscription, target resource group, expected changes, and cost impact before approving any state-changing command. <br>
Risk: The skill mixes Azure cloud operations with code review and generic workflow claims, which can lead to use outside its clearest scope. <br>
Mitigation: Use it only for Azure CLI tasks and avoid relying on it for code review, development policy, or unrelated workflow automation. <br>
Risk: Azure CLI guidance can affect cloud credentials, protected resources, and billable infrastructure. <br>
Mitigation: Use least-privilege Azure credentials, avoid sharing secrets in prompts or logs, and manually confirm resource names, regions, and cost implications. <br>


## Reference(s): <br>
- [ClawHub azure-cli skill page](https://clawhub.ai/thcjp/skills/azure-cli) <br>
- [Azure CLI Linux installer](https://aka.ms/InstallAzureCliLinux) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown with inline shell and PowerShell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure CLI command proposals, setup steps, troubleshooting guidance, and structured JSON-style examples.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact/SKILL.md frontmatter reports 1.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
