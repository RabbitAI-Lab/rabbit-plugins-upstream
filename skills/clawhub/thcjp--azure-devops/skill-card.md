## Description: <br>
Claims to help agents list Azure DevOps projects, repositories, and branches, create pull requests, manage work items, and support CI/CD coordination. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and project teams use this skill to inspect Azure DevOps resources, coordinate pull requests and work items, and report project status in agent-assisted workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Documentation is inconsistent and does not clearly constrain Azure DevOps write actions. <br>
Mitigation: Use only in a low-risk project until the publisher clarifies exact commands, required permissions, confirmation behavior, and expected outputs. <br>
Risk: The skill asks for command execution and may perform remote write operations such as pull request or work item changes. <br>
Mitigation: Use least-privilege Azure DevOps credentials, require explicit user confirmation before write operations, and review generated commands before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/azure-devops) <br>
- [Publisher Profile](https://clawhub.ai/user/thcjp) <br>
- [Skill Homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown and JSON-like status summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Azure DevOps project, repository, branch, pull request, work item, or pipeline status details.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
