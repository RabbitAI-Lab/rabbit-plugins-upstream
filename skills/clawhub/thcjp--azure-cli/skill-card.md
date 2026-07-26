## Description: <br>
Provides guidance and shell commands for installing and using Azure CLI to manage Azure cloud resources from an agent session. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and cloud operators use this skill to get Azure CLI installation, login, account-selection, and resource-management command guidance. It should be used with least-privilege credentials and explicit confirmation before commands that create, update, delete, deploy, or affect billing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to run Azure CLI commands against real cloud accounts, including commands that create, update, delete, deploy, or affect billing. <br>
Mitigation: Use a non-production Azure subscription or least-privilege credentials, and require explicit confirmation before any resource-changing or billing-affecting command. <br>
Risk: The skill scope and safety boundaries are underdefined. <br>
Mitigation: Review the skill before installing and limit execution to clearly scoped Azure tasks with user-approved commands. <br>
Risk: The artifact includes code-review and grading claims that are poorly scoped relative to the Azure CLI workflow. <br>
Mitigation: Treat those claims as unvalidated and do not rely on them as a separate capability without additional review. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/azure-cli) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>
- [Azure CLI Linux Installer](https://aka.ms/InstallAzureCliLinux) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples and structured JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose Azure CLI commands that require user confirmation, Azure credentials, network access, and attention to cost or resource changes.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
