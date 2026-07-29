## Description: <br>
Azure DevOps Tool Free helps agents manage Azure DevOps projects, repositories, branches, pull requests, and work items for personal or lightweight development workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual Azure DevOps users can use this skill to inspect projects, list repositories and branches, view pull requests, and prepare pull request creation commands through an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide PAT-backed Azure DevOps commands, including operations that create pull requests. <br>
Mitigation: Use a least-privilege Azure DevOps PAT and require explicit user confirmation before creating a pull request or running write-capable commands. <br>
Risk: The security review flags misleading local-only privacy claims because the skill can call external Azure DevOps APIs. <br>
Mitigation: Treat Azure DevOps API requests as networked data flow and avoid sending sensitive project details unless the user has approved the action. <br>
Risk: The security review flags overbroad activation guidance that may trigger outside Azure DevOps tasks. <br>
Mitigation: Use the skill only for Azure DevOps project, repository, branch, pull request, and work-item workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-devops-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure DevOps REST API commands and structured status or result summaries.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
