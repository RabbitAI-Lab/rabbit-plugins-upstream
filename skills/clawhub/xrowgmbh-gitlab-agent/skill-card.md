## Description: <br>
An agent for interacting with GitLab. Supports gitlab.com and self-hosted instances. Requires no GitLab DUO. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to let an agent triage assigned GitLab issues and merge requests, create branches and merge requests, manage labels and status comments, inspect pipelines, and coordinate review through the glab CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill is designed to act on a GitLab account and may perform recurring write actions with broad authority. <br>
Mitigation: Install only when that automation is intended, use a least-privilege GitLab token limited to the target projects, and review a manual run before enabling the recurring job. <br>
Risk: The skill can push commits, create comments and labels, manage merge requests, trigger pipelines, set variables, create releases, and merge changes with limited confirmation. <br>
Mitigation: Require explicit approval for high-impact actions such as pushes, comments, labels, merge requests, merges, variable changes, releases, and pipeline actions unless the operating environment already provides equivalent review controls. <br>


## Reference(s): <br>
- [ClawHub GitLab Agent](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent) <br>
- [GitLab default roles and permissions](https://docs.gitlab.com/user/permissions/#default-roles) <br>
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/) <br>
- [OpenClaw creating skills guidance](https://docs.openclaw.ai/tools/creating-skills) <br>
- [xrow public skills project](https://gitlab.com/xrow-public/skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, GitLab API examples, JSON cron configuration, and code snippets.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; may perform GitLab write actions when deliberately enabled by the user.] <br>

## Skill Version(s): <br>
1.75.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
