## Description: <br>
An agent for interacting with GitLab. Supports gitlab.com and self-hosted instances. Requires no GitLab DUO. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xrowgmbh](https://clawhub.ai/user/xrowgmbh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to let an agent manage assigned GitLab issues, merge requests, branches, labels, comments, CI pipelines, and release workflow tasks through the GitLab CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad autonomous authority to change repositories, issues, merge requests, and pipelines using the user's GitLab identity. <br>
Mitigation: Install only for a tightly controlled GitLab account or project where autonomous repository changes are acceptable. <br>
Risk: A broadly scoped GitLab token could allow unwanted changes across more projects than intended. <br>
Mitigation: Use a minimally scoped token and confirm protected-branch and CI policies prevent unwanted changes. <br>
Risk: Recurring automation could repeat undesired actions before the behavior is reviewed. <br>
Mitigation: Avoid enabling the recurring job until a manual run has proven the behavior is acceptable. <br>


## Reference(s): <br>
- [GitLab Default Roles and Permissions](https://docs.gitlab.com/user/permissions/#default-roles) <br>
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/) <br>
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label) <br>
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills) <br>
- [xrow Public Skills Project](https://gitlab.com/xrow-public/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires glab and GITLAB_TOKEN; actions may create or update GitLab issues, merge requests, branches, labels, comments, and CI pipelines.] <br>

## Skill Version(s): <br>
1.77.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
