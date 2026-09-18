## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to let an agent triage assigned GitLab issues and merge requests, make guarded repository changes, manage workflow labels, run CI follow-up, and prepare review-ready merge requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is designed for recurring autonomous GitLab write activity, including repository, issue, merge request, label, reviewer, fork, and CI changes without per-action approval.

Mitigation: Install it only for intended GitLab accounts and projects, use a tightly scoped GitLab token, monitor its merge requests and pipelines, and keep recurring execution disabled until its behavior is acceptable.

## Reference(s):

- [GitLab Agent on ClawHub](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [xrowgmbh ClawHub publisher profile](https://clawhub.ai/user/xrowgmbh)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [CI Tools label component](https://ci-tools.xrow.de/Components/label)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [GitLab skill source reference](https://gitlab.com/xrow-public/skills)
- [Documentation style reference](references/documentation-style.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, API calls, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, code changes, GitLab comments, merge request descriptions, and JSON helper output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires glab and jq binaries plus a GitLab token in GITLAB_TOKEN.]

## Skill Version(s):

1.91.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
