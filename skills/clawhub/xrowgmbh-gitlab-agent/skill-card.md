## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent operate assigned GitLab issues and merge requests, including guarded project-access checks, branch and MR delivery, CI follow-up, labels, comments, reviewer assignment, and recurring work discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can take autonomous write actions in GitLab, including branch pushes, merge request creation, labels, reviewer assignment, comments, and pipeline actions.

Mitigation: Install it only for tightly controlled GitLab accounts and projects where these actions are acceptable, and review the configured scope before use.

Risk: The recurring job guidance can keep the agent acting every 15 minutes.

Mitigation: Keep the recurring job disabled until a manual run and GitLab authentication check succeed, and enable it only when repeated autonomous operation is intended.

Risk: Broad GitLab tokens can increase the impact of mistakes or misuse.

Mitigation: Avoid tokens with release, variable, protected-branch, or broad group privileges unless they are explicitly required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog for GitLab](https://ci-tools.xrow.de/)
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow Skills Project](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [guidance, shell commands, code, configuration, markdown, text]

**Output Format:** [Markdown guidance with shell commands, JSON snippets, and GitLab workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses glab and jq with GITLAB_TOKEN; may create or update GitLab issues, merge requests, branches, labels, reviewer assignments, pipelines, releases, variables, and comments.]

## Skill Version(s):

1.91.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
