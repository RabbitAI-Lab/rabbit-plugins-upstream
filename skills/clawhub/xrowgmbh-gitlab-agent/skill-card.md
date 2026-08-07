## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent discover assigned GitLab issues and merge requests, verify project access and assignment, implement scoped changes, manage labels, pipelines, and merge request delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unattended GitLab write authority can change repositories and project state beyond a narrow assigned-task scope.

Mitigation: Install only when autonomous GitLab work is intended, use a narrowly scoped GitLab account or token, and confirm the owner and assignment gates match the target projects.

Risk: The skill can create or update issues, comments, branches, merge requests, labels, pipelines, forks, and related project workflow state.

Mitigation: Restrict token permissions to the minimum required projects, review generated changes before merge, and monitor GitLab activity for unexpected writes.

Risk: A recurring unattended job could repeatedly act on assigned work.

Mitigation: Enable recurring execution only when changes every 15 minutes are acceptable for the workspace and repository governance model.

## Reference(s):

- [GitLab default roles documentation](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [OpenClaw creating skills guidance](https://docs.openclaw.ai/tools/creating-skills)
- [GitLab skills repository](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitLab CLI actions, code changes, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab, jq, and GITLAB_TOKEN; GitLab writes depend on token permissions and project membership.]

## Skill Version(s):

1.79.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
