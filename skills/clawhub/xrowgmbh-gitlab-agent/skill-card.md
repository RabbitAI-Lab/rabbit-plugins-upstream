## Description:

Operate assigned GitLab work with owner-verified project access and guarded MR delivery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xrowgmbh](https://clawhub.ai/user/xrowgmbh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering automation agents use this skill to discover assigned GitLab issues and merge requests, verify owner-created project access, implement changes, open guarded merge requests, manage labels and pipelines, select reviewers, and maintain forks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad autonomous GitLab write authority can push branches, open or update merge requests, change labels and comments, trigger CI, and operate across forks.

Mitigation: Use a dedicated low-privilege GitLab account and token, restrict access to intended projects, and require explicit approval for externally visible writes such as pushes, merge requests, CI triggers, variables, releases, and fork operations.

Risk: Recurring execution has weak user-control boundaries and may continue acting on assigned GitLab work without fresh confirmation.

Mitigation: Enable recurring runs only with a separate approval, a removal plan, clear project scope, and monitoring of labels, merge requests, comments, and pipeline activity.

Risk: Project access and reviewer decisions depend on GitLab membership, assignment, label, and project metadata being complete and current.

Mitigation: Keep the owner membership gate, assignment gate, and deterministic reviewer helper enabled; treat incomplete or ambiguous data as a stop condition requiring human review.

## Reference(s):

- [GitLab Agent ClawHub page](https://clawhub.ai/xrowgmbh/skills/xrowgmbh-gitlab-agent)
- [Documentation style guide](references/documentation-style.md)
- [GitLab default roles](https://docs.gitlab.com/user/permissions/#default-roles)
- [CI Tools Components Catalog](https://ci-tools.xrow.de/)
- [OpenClaw creating skills](https://docs.openclaw.ai/tools/creating-skills)
- [xrow public skills](https://gitlab.com/xrow-public/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, GitLab comments, JSON helper output, and code or configuration changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GITLAB_TOKEN, glab, and jq; helper scripts emit JSON and fail closed on incomplete GitLab membership, reviewer, or label data.]

## Skill Version(s):

1.91.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
