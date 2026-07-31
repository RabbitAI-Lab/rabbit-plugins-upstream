## Description: <br>
An agent for interacting with GitLab. Supports gitlab.com and self-hosted instances. Requires no GitLab DUO. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to operate GitLab issues, merge requests, branches, pipelines, labels, variables, and releases through the glab CLI. It is intended for agents that need to perform assigned GitLab work with project access and assignment checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad unattended GitLab authority can change repositories and project state. <br>
Mitigation: Use a dedicated GitLab bot account with least-privilege, project-scoped access and remove unneeded variable, release, merge, and approval permissions. <br>
Risk: Recurring execution can repeatedly mutate repositories without direct operator review. <br>
Mitigation: Keep the 15-minute cron disabled unless unattended repository mutation is intended and operationally reviewed. <br>
Risk: The project access gate is only reliable if its helper script executes correctly. <br>
Mitigation: Fix and test the helper script execution issue before relying on the security gate for access control. <br>


## Reference(s): <br>
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles) <br>
- [CI Tools Components Catalog](https://ci-tools.xrow.de/) <br>
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label) <br>
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills) <br>
- [xrow Public Skills Project](https://gitlab.com/xrow-public/skills) <br>
- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent) <br>
- [Publisher Profile](https://clawhub.ai/user/xrowgmbh) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands, GitLab CLI commands, GraphQL and REST API examples, and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab and jq, and uses GITLAB_TOKEN for GitLab authentication.] <br>

## Skill Version(s): <br>
1.78.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
