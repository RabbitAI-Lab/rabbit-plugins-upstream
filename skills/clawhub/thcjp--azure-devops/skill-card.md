## Description: <br>
Helps agents list Azure DevOps projects, repositories, and branches, create pull requests, and manage work items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to inspect Azure DevOps project state, support pull request workflows, and coordinate work items from an agent conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose or run actions that may use local credentials or CLI configuration. <br>
Mitigation: Review each Azure DevOps action before execution and start with low-privilege credentials. <br>
Risk: The skill may change external Azure DevOps resources, including pull requests, work items, branches, or pipelines. <br>
Mitigation: Confirm whether an action is read-only or mutating before running it, and avoid high-privilege tokens until the documentation separates those actions clearly. <br>
Risk: The documentation is inconsistent with the stated Azure DevOps behavior. <br>
Mitigation: Validate expected inputs, outputs, and side effects in a test project before installing or using it in production workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/azure-devops) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured text with optional JSON examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Azure DevOps credentials, network access, and review before actions that change external resources.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
