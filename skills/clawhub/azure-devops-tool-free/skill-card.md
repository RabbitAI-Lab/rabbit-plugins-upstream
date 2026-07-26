## Description: <br>
Azure DevOps Base helps personal developers inspect Azure DevOps projects, repositories, branches, pull requests, and work items, and create pull requests through Azure DevOps API commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and individual Azure DevOps users use this skill to browse projects, repositories, and branches, review pull request lists, and draft pull request creation commands for lightweight workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses PAT-backed Azure DevOps API access and includes pull request creation examples. <br>
Mitigation: Use a least-privilege Azure DevOps PAT, confirm the target organization, project, repository, and branch before use, and require explicit approval before any POST or write action. <br>
Risk: The artifact claims local-only data handling, but Azure DevOps requests send relevant project, repository, branch, pull request, and authentication data to Azure DevOps APIs. <br>
Mitigation: Treat API calls as external data sharing with Azure DevOps and avoid sending credentials or repository details unless the user has approved the action. <br>
Risk: The security verdict is suspicious due to broad triggers and misleading data handling claims. <br>
Mitigation: Review the skill before installing or running it, and limit use to the documented Azure DevOps read and pull request workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-devops-tool-free) <br>
- [Azure DevOps projects API endpoint example](https://dev.azure.com/${AZURE_DEVOPS_ORG}/_apis/projects?api-version=7.1) <br>
- [Azure DevOps pull request API endpoint example](https://dev.azure.com/${ORG}/${PROJ}/_apis/git/repositories/${REPO_ID}/pullrequests?api-version=7.1) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, text, markdown] <br>
**Output Format:** [Markdown with inline bash commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure DevOps organization, project, repository, branch, pull request, and PAT-related configuration details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
