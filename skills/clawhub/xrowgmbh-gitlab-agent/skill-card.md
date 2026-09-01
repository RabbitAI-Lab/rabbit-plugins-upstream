## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent discover assigned GitLab issues and merge requests, pass owner and assignment gates, make scoped repository changes, open or update merge requests, and manage workflow labels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad unattended GitLab mutations across repositories, issues, merge requests, labels, pipelines, forks, and possible merge actions.

Mitigation: Install it only in a tightly scoped GitLab account or sandbox, and avoid maintainer or admin-level tokens unless those mutations are intended.

Risk: The skill may continue recurring work such as assigned-item processing and fork maintenance once enabled.

Mitigation: Review the recurring-job and fork-maintenance behavior before enabling the skill for shared or production GitLab projects.

Risk: Incorrect project membership or assignment context could authorize work on the wrong GitLab object.

Mitigation: Keep the owner membership security gate and assignment gate enabled, and require failures to stop work rather than continuing manually.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [GitLab Default Roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools Label Component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw Creating Skills](https://docs.openclaw.ai/tools/creating-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, GitLab CLI commands, code diffs, and status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and jq, with GITLAB_TOKEN as the primary environment variable.]

## Skill Version(s):

1.84.4 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
