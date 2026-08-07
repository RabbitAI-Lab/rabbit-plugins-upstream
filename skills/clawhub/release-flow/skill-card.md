## Description: <br>
Release Flow guides agents through the redfoxhub-html Git release process for starting feature branches and deploying through develop and master. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xue-xiao-yu](https://clawhub.ai/user/xue-xiao-yu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and release engineers use this skill to coordinate project-specific Git branch creation, test deployment to develop, and production deployment to master for redfoxhub-html. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can push release branches that trigger test or production pipelines. <br>
Mitigation: Install it only for repositories that follow the redfoxhub-html workflow, and review each proposed Git command and confirmation prompt before execution. <br>
Risk: Merge or push operations can affect protected branches or stop on conflicts. <br>
Mitigation: Require a clean working tree, stop on conflicts or rejected pushes, and use the repository's merge request process when branch protections block direct pushes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/xue-xiao-yu/skills/release-flow) <br>
- [redfoxhub-html test pipeline](https://flow.aliyun.com/pipelines/4962314/current) <br>
- [redfoxhub-html production pipeline](https://flow.aliyun.com/pipelines/4946808/current) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes user confirmation prompts before branch creation, merges, pushes, and production deployment steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
