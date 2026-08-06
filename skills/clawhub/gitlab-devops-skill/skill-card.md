## Description:

Manage GitLab projects from the command line by listing or inspecting projects, listing and creating issues, listing, creating, or merging merge requests, and listing or triggering CI/CD pipelines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[weiguang1017](https://clawhub.ai/user/weiguang1017)

### License/Terms of Use:

MIT

## Use Case:

Developers and DevOps engineers use this skill to operate GitLab.com or self-managed GitLab projects from an agent-assisted command-line workflow, including project inspection, issue and merge request workflows, and CI/CD pipeline checks or triggers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact GitLab write actions such as creating issues or merge requests, merging merge requests, and triggering pipelines.

Mitigation: Require explicit confirmation before write actions and confirm the project, branch or ref, merge request IID, and target GitLab URL before execution.

Risk: A broad GitLab token can expose more project access than a task requires.

Mitigation: Use a project-scoped or read-only token whenever possible and grant broad api scope only when write operations are required.

Risk: Implicit invocation can run against a real GitLab token if the agent environment is already configured.

Mitigation: Review the skill before installing it in environments with live GitLab credentials and keep tokens outside version control.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/weiguang1017/gitlab-devops-skill)
- [ClawHub skill page](https://clawhub.ai/weiguang1017/skills/gitlab-devops-skill)
- [GitLab](https://gitlab.com)
- [RestartX support](https://service.restartx.top/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands print JSON to stdout and exit non-zero on failure.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
